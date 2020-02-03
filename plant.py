import numpy.random as rndm
from math import sin, cos, pi
from graphics import *
from entity import *


class Plant(Entity):
    __g_ticks_from_breed = 0
    __g_ticks_to_breed = 10
    __g_breed_range = 40
    
    def _additional_initialization(self):
        self._graphic = Point(self._x,self._y)
        self._graphic.setOutline(color_rgb(self._color[0],self._color[1],self._color[2]))
        self.drawn = False

    def _breeding_changes(self):
        Plant.__g_ticks_from_breed = 0

    def _mutate_copy(self):
        r = rndm.uniform(0,Plant.__g_breed_range)
        theta = rndm.uniform(0,2*pi)
        m_x = self._x + r*cos(theta)
        m_y = self._y + r*sin(theta)
        m_color = self._color
        new_p = Plant(m_x, m_y, self._max_x, self._max_y, m_color)
        new_p.move_inbounds()
        return new_p
    
    def can_breed(self):
        return Plant.__g_ticks_from_breed >= Plant.__g_ticks_to_breed

    def tick(self):
        Plant.__g_ticks_from_breed += 1
        
    def draw(self, win):
        self._graphic.draw(win)
        self.drawn = True