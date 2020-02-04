import numpy.random as rndm
from math import sin, cos, pi, floor
from graphics import *
from entity import *


class Plant(Entity):
    __g_ticks_from_breed = 0
    __g_ticks_to_breed = 1
    __g_breed_range = 200
    
    def _additional_initialization(self):
        self._graphic = Circle(Point(self._x,self._y), 100)#Point(self._x,self._y)
        self._graphic.setOutline(color_rgb(self._color[0],self._color[1],self._color[2]))

    def _breeding_changes(self):
        Plant.__g_ticks_from_breed = 0

    def _mutate_copy(self):
        r = rndm.uniform(0,Plant.__g_breed_range)
        theta = rndm.uniform(0,2*pi)
        m_x = self._x + floor(r*cos(theta))
        m_y = self._y + floor(r*sin(theta))
        m_color = self._color
        new_p = Plant(m_x, m_y, self._max_x, self._max_y, m_color)
        new_p.move_inbounds()
        return new_p

    def get_coords(self):
        return (self._x,self._y)
    
    def can_breed(self):
        timer_allows = Plant.__g_ticks_from_breed >= Plant.__g_ticks_to_breed
        return timer_allows

    def tick(self):
        Plant.__g_ticks_from_breed += 1

    def move(self):
        r = rndm.uniform(0,Plant.__g_breed_range)
        theta = rndm.uniform(0,2*pi)
        self._x += floor(r*cos(theta))
        self._y += floor(r*sin(theta))
        self.move_inbounds()
        return (self._x,self._y)
        
    def draw(self, win):
        self._graphic.undraw()
        self._graphic = Circle(Point(self._x,self._y), 100)#Point(self._x,self._y)
        self._graphic.setOutline(color_rgb(self._color[0],self._color[1],self._color[2]))
        self._graphic.draw(win)