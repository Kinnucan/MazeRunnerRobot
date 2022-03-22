
class TowardsLight:
    def __init__(self, obj):
        self.robot = obj
        self.prevLight = 0

    def run(self):
        rawData_ambLight = self.robot.readAmbient()

        if rawData_ambLight >= 3:     #Outside the box
            return 0, 0

        if rawData_ambLight >= 2:
            mag = 20

        if 1 >= rawData_ambLight >= 2:
            mag = 10
        if rawData_ambLight == 0:    #Too dark, doesn't know where light source is
            mag = 0
        print("Ambient Light Value: ", rawData_ambLight, "\n")
        return mag, 0

    # def behaveDescrete(self):
    #     rawData_ambLight = self.robot.readAmbient()
    #     scale = 1
    #     map = {
    #         (0, 10): 0,
    #         (10, 30): 10,
    #         (30, 100): 20,
    #     }
    #     for range, mag in map.items():
    #         if range[1] > rawData_ambLight >= range[0]:
    #             return mag * scale, 0
