import numpy.random as rndm
from entityHandler import *
from agent import *


class AgentHandler(EntityHandler):
    def add(self, agen):
        if not isinstance(agen, Agent):
            raise TypeError("AgentHandler stores only Agents")
        self._entities.add(agen)

    def add_random(self, max_x, max_y, amount=1):
        for i in range(amount) :
            new_agent = Agent(max_x*rndm.uniform(),max_y*rndm.uniform(), max_x, max_y, tuple(rndm.randint(low=0,high=255,size=3)))
            self.add(new_agent)

    def draw_all(self, win):
        for e in self._entities:
            e.draw(win)