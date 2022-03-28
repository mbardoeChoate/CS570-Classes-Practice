# CS570 Python Classes practice

Based on what we did in class, Complete the class called ```robot.py```. In this file, make a class called ```Robot```. 
The robot class needs to have the following fields:

* ```motors``` = a list to add motors to
* ```max_speed``` = number for the maximum speed
* ```wheel_radius``` = the wheel radius of the drive wheels

The robot class will have the following methods

*```run()``` - a function that calculates and returns the velocity of the robot as a tuple (left velocity, right velocity.

The ```Robot``` class will interact with the Motor class to help determine the velocity of the robot for different motor
settings. 

If the motors are set with a maximum revolutions of 15 per second, 
and the motors are running at full strength, and the wheel radius is 2 inches, then the result or run should be
(188.495559215, 188.495559215). 


