# Generating code that updates a given  probability twice
# and gives the posterior distribution after both 
# values of the measurement are incorporated. The code allows for 
# any sequence of measurement of any length.

p = [0.2, 0.2, 0.2, 0.2, 0.2] # Initial probability array
world = ['green', 'red', 'red', 'green', 'green'] # The world as observed
measurements = ['red', 'green'] # The measurements (Z)
pHit = 0.6 # Probability of a hit
pMiss = 0.2 # Probability of a miss

def sense(p, Z): # Create the sense function
    q = [] # Create the empty array
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q) # Sum the values in the array
    
    for i in range(len(q)): # Normalize the array to return probabilities to 1
        q[i] = q[i] / s
    return q

for j in range(len(measurements)): # Incorporate measurements of any length
    p = sense(p, measurements[j])

print p # Return the posterior distribution