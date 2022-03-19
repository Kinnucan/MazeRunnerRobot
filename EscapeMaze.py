from PotentialFieldBrain import PotentialFieldBrain
from TowardsLight import TowardsLight
from ObstacleForce import  ObstacleForce
from Wander import Wanderer
from SturdyBotHW3Starter import SturdyBot
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4

config = {SturdyBot.LEFT_MOTOR: OUTPUT_C, SturdyBot.RIGHT_MOTOR: OUTPUT_B, SturdyBot.MEDIUM_MOTOR: OUTPUT_A,
          SturdyBot.ULTRA_SENSOR: INPUT_1}  # fill this in
robot = SturdyBot("Maze Escaper", config)

def run():
    brain = PotentialFieldBrain.PotentialFieldBrain(robot)

    wander = Wanderer()
    escape = TowardsLight(robot)
    obstacleForce_straight = ObstacleForce(robot, 0)
    obstacleForce_right = ObstacleForce(robot, 40)
    obstacleForce_left = ObstacleForce(robot, -40)

    brain.add(  wander  )
    brain.add(  escape  )
    brain.add(  obstacleForce_straight  )


    notOut = True
    while notOut:
        brain.step()
        if robot.readAmbient() == 100:
            notOut = False

    brain.stopAll()

run()
