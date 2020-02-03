class Entity(object):
    def __init__(self, x, y, max_x, max_y, color):
        self._x = x
        self._y = y
        self._max_x = max_x
        self._max_y = max_y
        self._color = color
        self._additional_initialization() #Graphics etc. depend on type
        
    def __str__(self):
        return ""+type(self)+" "+self._x+" "+self._y+" "+self._color

    def _additional_initialization(self):
        pass
    
    def tick(self):
        pass