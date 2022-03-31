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
    brain = PotentialFieldBrain.PotentialFieldBrain(robot)

    towardsColor = TowardsColor(robot)
    obstacleForce_straight = ObstacleForceV2(robot, 0)
    # obstacleForce_right_angle = ObstacleForceV2(robot, 45)
    # obstacleForce_right = ObstacleForceV2(robot, 90)
    # obstacleForce_left_angle = ObstacleForceV2(robot, -45)
    # obstacleForce_left = ObstacleForceV2(robot, -90)

    brain.add( towardsColor )
    brain.add( obstacleForce_straight )
    # brain.add( obstacleForce_right_angle )
    # brain.add( obstacleForce_right )
    # brain.add( obstacleForce_left )
    # brain.add( obstacleForce_left_angle )

    colorNotFound = True
    while colorNotFound:
        try:
            brain.step()
            if (robot.readColor == 1 and robot.readDistance <= 10):
                colorNotFound = False
        except KeyboardInterrupt:
            brain.stopAll()
            sys.exit(0)
    brain.stopAll()

run()
