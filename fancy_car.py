from base_car import Average_Car

class Fancy (Average_Car):
    # Changes direction of car. Can go in reverse drive_backwawrds()
    # Can only change gears if speed is zero
    # Speed of car going in reverse is still tracked as positive
    def __init__(self, name, max_speed_multiplier=1, acceleration_multiplier=1, break_efficiency_multiplier=1):
        self.forward_gear = True
        super().__init__(name, max_speed_multiplier, acceleration_multiplier, break_efficiency_multiplier)


    def drive(self, seconds):
        #continue moving in the same direction  (changes: distance_traveled and home_distance)
        #accept time value for how long to continue driving drive_forward(self, seconds)
        #No change in acceleration
        #average cars can only move forward
        if self.engine_state and self.forward_gear:
            self.distance_traveled += self.current_speed * seconds
            self.home_distance += self.current_speed * seconds
        if self.engine_state and not self.forward_gear:
            self.distance_traveled += self.current_speed * seconds
            self.home_distance -= self.current_speed * seconds


    def change_gear(self):
        if self.current_speed == 0:
            self.forward_gear = not self.forward_gear

    def honk(self):
        print("beep beep")

    def check_dash(self):
        # Shows car stats:
        # engine on/off
        # headlights on/off
        # current speed
        # odometer: distance traveled in trip
        # home: distance from home
        # current gear: park,drive, reverse
        if self.engine_state:
            print("Engine: ON")
        else:
            print("Engine: OFF")

        if self.headlights:
            print("Headlights: ON")
        else:
            print("Headlights: OFF")

        print(f"Current speed: {self.current_speed }")
        print(f"Distance Traveled: {self.distance_traveled}")
        print(f"Distance from Home: {self.home_distance}")

        if self.forward_gear:
            print("Current Gear: Dive")
        if not self.forward_gear:
            print("Current Gear: Reverse")
        if self.current_speed == 0:
            print("Current Gear: Park")

FancyCar = Fancy("FancyCar", 2, 1, 1)