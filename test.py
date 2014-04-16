from mdp import GridMDP
from mdp import best_policy
from mdp import value_iteration
from mdp import policy_iteration
from mdp import qlearn
from mdp import best_policyQ

def isnumber(x):
  "Is x a number? We say it is if it has a __int__ method."
  return hasattr(x, '__int__')

def print_table(table, header=None, sep='   ', numfmt='%g'):
  """Print a list of lists as a table, so that columns line up nicely.
  header, if specified, will be printed as the first row.
  numfmt is the format for all numbers; you might want e.g. '%6.2f'.
  (If you want different formats in different columns, don't use print_table.)
  sep is the separator between columns."""
  justs = [('rjust' if isnumber(x) else 'ljust') for x in table[0]]
  if header:
    table = [header] + table
  table = [[(numfmt % x if isnumber(x) else x) for x in row]
           for row in table]
  maxlen = lambda seq: max(map(len, seq))
  sizes = map(maxlen, zip(*[map(str, row) for row in table]))
  for row in table:
    print sep.join(getattr(str(x), j)(size)
                   for (j, size, x) in zip(justs, sizes, row))

prize = 1
trap = -1
neg = -0.4

mdp1 = GridMDP([[neg, trap, prize],
                [neg, None, neg],
                [neg,  neg, neg]],
                terminals=[(1, 2), (2, 2)],
                error=.8)

print "GRID"
print
print "Value iteration"
pi = best_policy(mdp1, value_iteration(mdp1, .01))
print_table(mdp1.to_arrows(pi))

print "Policy iteration"
print_table(mdp1.to_arrows(policy_iteration(mdp1)))

print "Q Learning"
pi = best_policyQ(mdp1, qlearn(mdp1, (0, 0), 5000))
print_table(mdp1.to_arrows(pi))