from saalis import *


world = World(700,700)
world.add_random(3)

for i in range(1000000000000) :
    world.tick()
