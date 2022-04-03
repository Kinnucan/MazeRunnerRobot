from PotentialFieldBrain import PotentialFieldBrain
from TowardsColor import TowardsColor
from ObstacleForce import ObstacleForceV2
from SturdyBotHW3Starter import SturdyBot
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import sys
import time

config = {  
            SturdyBot.LEFT_MOTOR: OUTPUT_C,
            SturdyBot.RIGHT_MOTOR: OUTPUT_B,
            SturdyBot.MEDIUM_MOTOR: OUTPUT_A,
            SturdyBot.RIGHT_TOUCH: INPUT_1,
            SturdyBot.ULTRA_SENSOR: INPUT_2,
            SturdyBot.COLOR_SENSOR: INPUT_3,
            SturdyBot.LEFT_TOUCH: INPUT_4
        }
robot = SturdyBot("Maze Escaper", config)

def run():
    colorNotFound = True

    while colorNotFound:
        try:
            robot.forward(20.0, 1.0)

            forwardDistance = robot.readDistance()
            print(forwardDistance)

            if (forwardDistance <= 10):
                while (robot.readDistance() > 2):
                    robot.forward(5.0, 0.25)

                color = robot.readColor()
                if (color == 5):
                    print(color)
                    colorNotFound = False
                    break
                else:
                    robot.backward(20.0, 1.0)

                    robot.turnRight(38, (90.0 / 180.0))
                    rightDistance = robot.readDistance()
                    print(rightDistance)

                    robot.turnLeft(38, (180.0 / 180.0))
                    leftDistance = robot.readDistance()
                    print(leftDistance)

                    if (rightDistance > leftDistance):
                        robot.turnRight(38, (180.0 / 180.0))
            elif (color == 5):
                print(color)
                colorNotFound = False
        except KeyboardInterrupt:
            print("Robot Stopped")
            sys.exit(0)
    print("Color Found!")

run()
