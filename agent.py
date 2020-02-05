import numpy.random as rndm
from math import floor
from graphics import *
from entity import *


class Agent(Entity):
    _radius = 10
    
    def _additional_initialization(self):
        pass

    def _init_graphic(self):
        self._graphic = Circle(Point(self._x,self._y), self._radius)
        self._graphic.setFill(color_rgb(self._color[0],self._color[1],self._color[2]))

    def _move_random(self):
        oldx = self._x
        oldy = self._y
        self._x += rndm.uniform(-10,10)
        self._y += rndm.uniform(-10,10)
        self.move_inbounds(Agent._radius*2)

    def tick(self):
        self._move_random()