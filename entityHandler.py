from entity import *


class EntityHandler(object):
    def __init__(self):
        self._entities = set()

    def __str__(self):
        strin = ""
        for e in self._entities:
            strin += str(e) + "\n"
        return strin
        
    def add(self):
        pass #This is supposed to be overloaded, so that type-checking is done in the child class

    def tick_all(self):
        bred_es = set()
        for e in self._entities:
            e.tick()
            if e.can_breed():
                new_e = e.breed()
                bred_es.add(new_e)
        for ne in bred_es:
            self.add(ne)