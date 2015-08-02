# Finalized python code that implements the basic essence of Google's self driving car localization system

p = [0.2, 0.2, 0.2, 0.2, 0.2] # Initial probabilities
world = ['green', 'red', 'red', 'green', 'green'] # The world the robot is in
measurements = ['red', 'red'] # The measurements the car has seen (can be scaled to be done by image)
motions = [1,1] # The motions taken (first right once and then right again)
pHit = 0.6 # Probability of a hit
pMiss = 0.2 # Probabilty of a miss
pExact = 0.8 # Probability of being in the right location
pOvershoot = 0.1 # Probability of overshooting
pUndershoot = 0.1 # Probability of under-shooting

def sense(p, Z): # The basic sensing function
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U): # The basic movement function
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q

for k in range(len(measurements)): # Loop that iterates through all the measurements
    p = sense(p, measurements[k])
    p = move(p, motions[k])
    
print p # Print showing the final posterior distribution (used to verify final location)
