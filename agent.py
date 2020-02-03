import numpy.random as rndm
from graphics import *
from entity import *


class Agent(Entity):
    _size = 10
    
    def _additional_initialization(self):
        self._graphic = Circle(Point(self._x,self._y), self._size)
        self._graphic.setFill(color_rgb(self._color[0],self._color[1],self._color[2]))

    def _move_random(self):
        oldx = self._x
        oldy = self._y
        self._x += rndm.uniform(-10,10)
        self._y += rndm.uniform(-10,10)
        self.move_inbounds()
        self._graphic.move(self._x-oldx,self._y-oldy)

    def tick(self):
        self._move_random()
        
    def draw(self, win):
        self._graphic.draw(win)