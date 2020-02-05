import numpy.random as rndm
from entityHandler import *
from agent import *


class AgentHandler(EntityHandler):
    def _after_tick_action(self, agen):
        pass

    def add(self, agen):
        if not isinstance(agen, Agent):
            raise TypeError("AgentHandler handles only Agents")
        self._entities.add(agen)

    def add_random(self, max_x, max_y, type, amount=1):
        for i in range(amount) :
            new_agent = type(max_x*rndm.uniform(),max_y*rndm.uniform(), max_x, max_y, tuple(rndm.randint(low=0,high=255,size=3)))
            self.add(new_agent)
            
    def all_try_eating(self, others):
        for agen in self._entities:
            how_many = self._agent_tries_eating(agen, others)
        
            
    def _agent_tries_eating(self, agen, others):
        if not isinstance(agen, Agent):
            raise TypeError("AgentHandler handles only Agents' eatings")
        if not isinstance(others, EntityHandler):
            raise TypeError("Can't eat something that isn't an Entity")
        in_range = others.entities_in_range(agen.get_coords(), agen.eating_range(),True)
        if len(in_range) > 0:
            in_range.sort(key=(lambda a : a[1]),reverse=False)
            how_many = min(len(in_range), agen.can_eat_amount())
            agen.eat(in_range[0][0].get_nutrition_value(), how_many)
            for i in range(how_many) :
                in_range[i][0].kill()
            return how_many
        return 0