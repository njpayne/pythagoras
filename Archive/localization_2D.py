# Finalized Python code that implements the basic essence of Google's self driving car localization system in a 2D grid
# Monte Carlo robot localization using histogram fitters

# In principle, these below are carefully assembled 2D models of the roads surface
# That does not affect what is below. Rather, it makes the measurement function more involved
# To do this, we need to replace the simple matching with an image matching
colors = [['red', 'green', 'green',   'red', 'red'],
          ['red',   'red', 'green',   'red', 'red'],
          ['red',   'red', 'green', 'green', 'red'],
          ['red',   'red',   'red',   'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']

p = [[1./20, 1./20, 1./20, 1./20, 1./20],
     [1./20, 1./20, 1./20, 1./20, 1./20],
     [1./20, 1./20, 1./20, 1./20, 1./20],
     [1./20, 1./20, 1./20, 1./20, 1./20]]

motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7 # This is the probability that the sensor is right

p_move = 0.8 # This is the probability that the car moves

def show(p):
    for i in range(len(p)):
        print p[i]

sensor_wrong = 1 - sensor_right # This is the probability that the sensor is wrong
p_stay = 1 - p_move # This is the complement of the probability of moving

# Create a sense function
def sense(p, colors, measurement): # Input the probability distribution & map
    component = [[0.0 for row in range(len(p[0]))] for col in range(len(p))]
    # component creates a new posterior distribution that is initialized with zeros

    s = 0.0
    for i in range(len(p)): # Iterate over all elements in the cell
        for j in range(len(p[i])):
            hit = (measurement == colors[i][j]) # Check whether the measurements match
            component[i][j] = p[i][j] * (hit * sensor_right + (1-hit) * sensor_wrong)
            # Above, the non-normalized posterior is the prior times the sum that depends on the sensor
            s += component[i][j] # Add up all the values in component to give total probability
    
    for i in range(len(component)):
        for j in range(len(p[i])):
            component[i][j] /= s # This is used to normalize the values 

    return component # Return the probability distribution   

# Create the movement function
def move(p, motion): # Input a distribution and a motion vector
    component = [[0.0 for row in range(len(p[0]))] for col in range(len(p))]
  
    for i in range(len(p)): # For each cell, I collect possible cells that the robot might have come from
        for j in range(len(p[i])):
            component[i][j] = (p_move * p[(i - motion[0]) % len(p)][(j - motion[1]) % len(p[i])]) + (p_stay * p[i][j])
            # Note that here we minus the motion, indicating we are going back in time
            # If we don't move, then we use the probability of a specific cell * the probability of staying!
    return component # I simply return the corresponding distribution
    # Note that I don't have to normalize here

# Include relevant validation (optional)
if len(measurements) != len(motions): # Check if measurements vector is same as motions vector
    raise ValueError, "There is an error in the size of the measurements and motions vector!"

# These two lines generate an initial uniform distribution
# This is the initial initialization of the probability table
pinit = 1.0 / float(len(colors)) / float(len(colors[0])) # Rows * columns
# This initializes p as 1 / 20 because there are 20 grid cells
p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]
# p creates an array that is the size of the colors array, initialized with the value of p

for k in range(len(measurements)): # Iterate through the measurements
    p = move(p, motions[k]) # Move & provide the current distribution & motions
    p = sense(p, colors, measurements[k]) # Take current distribution, world, and measurement
    # This generates a bew probability distribution

show(p) # Output the final probability distribution
