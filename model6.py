# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 20:23:59 2019

@author: de-sinnett
"""
# Import random, operator, plotting, animation, timer and csv modules, and Agent Class
import random
import operator
import matplotlib.pyplot
import matplotlib.animation
import time
import agentframework
import csv

# Start the clock
start = time.clock()

# Open the input file
f = open('in.txt')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

# Create an empty list
environment = []

# Read in input data
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)

# Create a new empty list
agents = []

# Control how many agents
num_of_agents = 10

# Control number of iterations
num_of_iterations = 100

# Controls number of neighbours
neighbourhood = 20

# Set the animation pane
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Set up agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

# Set the stopping criteria    
carry_on = True

# Define the animation
def update(frame_number):
    fig.clear()
    global carry_on
    # Move the agents, make them eat and share with neighbours
    for j in range(num_of_iterations):
        random.shuffle(agents)
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
        # Set the stopping criteria
        if random.random() < 0.1:
            carry_on = False
            print ("stopping condition")
    # Plot the agents        
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)

# Define the stopping condition
def gen_function(b = [0]):
    a = 0
    global carry_on
    while (a < 10) & (carry_on):
        # Returns control and waits next call
        yield a
        a = a + 1
        
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.imshow(environment)
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
#animation = matplotlib.animation.FuncAnimation(fig, update, repeat=False, frames=gen_function)

# Stops the clocl
end = time.clock()
print("time = " + str(end - start))

# Calculate max and min distance
# Optimise so it doesn't repeat pairs of agents or test agents against themselves
# Orders of magnitude of agents versus times and plot as a scattergraph

# Write out environment as a file at the end
# Write a second file that writes out the total amount stored by all agents on a line
# Append the data on the file each time it runs rather than clearing it each time
# Override __str__(self) in the agents, as mentioned in lecture in classes,so they display this information about about their location and stores when printed
# Get the agents to wander around the full environment by finding out the size of the environment inside the agents, and using the size when you randomise their starting locations and deal with the boundary conditions
# Get the agents to eat the last few bits if there's less than 10 left, without leaving negative values
# Get the agents to sick up their store in a location if they're eaten more than 100 units (colours will rescale)

# Get the model that it reads the parameters from command line using argv so it runs like: python model.py 200 20 30 (where 200 is agents, 20 iterations, 30 neighbourhood). Remember need to type something to catch exceptsions when user types something that can't be cast to an int.
# Write a python program that uses subprocess.call to run the model with a variety of results using ranges to set those parameters (remember to leave some defaults) e.g. stepping up agent numbers by 10 each time it runs, and append the total amount stored to a file for each run (parameter sweeping)?
# May want an argv variable that also turns off visual output for multiple runs (see StackOverflow answer)

# Show agents animating and environment?

