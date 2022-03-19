
import random

class Wanderer:

    def __init__(self, obj):
        self.robot = obj
        self.prevHead = 0
    def run(self):
        rawData = self.robot.readAmbient()

        turnRange = 0
        if 0 <= rawData <= 30:
            turnRange = 20

        if 30 <= rawData <= 60:
            turnRange = 10

        num = random.randint(self.prevHead - turnRange, (self.prevHead+turnRange) )
        print(self.prevHead)
        self.prevHead = num
        return 10, num