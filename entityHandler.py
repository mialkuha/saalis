from math import pow
from entity import *
from graphics import *


class EntityHandler(object):
    def __init__(self):
        self._entities = set()

    def __str__(self):
        strin = ""
        for e in self._entities:
            strin += str(e) + "\n"
        return strin

    def _entities_in_range(self, origin, range, ret_objects=False):
        if ret_objects:
            ret = []
        else :
            ret = 0
        r2 = pow(range,2)
        (o_x, o_y) = origin
        for e in self._entities:
            (x, y) = e.get_coords()
            dist2 = pow(x-o_x,2) + pow(y-o_y,2)
            if r2 > dist2:
                if ret_objects:
                    ret += (e, dist2)
                else :
                    ret +=1
        return ret
        
    def add(self):
        pass #This is supposed to be overloaded, so that type-checking is done in the child class
        
    def get_amount(self):
        return len(self._entities)

    def tick_all(self):
        bred_es = set()
        for e in self._entities:
            e.tick()
            if e.can_breed():
                new_e = e.breed()
                bred_es.add(new_e)
        for ne in bred_es:
            self.add(ne)

    def draw_all(self, win):
        for e in self._entities:
            e.draw(win)