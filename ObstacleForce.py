import random
import time

class ObstacleForce:
    def __init__(self, obj):
        self.robot = obj
        self.touchCount = 0
        self.closeCallCount = 0

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
        touch = self.robot.readTouch()

        actVec = (0, 0)
        dist = self.robot.ultraSensor.distance_centimeters

        if touch in [(False, False), (None, None)]:
            mag_ang_map = {
                (0, 20): (50, 120),
                (20, 30): (20, 80),
                (30, 50): (10, 40),
                (50, 200): (0, 0),
            }

            for range, mag_ang in mag_ang_map.items():
                if range[0] <= dist < range[1]:
                    actVec = (mag_ang[0] * scale, mag_ang[1]
                              * random.choice([-1, 1]))
                    break
        elif touch == (True, False):
            actVec = (40, 85)
        elif touch == (False, True):
            actVec = (40, -85)
        elif touch == (True, True):
            actVec = (60, 120)
        # ************************************* #
        if touch[0] or touch[1]:
            self.touchCount += 1
        if dist < 20:
            self.closeCallCount += 1
        # ************************************* #
        print('[ObstacleForce] Observation - Touch\t',
              touch, '\t| Action Vector \t', actVec)
        print('[ObstacleForce] Observation - Dist\t',
              dist, '\t| Action Vector \t', actVec)
        # ************************************* #
        return actVec

    def summary(self):
        return {
            'TouchCount': self.touchCount,
            'CloseCallCount': self.closeCallCount,
        }


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
        runTime = ((abs(self.angle) / 180.0) * 1.0)

        if (self.angle > 0):
            self.robot.turnRight(30, runTime)
            rawData = self.robot.ultraSensor.distance_centimeters
            self.robot.turnLeft(30, runTime)
        elif (self.angle < 0):
            self.robot.turnLeft(30, runTime)
            rawData = self.robot.ultraSensor.distance_centimeters
            self.robot.turnRight(30, runTime)
        print("Sensor Reading:")
        print(rawData)

        # if (rawData > 500):
        #     rawData = 500
        # if (rawData < 0):
        #     rawData = 0
        # print("Modified rawData:")
        # print(rawData)

        if (rawData != 0):
            pass

        new_angle = 0

        if (self.angle < 0):
            new_angle = self.angle + 180
        elif (self.angle > 0):
            new_angle = self.angle - 180
        print(new_angle)

        return (rawData, new_angle)
