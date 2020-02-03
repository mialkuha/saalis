import numpy.random as rndm
from graphics import *
from entity import *


class Agent(Entity):
    def _additional_initialization(self):
        self._graphic = Circle(Point(self._x,self._y), self._size)
        self._graphic.setFill(color_rgb(self._color[0],self._color[1],self._color[2]))

    def _move_random(self):
        dx = rndm.uniform(-10,10)
        dy = rndm.uniform(-10,10)
        if (self._x + dx > self._max_x) :
            dx = self._max_x - self._x
            self._x = self._max_x
        if (self._y > self._max_y) :
            dy = self._max_y - self._y
            self._y = self._max_y
        if (self._x + dx < 0) :
            dx = -self._x
            self._x = 0
        if (self._y < 0) :
            dy = -self._y
            self._y = 0
        self._graphic.move(dx,dy)

    def tick(self):
        self._move_random()
        
    def draw(self, win):
        self._graphic.draw(win)