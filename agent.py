from entity import *


class Agent(Entity):
    _speed = 5
    _radius = 10
    _eating_range = 50
    _can_eat_amount = 10
    _initial_nutr_value = 100
    _initial_hunger = 500
    _initial_hunger_for_breed = 300
    _initial_need_eat_after_breed = 1
    _breed_hunger_multiplier = 0.5
    
    def _additional_initialization(self):
        self._nutrition_value = self._initial_nutr_value
        self._hunger = self._initial_hunger
        self._hunger_for_breed = self._initial_hunger_for_breed
        self._need_eat_after_breed = self._initial_need_eat_after_breed
        self._eaten_after_breed = 0

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
        self._eaten_after_breed += 1
    
    def eating_range(self):
        return self._eating_range
        
    def can_eat_amount(self):
        return self._can_eat_amount
        
    def can_breed(self):
        return (self._eaten_after_breed > self._need_eat_after_breed) and (self._hunger > self._hunger_for_breed)
    
    def _breeding_changes(self):
        self._hunger *= self._breed_hunger_multiplier
        self._eaten_after_breed = 0

    def _mutate_copy(self):
        new_e = type(self)(self._x, self._y, self._max_x, self._max_y, self._color)
        new_e.move_random()
        return new_e


class Predator(Agent):
    _speed = 20
    _radius = 10
    _eating_range = 100
    _can_eat_amount = 1
    _initial_nutr_value = 50
    _initial_hunger = 1000
    _initial_hunger_for_breed = 500
    _initial_need_eat_after_breed = 1
    _breed_hunger_multiplier = 0.7
    
    
class Prey(Agent):
    _speed = 30
    _radius = 50
    _eating_range = 50
    _can_eat_amount = 10
    _initial_nutr_value = 500
    _initial_hunger = 500
    _initial_hunger_for_breed = 300
    _initial_need_eat_after_breed = 10
    _breed_hunger_multiplier = 0.3
    