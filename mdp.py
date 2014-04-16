"""Based on code from http://aima-python.googlecode.com/svn/trunk/mdp.py
and related utils functions.

Modified to support Q-Learning and various statistics.
I also fixed Policy Iteration to use delta parameter rather than a fixed
number of policy evaluation steps.
"""

import operator
import random

def update(x, **entries):
  """Update a dict; or an object with slots; according to entries.
  >>> update({'a': 1}, a=10, b=20)
  {'a': 10, 'b': 20}
  >>> update(Struct(a=1), a=10, b=20)
  Struct(a=10, b=20)
  """
  if isinstance(x, dict):
      x.update(entries)
  else:
      x.__dict__.update(entries)
  return x

def argmin(seq, fn):
  """Return an element with lowest fn(seq[i]) score; tie goes to first one.
  >>> argmin(['one', 'to', 'three'], len)
  'to'
  """
  best = seq[0]; best_score = fn(best)
  for x in seq:
      x_score = fn(x)
      if x_score < best_score:
          best, best_score = x, x_score
  return best

def argmax(seq, fn):
  """Return an element with highest fn(seq[i]) score; tie goes to first one.
  >>> argmax(['one', 'to', 'three'], len)
  'three'
  """
  return argmin(seq, lambda x: -fn(x))

def vector_add(a, b):
  """Component-wise addition of two vectors.
  >>> vector_add((0, 1), (8, 9))
  (8, 10)
  """
  return tuple(map(operator.add, a, b))


class MDP:
  """A Markov Decision Process, defined by an initial state, transition model,
  and reward function. We also keep track of a gamma value, for use by
  algorithms. The transition model is represented somewhat differently from
  the text.  Instead of P(s' | s, a) being a probability number for each
  state/state/action triplet, we instead have T(s, a) return a list of (p, s')
  pairs.  We also keep track of the possible states, terminal states, and
  actions for each state. [page 646]"""

  def __init__(self, init, actlist, terminals, gamma=.9):
    update(self, init=init, actlist=actlist, terminals=terminals,
           gamma=gamma, states=set(), reward={})

  def R(self, state):
    "Return a numeric reward for this state."
    return self.reward[state]

  def T(self, state, action):
    """Transition model.  From a state and an action, return a list
    of (probability, result-state) pairs."""
    abstract

  def actions(self, state):
    """Set of actions that can be performed in this state.  By default, a
    fixed list of actions, except for terminal states. Override this
    method if you need to specialize by state."""
    if state in self.terminals:
      return [None]
    else:
      return self.actlist

class GridMDP(MDP):
  """A two-dimensional grid MDP.  All you have to do is
  specify the grid as a list of lists of rewards; use None for an obstacle
  (unreachable state).  Also, you should specify the terminal states.
  An action is an (x, y) unit vector; e.g. (1, 0) means move east."""

  def turn_heading(self, heading, inc):
    return self.actlist[(self.actlist.index(heading) + inc) % len(self.actlist)]

  def turn_right(self, heading):
    return self.turn_heading(heading, -1)

  def turn_left(self, heading):
    return self.turn_heading(heading, +1)

  def __init__(self, grid, terminals, init=(0, 0), gamma=.9, error=.8):
    grid.reverse() ## because we want row 0 on bottom, not on top
    if error < 0 or error > 1:
      raise ValueError("error must be between 0 and 1")
    self.error = error
    MDP.__init__(self, init, actlist=[(1, 0), (0, 1), (-1, 0), (0, -1)],
                 terminals=terminals, gamma=gamma)
    update(self, grid=grid, rows=len(grid), cols=len(grid[0]))
    for x in range(self.cols):
      for y in range(self.rows):
        self.reward[x, y] = grid[y][x]
        if grid[y][x] is not None:
          self.states.add((x, y))

  def T(self, state, action):
    if action is None:
      return [(0.0, state)]
    else:
      return [(self.error, self.go(state, action)),
              ((1 - self.error) / 2, self.go(state, self.turn_right(action))),
              ((1 - self.error) / 2, self.go(state, self.turn_left(action)))]

  def go(self, state, direction):
    "Return the state that results from going in this direction."
    state1 = vector_add(state, direction)
    return state1 if state1 in self.states else state


  def to_grid(self, mapping):
    """Convert a mapping from (x, y) to v into a [[..., v, ...]] grid."""
    return list(reversed([[mapping.get((x,y), '[]')
                           for x in range(self.cols)]
                          for y in range(self.rows)]))

  def to_arrows(self, policy):
    def chars(a, s):
      if a == (1, 0): return '>'
      if a == (0, 1): return '^'
      if a == (-1, 0): return '<'
      if a == (0, -1): return 'v'
      if self.reward[s] < 0: return '-'
      return '+'
    return self.to_grid(
      dict([(s, chars(a, s)) for (s, a) in policy.items()]))

#______________________________________________________________________________

def value_iteration(mdp, epsilon=0.001, solution=lambda a, b: True):
  "Solving an MDP by value iteration."
  U1 = dict([(s, 0) for s in mdp.states])
  R, T, gamma = mdp.R, mdp.T, mdp.gamma
  iterations = 0
  total = 0
  while True:
    iterations += 1
    U = U1.copy()
    delta = 0
    for s in mdp.states:
      U1[s] = R(s) + gamma * max([sum([p * U[s1] for (p, s1) in T(s, a)])
                                  for a in mdp.actions(s)])
      delta = max(delta, abs(U1[s] - U[s]))
      total += 1
    if delta < epsilon * (1 - gamma) / gamma and solution(mdp, best_policy(mdp, U)):
      print "took " + str(iterations) + " iterations, backups: " + str(total)
      return U

def best_policy(mdp, U):
  """Given an MDP and a utility function U, determine the best policy,
  as a mapping from state to action. (Equation 17.4)"""
  pi = {}
  for s in mdp.states:
    pi[s] = argmax(mdp.actions(s), lambda a:expected_utility(a, s, U, mdp))
  return pi

def expected_utility(a, s, U, mdp):
  "The expected utility of doing a in state s, according to the MDP and U."
  return sum([p * U[s1] for (p, s1) in mdp.T(s, a)])

#______________________________________________________________________________

def policy_iteration(mdp, threshold=0.01, solution=lambda a, b: False):
  "Solve an MDP by policy iteration."
  U = dict([(s, 0) for s in mdp.states])
  pi = dict([(s, random.choice(mdp.actions(s))) for s in mdp.states])
  iterations = 0
  total = 0
  R, T, gamma = mdp.R, mdp.T, mdp.gamma
  while True:
    iterations += 1
    while True:
      delta = 0
      for s in mdp.states:
        total += 1
        temp = U[s]
        U[s] = R(s) + gamma * sum([p * U[s1] for (p, s1) in T(s, pi[s])])
        delta = max(delta, abs(temp - U[s]))
      if delta < threshold: break
    unchanged = True
    for s in mdp.states:
      a = argmax(mdp.actions(s), lambda a: expected_utility(a,s,U,mdp))
      if a != pi[s]:
        pi[s] = a
        unchanged = False
    if unchanged or solution(mdp, pi):
      print "took " + str(iterations) + " iterations, backups: " + str(total)
      return pi

#______________________________________________________________________________

def weighted_choice(states):
  r = random.random()
  ps = 0
  for p, s in states:
    ps += p
    if r <= ps:
      return s
  return states[-1][1]

def qlearning(mdp, state, Q={}, alpha=0.001):
  """Pseudo-code from Sutton:
    Initialize Q(s, a) arbitrarily (in our case zeroes)
    Repeat (for each episode)
        Choose a from s using policy derived from Q (e.g. epsilon-greedy)
        Take action a, observe r and s'
        Q(s, a) <- Q(s, a) + alpha[r + gamma(max(Q(s', a')) - Q(s, a))]
        s <- s'
    until s' is terminal
  """
  R, T, gamma = mdp.R, mdp.T, mdp.gamma
  s = state
  steps = 0
  while s not in mdp.terminals:
    steps += 1
    a = random.choice(mdp.actions(s))
    current = Q.get((s, a), 0)
    s1 = weighted_choice(T(s, a))
    max_available = max([Q.get((s1, a1), 0) for a1 in mdp.actions(s1)])
    Q[(s, a)] = current + alpha * (R(s1) + gamma * (max_available - current))
    s = s1
  return steps

def qlearn(mdp, state, iterations):
  Q = {}
  steps = 0
  for _ in range(iterations):
    if not Q:
      steps += qlearning(mdp, state, Q)
    else:
      steps += qlearning(mdp, random.choice(Q.keys())[0], Q)
  print "took %s iterations, steps: %s" % (iterations, steps)
  return Q

def best_policyQ(mdp, Q):
  """Given an MDP and the Q function, determine the best policy,
  as a mapping from state to action."""
  pi = {}
  for s in mdp.states:
    pi[s] = argmax(mdp.actions(s), lambda a:Q.get((s, a), 0))
  return pi