
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

class ObstacleForceV2:
    # Alternate version of the above ObstacleForce class
    # This one takes in an angle and rotates the medium motor
    # in that direction, takes a reading from the ultrasonic sensor
    # (presumably mounted on the medium motor) and then rotates
    # the motor back to its original angle
    
    def __init__(self, obj, angle):
        self.robot = obj
        self.angle = angle

    def run(self):
        self.robot.pointerTurnBy(self.angle, 15.0)
        rawData = self.robot.ultraSensor.distance_centimeters
        self.robot.pointerTurnBy((-1 * self.angle), 15.0)

        if(rawData > 500):
            rawData = 500
        if(rawData < 0):
            rawData = 0

        angle = 0

        if (self.angle < 0): angle = self.angle + 180
        elif (self.angle > 0): angle = self.angle - 180

        return (0, angle)
