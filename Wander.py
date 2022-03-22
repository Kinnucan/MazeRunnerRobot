
import random

class Wanderer:

    def __init__(self, obj):
        self.robot = obj
        self.prevHead = 0
    def run(self):
        print("Previous heading: ", self.prevHead, "\n")

        num = random.randint(self.prevHead - 10, (self.prevHead + 10))
        print("Current Heading: ", num, "\n")

        self.prevHead = num

        return 5, num