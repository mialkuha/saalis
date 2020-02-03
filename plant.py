import numpy.random as rndm
from graphics import *
from entity import *


class Plant(Entity):
    
    def _additional_initialization(self):
        self._graphic = Point(self._x,self._y)
        self._graphic.setOutline(color_rgb(self._color[0],self._color[1],self._color[2]))

    def tick(self):
        pass #TODO
        
    def draw(self, win):
        self._graphic.draw(win)