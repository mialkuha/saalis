from saalis import *


world = World(700,700)
world.add_random(100)

for i in range(1000000) :
    world.tick()
