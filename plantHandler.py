import numpy.random as rndm
from entityHandler import *
from plant import *


class PlantHandler(EntityHandler):
    def add(self, plan):
        if not isinstance(plan, Plant):
            raise TypeError("PlantHandler handles only Plants")
        self._entities.add(plan)

    def add_random(self, max_x, max_y, amount=1):
        for i in range(amount) :
            new_plant = Plant(max_x*rndm.uniform(),max_y*rndm.uniform(), max_x, max_y, tuple(rndm.randint(low=0,high=255,size=3)))
            self.add(new_plant)

    def draw_all(self, win):
        for e in self._entities:
            e.draw(win)