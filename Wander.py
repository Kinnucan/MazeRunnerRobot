
import random


class Wanderer:

    def __init__(self):
        self.prevHead = 0
        self.directionChangeCount = 0
        self.leftTurnCount = 0
        self.rightTurnCount = 0

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

        # ************************************* #
        if ang/self.prevHead < 0:
            self.directionChangeCount += 1

        if ang < 0:
            self.leftTurnCount += 1
        elif ang > 0:
            self.rightTurnCount += 1
        # ************************************* #
        print('[Wanderer] Observation \t\t',
              None, '\t| Action Vector \t', actVec)
        # ************************************* #
        return actVec

    def summary(self):
        return {
            'DirectionChangeCount': self.directionChangeCount,
            'LeftTurnCount': self.leftTurnCount,
            'RightTurnCount': self.rightTurnCount,
        }
