import random


class ObstacleForce:
    def __init__(self, obj):
        self.robot = obj

    def run(self):

        # rawData = self.robot.ultraSensor.distance_centimeters

        # if rawData > 100:
        #     rawData = 100
        # if rawData < 0:
        #     rawData = 0

        # if rawData < 5:
        #     angle = -180
        # elif rawData > 5:
        #     angle = 0
        # print("Distance to an Obstacle: ", rawData, "\n")
        # return 0, angle
        return self.behaveDescrete()

    def behaveDescrete(self):
        scale = 1
        dist = self.robot.ultraSensor.distance_centimeters
        mag_ang_map = {
            (0, 20): (40, 180),
            (20, 30): (20, 80),
            (30, 50): (10, 40),
            (50, 80): (0, 0),
        }

        for range, mag_ang in mag_ang_map.items():
            if range[0] <= dist < range[1]:
                return mag_ang[0] * scale, mag_ang[1] * random.choice([-1, 1])


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
            self.robot.steerMove(100.0, steerHeading)
            rawData = self.robot.ultraSensor.distance_centimeters
            self.robot.steerMove(100.0, (-1 * steerHeading))
        elif (self.angle < 0):
            self.robot.steerMove(100.0, steerHeading)
            rawData = self.robot.ultraSensor.distance_centimeters
            self.robot.steerMove(100.0, (-1 * steerHeading))

        if(rawData > 500):
            rawData = 500
        if(rawData < 0):
            rawData = 0

        angle = 0

        if (self.angle < 0):
            angle = self.angle + 180
        elif (self.angle > 0):
            angle = self.angle - 180

        return (0, angle)
