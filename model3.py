# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 20:23:59 2019

@author: de-sinnett
"""
# Import random, operator, plotting and timer modules
import random
import operator
import matplotlib.pyplot
import time

# Start the clock
start = time.clock()

# Define distance calculation between agents
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5

# Create a new empty list
agents = []

# Control how many agents
num_of_agents = 10

# Control number of iterations
num_of_iterations = 100

# Set up variables to start at random coordinates in a 100x100 grid (agent 1)
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

# Print agent starting co-ordinates
print(agents)

# Random walk 100 steps
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100

# Print agent stopping co-ordinates
print(agents)

# Calculate Euclidian distance between all agents
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        print(distance)

# Stop the clock
end = time.clock()
print("time = " + str(end - start))

# Print agent with maximum first co-ordinate
print (max(agents))

# Print agent with maxmimum second co-ordinate
print (max(agents, key = operator.itemgetter(1)))

# Plot agents
for i in range(num_of_agents):
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

# Calculate max and min distance
# Optimise so it doesn't repeat pairs of agents or test agents against themselves
# Orders of magnitude of agents versus times and plot as a scattergraph
