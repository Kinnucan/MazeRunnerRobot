
import random

class Wanderer:

    def __init__(self, obj):
        self.robot = obj
        self.prevHead = 0
    def run(self):
        rawData = self.robot.readAmbient()

        num = 0
        if 0 <= rawData <= 30:
            num = random.randint(self.prevHead - 20, (self.prevHead + 20))
        if 30 <= rawData <= 60:
            num = random.randint(self.prevHead - 10, (self.prevHead + 10))

        print(self.prevHead)
        self.prevHead = num
        return 5, num