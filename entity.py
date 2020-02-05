import numpy.random as rndm
from math import sin, cos, pi
from graphics import *

class Entity(object):
    _speed = 10 #How many pixels can this move in a tick
    
    def __init__(self, x, y, max_x, max_y, color):
        self._x = x
        self._y = y
        self._max_x = max_x
        self._max_y = max_y
        self._color = color
        self._is_dying = False
        self._nutrition_value = 0 #This depends on type
        self.move_inbounds()
        self._init_graphic()
        self._additional_initialization() #Things that depend on type
        
    def __str__(self):
        return ""+str(type(self))+" "+str(self._x)+" "+str(self._y)+" "+str(self._color)

    def _init_graphic(self):
        self._graphic = Point(self._x,self._y)
        self._graphic.setOutline(color_rgb(self._color[0],self._color[1],self._color[2]))

    def _additional_initialization(self):
        pass

    def _breeding_changes(self):
        pass

    def _mutate_copy(self):
        pass
    
    def tick(self):
        pass
    
    def can_breed(self):
        pass

    def get_coords(self):
        return (self._x,self._y)

    def get_nutrition_value(self):
        return self._nutrition_value

    def is_dying(self):
        return self._is_dying
    
    def kill(self):
        self._is_dying = True
    
    def move_inbounds(self, buffer=0):
        if (self._x < 0):
            self._x = buffer
        elif (self._x > self._max_x):
            self._x = self._max_x-buffer
        if (self._y < 0):
            self._y = buffer
        elif (self._y > self._max_y):
            self._y = self._max_y-buffer

    def move_random(self):
        r = rndm.uniform(0,self._speed)
        theta = rndm.uniform(0,2*pi)
        self._x += r*cos(theta)
        self._y += r*sin(theta)
        self.move_inbounds()
        return (self._x,self._y)
    
    def breed(self):
        self._breeding_changes() #what happens to the entity on breeding depends on type
        return self._mutate_copy()
        
    def undraw(self):
        self._graphic.undraw()
        
    def draw(self, win):
        self._graphic.undraw()
        self._init_graphic()
        self._graphic.draw(win)