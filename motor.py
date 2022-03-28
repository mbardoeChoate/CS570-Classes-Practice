

class Motor:

    def __init__(self, name, max_revolutions, direction=1):
        self.name=name
        self.max_revolutions=max_revolutions
        self.direction=direction
        self.voltage=0

    def set_voltage(self,voltage):
        self.voltage=max(-1,min(1,voltage))

    def get_speed(self):
        return self.voltage*self.max_revolutions*self.direction

    def reverse_direction(self):
        self.direction=-self.direction


if __name__=="__main__":
    alan=Motor("Alan", 12.5)
    alan.set_voltage(.5)
    print(alan.get_speed())