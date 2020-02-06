import numpy.random as rndm
from graphics import *
from entity import *


class Plant(Entity):
    __ticks_from_breed = 0
    __ticks_to_breed = 10
    __neighbours_to_not_breed = 10
    _speed = 200 #For Plants this means how far they can breed
    
    def _additional_initialization(self):
        self._nutrition_value = 10

    def _breeding_changes(self):
        Plant.__ticks_from_breed = 0

    def _mutate_copy(self):
        new_p = Plant(self._x, self._y, self._max_x, self._max_y, self._color)
        new_p.move_random()
        return new_p
    
    def can_breed(self, neighbours):
        timer_allows = Plant.__ticks_from_breed >= Plant.__ticks_to_breed
        neighbours_allow = neighbours < Plant.__neighbours_to_not_breed
        return timer_allows
    
    def set_ticks_to_breed(new_amount):
        Plant.__ticks_to_breed = new_amount

    def tick(self):
        Plant.__ticks_from_breed += 1