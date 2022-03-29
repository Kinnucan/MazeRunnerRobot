import random

class TowardsColor:

    def __init__(self, obj):
        self.robot = obj
        self.prevHead = 0
        self.targetColor = 1
        self.targetFound = False

    def run(self):
        if (self.targetFound):
            return 100.0, 0.0
        else:
            currentColor = self.robot.readColor()
            print("Color:")
            print(currentColor)
            if currentColor == self.targetColor:
                self.targetFound = True
                return 100.0, 0.0
            else:
                num = random.randint(self.prevHead - 20, self.prevHead + 20)
                self.prevHead = num
                return 10.0, 0.0
