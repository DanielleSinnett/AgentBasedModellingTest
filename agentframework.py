# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 19:42:49 2019

@author: de-sinnett
"""
import random

# Define a class called Agent
class Agent:        
    def __init__ (self, environment, agents):
        self._x = random.randint(0,99)
        self._y = random.randint(0,99)
        self.environment = environment
        self.store = 0
        self.agents = agents
    
    # Move agents 100 random steps
    def move(self):        
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100

    # Set agents to eat environment
    def eat(self):
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
    
    # Calculate Euclidean distance between agents
    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5
    
    # Set agents to share with neighbours
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                average = (self.store + agent.store) / 2.0
                self.store = average
                agent.store = average
            else:
                print(distance)
        print("Sharing " + str(distance) + " " + str(average))
            
    # Add a property for the _x variable
    @property
    def x(self):
        print("I am the agent's x coordinate")
        return self._x
    @property
    def y(self):
        print("I am the agent's y coordinate")
        return self._y
    
    #@x.setter
    #def x(self, value):
        #self._x = value
    #@y.setter
    #def y(self, value):
        #self._y = value