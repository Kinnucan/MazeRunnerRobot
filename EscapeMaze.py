from PotentialFieldBrain import PotentialFieldBrain
from TowardsLight import TowardsLight
from ObstacleForce import ObstacleForce
from Wander import Wanderer
from SturdyBotHW3Starter import SturdyBot
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import sys
import traceback
import time

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

    countOutside = 0

    lightThreshold = 9

    startTime = time.time()
    endTime = 0

    while notOut:
        try:
            brain.step()
            if robot.readAmbient() >= lightThreshold:
                countOutside += 1
                if countOutside > 3:
                    print('OH NOOOOOO!!! TOOO BRIGJHT!!!!')
                    notOut = False
                    endTime = time.time()
            else:
                countOutside = 0
        except:
            print(traceback.format_exc())
            brain.stopAll()
            sys.exit(0)

    brain.stopAll()

    print('*'*40, '[Summary]', '*'*40)
    print('Time to exit: \t', endTime-startTime)
    wanderSum = wander.summary()
    escapeSum = escape.summary()
    obstacleSum = obstacleForce.summary()
    print('Wander Summary: \t', wanderSum)
    print('Escape Summary: \t', escapeSum)
    print('Obstacle Summary: \t', obstacleSum)
    print('*'*40, '*********', '*'*40)


run()
