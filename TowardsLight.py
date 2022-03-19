
class TowardsLight:
    def __init__(self, obj):
        self.robot = obj
        self.prevLight = 0
    def run(self):
        rawData_ambLight = self.robot.readAmbient()

        if rawData_ambLight >= 100:
            return 0, 0

        ambLight = rawData_ambLight

        if ambLight > self.prevLight:
            return 10, 0
        if ambLight < self.prevLight:
            return 10, 180

        self.prevLight = ambLight
        return 20, 0
