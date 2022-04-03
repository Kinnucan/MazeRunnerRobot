
class TowardsLight:
    def __init__(self, obj):
        self.robot = obj
        self.intensityFreq = {}

    def run(self):
        # rawData_ambLight = self.robot.readAmbient()

        # if rawData_ambLight >= 3:  # Outside the box
        #     return 0, 0

        # if rawData_ambLight >= 2:
        #     mag = 20

        # if 1 >= rawData_ambLight >= 2:
        #     mag = 10
        # if rawData_ambLight == 0:  # Too dark, doesn't know where light source is
        #     mag = 0
        # print("Ambient Light Value: ", rawData_ambLight, "\n")
        # return mag, 0
        return self.behaveDescrete()

    def behaveDescrete(self):
        rawData_ambLight = self.robot.readAmbient()
        scale = 1
        mag_map = {
            (0, 1): 0,
            (1, 2): 30,
            (2, 4): 40,
        }

        actVec = (0, 0)
        for range, mag in mag_map.items():
            if range[0] <= rawData_ambLight < range[1]:
                actVec = (mag * scale, 0)
                break

        # ************************************* #
        self.intensityFreq[rawData_ambLight] = self.intensityFreq.get(
            rawData_ambLight, 0) + 1
        # ************************************* #
        print('[TowardsLight] Observation \t\t',
              rawData_ambLight, '\t| Action Vector \t', actVec)
        # ************************************* #

        return actVec

    def summary(self):
        return{
            'IntensityFreq': self.intensityFreq
        }
