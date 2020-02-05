from entity import *


class Agent(Entity):
    _speed = 5
    _radius = 10
    _eating_range = 50
    _can_eat_amount = 10
    _initial_nutr_value = 100
    _initial_hunger = 500
    
    def _additional_initialization(self):
        self._nutrition_value = self._initial_nutr_value
        self._hunger = Agent._initial_hunger

    def _init_graphic(self):
        self._graphic = Circle(Point(self._x,self._y), self._radius)
        self._graphic.setFill(color_rgb(self._color[0],self._color[1],self._color[2]))

    def tick(self):
        self.move_random()
        self._hunger -= 1
        if self._hunger < 1 :
            self._is_dying = True
    
    def eat(self, nutr_value, amount):
        self._hunger += nutr_value*amount
    
    def eating_range(self):
        return self._eating_range
        
    def can_eat_amount(self):
        return self._can_eat_amount
        

class Predator(Agent):
    _speed = 15
    _radius = 10
    _eating_range = 100
    _can_eat_amount = 1
    _initial_nutr_value = 50
    _initial_hunger = 1000
    
    
class Prey(Agent):
    _speed = 5
    _radius = 50
    _eating_range = 50
    _can_eat_amount = 10
    _initial_nutr_value = 500
    _initial_hunger = 500
    