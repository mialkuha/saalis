from entity import *


class Agent(Entity):
    _radius = 10
    _speed = 10
    
    def _additional_initialization(self):
        self._hunger = 100

    def _init_graphic(self):
        self._graphic = Circle(Point(self._x,self._y), self._radius)
        self._graphic.setFill(color_rgb(self._color[0],self._color[1],self._color[2]))

    def tick(self):
        self.move_random()
        self._hunger -= 1
        if self._hunger < 1 :
            self._is_dying = True