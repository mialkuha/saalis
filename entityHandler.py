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
        for e in self._entities:
            e.tick()