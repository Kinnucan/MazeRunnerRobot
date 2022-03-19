# A Potential Field control system

# import SturdyBot
import math
import time

#-------------------------------------------
# 

class PotentialFieldBrain:
    """ This class represents a brain for a potential field reactive system.
    This continues to use the concept of a behavior, but potential field
    behaviors each produce a vector describing the force they compute on the
    robot. The brain does vector addition to combine those vectors, and then
    transforms the resulting force on the robot into a movement direction and
    speed"""


    #----------------------------------------
    #Initialization and destruction routines
    
    def __init__(self, robot, maxMagnitude = 100.0):
        """Initializes the brain with the robot it controls. Also takes
        an optional input to define the maximum magnitude of any vector."""

        self.robot = robot
        # set maximum possible magnitude
        self.maxMagnitude = maxMagnitude
        self.behaviors = []


    def add(self, behavior):
        """Takes a behavior object as input, and initializes it, and
        adds it to the list"""
        self.behaviors.append( behavior )


    def run(self, numSteps):
        """Takes in a number of steps, and runs the that many cycles"""
        for i in range(numSteps):
            self.step()
        self.robot.stop()

    def stopAll(self):
        """Stops the robot from moving, and could shut down anything else that was required"""
        self.robot.stop()

    # 
    def step(self):
        """One step means figuring out the vectors for each of the behaviors, and performing
        vector addition to combine them.  Then the resulting vector is the action taken."""
        vectors = self._updateBehaviors()
        (magnitude, angle) = self._vectorAdd(vectors)
        print("Original:", magnitude, angle)

        vectorMag = self._scaleMagnitude(magnitude)

        steerHeading = (angle / 180.0) * 100.0

        print("Scaled:", vectorMag, steerHeading)


        if abs(angle) <= 90:
            # If the angle is forward-looking, then use steerHeading and go forward
            print("Forward...")
            self.robot.steerMove(vectorMag, steerHeading)
        else:
            # If the angle is backward-looking, then move backward briefly, then
            # turn in place toward the angle
            print("Backward...")
            self.robot.backward(vectorMag, 0.5)
            self.robot.turnRight(steerHeading * 0.8)  # scale back speed a bit

        time.sleep(0.5)
        

    def _scaleMagnitude(self, magnitude):
        """Takes in a magnitude and scales it as a percentage of
        the maximum magnitude, so that it is between 0.0 and 1.0."""
        if magnitude > self.maxMagnitude:
            magnitude = self.maxMagnitude
        return magnitude


    def _scaleRotation(self, rotSpeed):
        """Takes in a rotation speed and scales it so that
        it is further from  zero than 0.2."""
        if rotSpeed > 0:
            # if scaled speed is too low, set to 0.2
            rotSpeed = max(20.0, rotSpeed)
        elif rotSpeed < 0:
          # if scaled speed is too low, set to 0.2
            rotSpeed = min(-20.0, rotSpeed)
        return rotSpeed
    
    def _updateBehaviors(self):
        """Run through all behaviors, and ask them to calculate the force
        they detect. Return the forces as a list. Note: forces are given as a
        tuple containing magnitude and direction"""
        vectors = []
        for behav in self.behaviors:
            vec = behav.run()
            vectors.append(vec)
        return vectors


    def _vectorAdd(self, vectors):
        """takes in a list of vectors and produces the final vector.  Notice
        that, for simplicity, the behaviors return a magnitude/angle description
        of a vector, but that having the vector described as an x and y offset is
        much easier, so first the values are converted ,and then added."""
        xSum = 0
        ySum = 0
        for vec in vectors:
            (mag, angle) = vec
            radAngle = math.radians(angle)
            xVal = math.cos(radAngle) * mag
            yVal = math.sin(radAngle) * mag
            xSum += xVal
            ySum += yVal
        totalMag = math.hypot(xSum, ySum)
        totalAngle = math.atan2(ySum, xSum)
        degAngle = math.degrees(totalAngle)
        # Convert angles to the range from -180 to +180
        while degAngle < -180:
            degAngle += 360
        while degAngle > 180:
            degAngle -= 360
        return (totalMag, degAngle)




if __name__ == '__main__':
    pBrain = PotentialFieldBrain('r')
    vects = [[25, 135], [35, -135]]
    mag, ang = pBrain._vectorAdd(vects)
    print(mag, ang)

