from PotentialFieldBrain import PotentialFieldBrain
from TowardsLight import TowardsLight
from ObstacleForce import ObstacleForce
from Wander import Wanderer
from SturdyBotHW3Starter import SturdyBot
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import sys

config = {SturdyBot.LEFT_MOTOR: OUTPUT_C, SturdyBot.RIGHT_MOTOR: OUTPUT_B, SturdyBot.MEDIUM_MOTOR: OUTPUT_A,
          SturdyBot.ULTRA_SENSOR: INPUT_2, SturdyBot.COLOR_SENSOR: INPUT_3, SturdyBot.LEFT_TOUCH: INPUT_4, SturdyBot.RIGHT_TOUCH: INPUT_1}
robot = SturdyBot("Maze Escaper", config)


def run():
    brain = PotentialFieldBrain(robot, 60)

    wander = Wanderer()
    escape = TowardsLight(robot)
    obstacleForce = ObstacleForce(robot)

    brain.add(wander)
    brain.add(escape)
    brain.add(obstacleForce)

    notOut = True
    while notOut:
        try:
            brain.step()
            if robot.readAmbient() >= 4:
                notOut = False
        except:
            brain.stopAll()
            sys.exit(0)
    brain.stopAll()


run()
