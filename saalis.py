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
        self._agents = AgentHandler()
        self._plants = PlantHandler()
        self._win = GraphWin("World", width, height, autoflush=False)
    
    def add_random(self, amount=1):
        self._agents.add_random(self._width, self._height, amount)
        self._agents.draw_all(self._win)
        self._plants.add_random(self._width, self._height, amount)
        self._plants.draw_all(self._win)
    
    def tick(self):
        self._agents.tick_all()
        self._plants.tick_all()
        print("Plants:"+str(self._plants.get_amount())+", Agents:"+str(self._agents.get_amount()))
        self._agents.draw_all(self._win)
        self._plants.draw_all(self._win)
        update()