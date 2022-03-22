
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

    def behaveContinous(self):
        rawData_ambLight = self.robot.readAmbient()
        scale = 1
        return int(rawData_ambLight * scale), 0

    def behaveDescrete(self):
        rawData_ambLight = self.robot.readAmbient()
        scale = 1
        map = {
            (0, 10): 0,
            (10, 30): 10,
            (30, 100): 20,
        }
        for range, mag in map.items():
            if range[1] > rawData_ambLight >= range[0]:
                return mag * scale, 0
