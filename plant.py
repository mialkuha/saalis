import numpy.random as rndm
from graphics import *
from entity import *


class Plant(Entity):
    __ticks_from_breed = 0
    __ticks_to_breed = 10
    _speed = 200 #For Plants this means how far they can breed
    
    def _additional_initialization(self):
        self._nutrition_value = 10

    def _breeding_changes(self):
        Plant.__ticks_from_breed = 0
    
    def can_breed(self):
        timer_allows = Plant.__ticks_from_breed >= Plant.__ticks_to_breed
        return timer_allows
    
    def set_ticks_to_breed(new_amount):
        Plant.__ticks_to_breed = new_amount

    def tick(self):
        Plant.__ticks_from_breed += 1