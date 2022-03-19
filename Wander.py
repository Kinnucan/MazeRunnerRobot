
import random

class Wanderer:

    def __init__(self):
        self.prevHead = 0
    def run(self):
        num = random.randint(self.prevHead - 20, (self.prevHead+20) )
        print(self.prevHead)
        self.prevHead = num
        return (30.0, num)