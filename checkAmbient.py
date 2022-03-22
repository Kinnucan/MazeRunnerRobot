from SturdyBotHW3Starter import SturdyBot
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import sys
import time

config = {SturdyBot.LEFT_MOTOR: OUTPUT_C, SturdyBot.RIGHT_MOTOR: OUTPUT_B, SturdyBot.MEDIUM_MOTOR: OUTPUT_A,
          SturdyBot.ULTRA_SENSOR: INPUT_2, SturdyBot.COLOR_SENSOR: INPUT_3}
robot = SturdyBot("Maze Escaper", config)
robot.calibrateWhite()


def run():
    iteration = 0
    while True:
        try:
            print('Iteration:', iteration,
                  '\t | Ambient Reading:', robot.readAmbient())
            iteration += 1
            time.sleep(1)
        except KeyboardInterrupt:
            robot.stop()
            sys.exit(0)


run()
