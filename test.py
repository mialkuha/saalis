from saalis import *


world = World(1000,1000)
world.add_random(4)

for i in range(1000000000000) :
    world.tick()
