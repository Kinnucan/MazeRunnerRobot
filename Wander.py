
import random


class Wanderer:

    def __init__(self, obj):
        self.robot = obj
        self.prevHead = 0

    def run(self):
        # print("Previous heading: ", self.prevHead, "\n")

        # num = random.randint(self.prevHead - 10, (self.prevHead + 10))
        # print("Current Heading: ", num, "\n")

        # self.prevHead = num

        # return 5, num
        return self.behaveDescrete()

    def behaveDescrete(self):
        scale = 1
        mag = 20
        ang = ((self.prevHead + random.randint(-30,  30)) %
               90) * [1, -1][self.prevHead < 0]
        self.prevHead = ang
        actVec = (mag * scale, ang)
        print('[TowardsLight] Observation \t',
              None, ' | Action Vector \t', actVec)
        return actVec
