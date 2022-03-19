
class ObstacleForce:
    def __init__(self, obj):
        self.robot = obj
    def run(self):

        rawData = self.robot.ultraSensor.distance_centimeters

        if rawData > 100:
            rawData = 100
        if rawData < 0:
            rawData = 0

        if rawData < 30:
            angle = -180
        elif rawData > 30:
            angle = 0
        return 0, angle
