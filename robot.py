# Put the robot code here
from motor import Motor
import math

class Robot:

    def __init__(self, num_motors, wheel_radius):
        self.num_motors=num_motors
        self.motors=[None]*self.num_motors
        self.wheel_radius=wheel_radius

    def add_motor(self,position,motor):
        self.motors[position]=motor

    def run(self):
        return math.pi*

if __name__=="__main__":
    robbie=Robot(2,2)
    alan=Motor("Alan", 15)
    matilda=Motor("Matilda",15)
    robbie.add_motor(0, alan)
    robbie.add_motor(1, matilda)