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
    
    def _after_tick_action(self, entit):
        pass

    def entities_in_range(self, origin, rang, ret_objects=False):
        if ret_objects:
            ret = []
        else :
            ret = 0
        r2 = pow(rang,2)
        (o_x, o_y) = origin
        for e in self._entities:
            (x, y) = e.get_coords()
            dist2 = pow(x-o_x,2) + pow(y-o_y,2)
            if r2 > dist2:
                if ret_objects:
                    ret.append((e, dist2))
                else :
                    ret +=1
        return ret
        
    def add(self):
        pass #This is supposed to be overloaded, so that type-checking is done in the child class
        
    def get_amount(self):
        return len(self._entities)

    def tick_all(self):
        for e in self._entities:
            e.tick()

    def breed_die_all(self):
        bred_es = set()
        dying_es = set()
        for e in self._entities:
            if e.can_breed():
                new_e = e.breed()
                bred_es.add(new_e)
            if e.is_dying():
                dying_es.add(e)
        for ne in bred_es:
            self.add(ne)
        for de in dying_es:
            de.undraw()
            self._entities.remove(de)

    def draw_all(self, win):
        for e in self._entities:
            e.draw(win)