import numpy.random as rndm
from math import floor, exp
from entityHandler import *
from plant import *


class PlantHandler(EntityHandler):
    __max_hops = 10
    __personal_space = 10
    __neighbour_radius = 50
    __breeding_slowing_rate = 0.01

    def add(self, plan):
        if not isinstance(plan, Plant):
            raise TypeError("PlantHandler handles only Plants")
        hops = 0
        (x, y) = plan.get_coords()
        while self.entities_in_range((x,y), self.__personal_space) !=0 and hops < self.__max_hops :
            (x, y) = plan.move_random()
            hops +=1
        if hops < self.__max_hops and self.entities_in_range((x,y), self.__personal_space)==0:
            self._entities.add(plan)      
            Plant.set_ticks_to_breed(exp(self.get_amount()*self.__breeding_slowing_rate))


    def add_random(self, max_x, max_y, amount=1):
        for i in range(amount) :
            new_plant = Plant(floor(max_x*rndm.uniform()),floor(max_y*rndm.uniform()), max_x, max_y, tuple(rndm.randint(low=0,high=255,size=3)))
            self.add(new_plant)
            
    def breed_die_all(self):
        bred_ps = set()
        dying_ps = set()
        for p in self._entities:
            if p.can_breed(self.entities_in_range(p.get_coords(), self.__neighbour_radius)):
                new_p = p.breed()
                bred_ps.add(new_p)
            if p.is_dying():
                dying_ps.add(p)
        for np in bred_ps:
            self.add(np)
        for dp in dying_ps:
            dp.undraw()
            self._entities.remove(dp)