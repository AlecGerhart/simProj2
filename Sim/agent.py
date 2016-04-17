import rngs
import rvgs
import random

class Agent:

    currId = 0

    def __init__(self):
        self.agentId = random.random()
        self.alive = True
        self.age = 0
        self.puberty = rvgs.uniform(12,15)
        self.sex = rvgs.bernoulli(0.5)
        self.lifespan = rvgs.uniform(60,100)
        self.fov = rvgs.equilikely(1,6)
        self.met = rvgs.uniform(1,4)
        self.fert = 0
        self.lastTime = 0

        if self.sex == 1:
            self.fert = rvgs.uniform(40,50)
        else:
            self.fert = rvgs.uniform(50,60)
