from math import floor

class Entity(object):
    def __init__(self, x, y, max_x, max_y, color):
        self._x = floor(x)
        self._y = floor(y)
        self._max_x = max_x
        self._max_y = max_y
        self._color = color
        self.move_inbounds()
        self._additional_initialization() #Graphics etc. depend on type
        
    def __str__(self):
        return ""+str(type(self))+" "+str(self._x)+" "+str(self._y)+" "+str(self._color)

    def _additional_initialization(self):
        pass

    def _breeding_changes(self):
        pass

    def _mutate_copy(self):
        pass
    
    def tick(self):
        pass
    
    def can_breed(self):
        pass
    
    def move_inbounds(self, buffer=0):
        if (self._x < 0):
            self._x = buffer
        elif (self._x > self._max_x):
            self._x = floor(self._max_x)-buffer
        if (self._y < 0):
            self._y = buffer
        elif (self._y > self._max_y):
            self._y = floor(self._max_y)-buffer
    
    def breed(self):
        self._breeding_changes() #what happens to the entity on breeding depends on type
        return self._mutate_copy()