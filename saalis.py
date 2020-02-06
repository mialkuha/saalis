from graphics import *
from agentHandler import *
from plantHandler import *

class Saalis:

    def __init__(self):
        pass
        

class World(object):
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._preys = AgentHandler()
        self._predators = AgentHandler()
        self._plants = PlantHandler()
        self._win = GraphWin("World", width, height, autoflush=False)
    
    def add_random(self, amount=1):
        self._preys.add_random(self._width, self._height, Prey, amount*amount)
        self._preys.draw_all(self._win)
        self._predators.add_random(self._width, self._height, Predator, amount)
        self._predators.draw_all(self._win)
        self._plants.add_random(self._width, self._height, amount*amount)
        self._plants.draw_all(self._win)
    
    def tick(self):
        self._preys.tick_all()
        self._predators.tick_all()
        self._plants.tick_all()
        
        self._preys.all_try_eating(self._plants)
        self._predators.all_try_eating(self._preys)
        
        self._preys.breed_die_all()
        self._predators.breed_die_all()
        self._plants.breed_die_all()
        
        if (self._plants.get_amount()==0):
            self._plants.add_random(self._width, self._height, Prey, 1)
        if (self._predators.get_amount()==0):
            self._predators.add_random(self._width, self._height, Predator, 1)
        if (self._preys.get_amount()==0):
            self._preys.add_random(self._width, self._height, Prey, 1)
        
        print("Plants:"+str(self._plants.get_amount())+", Preys:"+str(self._preys.get_amount())+", Predators:"+str(self._predators.get_amount()))
        
        self._preys.draw_all(self._win)
        self._predators.draw_all(self._win)
        self._plants.draw_all(self._win)
        update()