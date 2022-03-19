
class ObstacleForce:
    def __init__(self, obj, angle):
        self.robot = obj
        self.angle = angle
    def run(self):
        self.robot.pointerTurnTo(self.angle)
        rawData = self.robot.ultraSensor.distance_centimeters
        self.robot.pointerTurnTo(0)

        if rawData > 100:
            rawData = 100
        if rawData < 0:
            rawData = 0

        angle = 0
        if self.angle < 0:
            angle = self.angle + 180
        elif self.angle > 0:
            angle = self.angle - 180
        return 0, angle