
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
    # This one takes in an angle and rotates the robot
    # in the direction of the angle, takes a reading from the
    # ultrasonic sensor and then rotates the robot back to its 
    # original heading

    def __init__(self, obj, angle):
        self.robot = obj
        self.angle = angle

    def run(self):
        rawData = 0
        steerHeading = ((self.angle / 180.0) * 100.0)

        if (self.angle > 0):
            self.robot.steerMove(15.0, steerHeading)
            rawData = self.robot.ultraSensor.distance_centimeters
            self.robot.steerMove(15.0, (-1 * steerHeading))
        elif (self.angle < 0):
            self.robot.steerMove(15.0, steerHeading)
            rawData = self.robot.ultraSensor.distance_centimeters
            self.robot.steerMove(15.0, (-1 * steerHeading))

        if(rawData > 500):
            rawData = 500
        if(rawData < 0):
            rawData = 0

        angle = 0

        if (self.angle < 0): angle = self.angle + 180
        elif (self.angle > 0): angle = self.angle - 180

        return (0, angle)
