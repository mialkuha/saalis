class Entity(object):
    def __init__(self, x, y, max_x, max_y, color):
        self._x = x
        self._y = y
        self._max_x = max_x
        self._max_y = max_y
        self._color = color
        self.move_inbounds()
        self._additional_initialization() #Graphics etc. depend on type
        
    def __str__(self):
        return ""+type(self)+" "+self._x+" "+self._y+" "+self._color

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
    
    def move_inbounds(self):
        if (self._x < 0):
            self._x = 0
        elif (self._x > self._max_x):
            self._x = self._max_x
        if (self._y < 0):
            self._y = 0
        elif (self._y > self._max_y):
            self._y = self._max_y
    
    def breed(self):
        self._breeding_changes() #what happens to the entity on breeding depends on type
        return self._mutate_copy()