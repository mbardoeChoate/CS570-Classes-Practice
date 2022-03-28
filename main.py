# you will need to import the robot and motor classes
from robot import Robot
from motor import Motor

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_robot=Robot(1,2) # robot with one motor and wheel radius of 2
    my_motor=Motor("??",15)
    my_robot.add_motor(my_motor)
    # set the voltage on the motor to 1

    print(my_robot.run())
    # this should spit out how fast the robot should be going
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
