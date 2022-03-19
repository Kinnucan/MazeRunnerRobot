
class TowardsLight:
    def __init__(self, obj):
        self.robot = obj
        self.prevLight = 0
    def run(self):
        rawData_ambLight = self.robot.readAmbient()

        if rawData_ambLight >= 100:
            return 0, 0

        if rawData_ambLight > 30:
            mag = 20

        if 10 >= rawData_ambLight >= 30:
            mag = 10
        if rawData_ambLight < 10:
            mag = 0
        return mag, 0
