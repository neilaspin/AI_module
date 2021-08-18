"""Braitenberg-based obstacle-avoiding robot controller."""

from controller import Robot
from controller import Compass

# Get reference to the robot.
robot = Robot()

# Get simulation step length.
timeStep = int(robot.getBasicTimeStep())

# Constants of the Thymio II motors and distance sensors.
maxMotorVelocity = 9.53
distanceSensorCalibrationConstant = 360

# Get left and right wheel motors.
leftMotor = robot.getMotor("motor.left")
rightMotor = robot.getMotor("motor.right")

# get robot's Compass device
compass = robot.getCompass("compass")

# enable the Compass
compass.enable(timeStep)

# Get frontal distance sensors.
outerLeftSensor = robot.getDistanceSensor("prox.horizontal.0")
centralLeftSensor = robot.getDistanceSensor("prox.horizontal.1")
centralSensor = robot.getDistanceSensor("prox.horizontal.2")
centralRightSensor = robot.getDistanceSensor("prox.horizontal.3")
outerRightSensor = robot.getDistanceSensor("prox.horizontal.4")

# Enable distance sensors.
outerLeftSensor.enable(timeStep)
centralLeftSensor.enable(timeStep)
centralSensor.enable(timeStep)
centralRightSensor.enable(timeStep)
outerRightSensor.enable(timeStep)

# Disable motor PID control mode.
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

# Set ideal motor velocity.
initialVelocity = maxMotorVelocity

# Set the initial velocity of the left and right wheel motors.
leftMotor.setVelocity(initialVelocity)
rightMotor.setVelocity(initialVelocity)

while robot.step(timeStep) != -1:

    # Read values from four distance sensors and calibrate.
    outerLeftSensorValue = outerLeftSensor.getValue() / distanceSensorCalibrationConstant
    centralLeftSensorValue = centralLeftSensor.getValue() / distanceSensorCalibrationConstant
    centralSensorValue = centralSensor.getValue() / distanceSensorCalibrationConstant
    centralRightSensorValue = centralRightSensor.getValue() / distanceSensorCalibrationConstant
    outerRightSensorValue = outerRightSensor.getValue() / distanceSensorCalibrationConstant

    # current Compass measurement.
    # The returned vector indicates the north direction in the coordinate system of the Compass device
    # Desired compass values: [x,y,z] : [0,1,2] : x for north, z for left and right
    compassValues = compass.getValues()
    print
    "compass:" + str(compassValues)

    # Set wheel velocities based on sensor values
    # Will turns right if the central sensor is triggered.
    leftMotor.setVelocity(initialVelocity - (centralRightSensorValue + outerRightSensorValue) / 1)
    rightMotor.setVelocity(initialVelocity - (centralLeftSensorValue + outerLeftSensorValue) / 1 - centralSensorValue)

    if centralRightSensorValue == 0 and outerRightSensorValue == 0:
        if centralLeftSensorValue == 0 and outerLeftSensorValue == 0:
            # If no obstacle stands in our way --> y =  0.009330825235785215
            # if there is an obstacle the way
            # and the obstacle is on the left, turn right
            if compassValues[1] < 0.0093 and compassValues[0] < -0.1:
                leftMotor.setVelocity(8.53)
                rightMotor.setVelocity(initialVelocity)
                # print "turn right"
            # if there is an obstacle on the right, turn left
            if compassValues[1] < 0.0093 and compassValues[0] > 0.1:
                leftMotor.setVelocity(initialVelocity)
                rightMotor.setVelocity(8.53)
                # print "turn left"

