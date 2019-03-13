# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 20:23:59 2019

@author: de-sinnett
"""
# Import random, operator and plotting modules
import random
import operator
import matplotlib.pyplot

# Create a new empty list
agents = []

# Set up variables to start at random coordinates in a 100x100 grid (agent 1)
agents.append([random.randint(0,99),random.randint(0,99)])

# Random walk one step
if random.random() < 0.5:
    agents[0][0] = agents[0][0] + 1
else:
    agents[0][0] = agents[0][0] - 1

if random.random() < 0.5:
    agents[0][1] = agents[0][1] + 1
else:
    agents[0][1] = agents[0][1] - 1

# Set up variables to start at random coordinates in a 100x100 grid (agent 2)
agents.append([random.randint(0,99),random.randint(0,99)])

# Random walk one step
if random.random() < 0.5:
    agents[1][0] = agents[1][0] + 1
else:
    agents[1][0] = agents[1][0] - 1

if random.random() < 0.5:
    agents[1][1] = agents[1][1] + 1
else:
    agents[1][1] = agents[1][1] - 1
    
print (agents)

# Print agent with maximum value in first co-ordinate
print (max(agents))

# Print agent with maximum value in second co-ordinate
print (max(agents, key=operator.itemgetter(1)))

# Plot the agents
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.scatter(m[1], m[0], color='red')
matplotlib.pyplot.show()
