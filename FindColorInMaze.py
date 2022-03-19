from PotentialFieldBrain import PotentialFieldBrain
from TowardsColor import TowardsColor
from ObstacleForce import  ObstacleForce
from SturdyBotHW3Starter import SturdyBot
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4

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
    obstacleForce_straight = ObstacleForce(robot, 0)
    obstacleForce_right = ObstacleForce(robot, 40)
    obstacleForce_left = ObstacleForce(robot, -40)

    brain.add( towardsColor )
    brain.add( obstacleForce_straight )
    brain.add( obstacleForce_right )
    brain.add( obstacleForce_left )


    colorNotFound = True
    while colorNotFound:
        brain.step()
        if (robot.readColor == 0 and robot.ultraSensor <= 10):
            colorNotFound = False
    brain.stopAll()

run()
