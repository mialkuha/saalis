import numpy.random as rndm
from math import floor, pow
from entityHandler import *
from plant import *


class PlantHandler(EntityHandler):
    __max_hops = 10
    __personal_space = 100
    
    def __init__(self, g_width, g_height):
        super().__init__()
        self._grid_width = g_width
        self._grid_height = g_height
        self._grid = [[0 for j in range(self._grid_height)] for i in range(self._grid_width)]
    
    def _free_at(self, x, y):
        if x<0 or x>=self._grid_width or y<0 or y>=self._grid_height :
            return False
        if self._grid[x][y] > 0:
            return False
        cumulant = 0
        minx = max(x-self.__personal_space,0)
        maxx = min(x+self.__personal_space,self._grid_width)
        miny = max(y-self.__personal_space,0)
        maxy = min(y+self.__personal_space, self._grid_height)
        
        for i in range(minx,maxx):
            for j in range(miny,maxy):
                if ((i-x)*(i-x)+(j-y)*(j-y)<self.__personal_space*self.__personal_space):
                    cumulant += self._grid[i][j]
        return not cumulant
                          
    def add(self, plan):
        if not isinstance(plan, Plant):
            raise TypeError("PlantHandler handles only Plants")
        hops = 0
        (x, y) = plan.get_coords()
        while not self._free_at(x, y) and hops < self.__max_hops :
            (x, y) = plan.move()
            hops +=1
        if hops < self.__max_hops and self._free_at(x, y):
            self._grid[x][y] = 1
            self._entities.add(plan)      


    def add_random(self, max_x, max_y, amount=1):
        for i in range(amount) :
            new_plant = Plant(floor(max_x*rndm.uniform()),floor(max_y*rndm.uniform()), max_x, max_y, tuple(rndm.randint(low=0,high=255,size=3)))
            self.add(new_plant)

    def draw_all(self, win):
        for e in self._entities:
            e.draw(win)