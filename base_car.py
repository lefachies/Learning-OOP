class Average_Car:
    def __init__(self, name, max_speed_multiplier=1, acceleration_multiplier=1, break_efficiency_multiplier=1):

        self.name = name
        self.max_speed = 50.0 * max_speed_multiplier
        self.acceleration = 5.0 * acceleration_multiplier
        self.break_efficiency = -10.0 * break_efficiency_multiplier
        self.engine_state = False
        self.current_speed = 0.0
        self.home_distance = 0.0
        self.distance_traveled = 0
        self.headlights = False

    def engine_toggle(self):
        # Turns on engine and now we can use: gas(), drive(),breaking()
        # Establishes a home point (sets: home_distance = 0)

        # Turns off engine an now we can't use: gas(), drive(), breaking()
        # This can only turn off if we are not moving (current_speed == 0)
        if not self.engine_state:
            self.engine_state = True
            self.home_distance = 0.0
        elif self.engine_state and self.current_speed == 0:
            self.engine_state = False



    def gas(self, seconds):
        # accelerates the car (changes: current_speed)
        # accelerates depending on how long the gas pedal is pressed(in seconds)
        # accept seconds as an input to know how long to keep it pressed for.
        #does not affect distance, only speed.
        assert seconds >= 0, f'seconds must be a positive value. Not {seconds}'
        if self.engine_state and self.current_speed < self.max_speed:
            # Only accelerate if the current speed is less than the max speed
            self.current_speed = self.current_speed + self.acceleration * seconds
            if self.current_speed > self.max_speed:
                self.current_speed = self.max_speed

    def drive(self, seconds):
        #continue moving in the same direction  (changes: distance_traveled and home_distance)
        #accept time value for how long to continue driving drive_forward(self, seconds)
        #No change in acceleration
        #average cars can only move forward
        assert seconds >= 0, f'seconds must be a positive value. Not {seconds}'
        if self.engine_state:
            self.distance_traveled += self.current_speed * seconds
            self.home_distance += self.current_speed * seconds

    def breaking(self, full_stop, seconds=0):
        # slows down the vehicle
        # should accept a time value for how long the pedal should be pressed.
        # should only affect speed not distance

        # Only break if the current speed is not zero
        assert seconds >= 0, f'seconds must be a positive value. Not {seconds}'
        if not full_stop:
            if self.current_speed > 0 and self.engine_state:
                self.current_speed = self.current_speed + self.break_efficiency * seconds
                if self.current_speed < 0:
                    self.current_speed = 0
        else:
            self.current_speed = 0

    def headlights_toggle(self):
        # Toggles on / off the headlighs
        self.headlights = not self.headlights


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

        if self.current_speed > 0:
            print("Current Gear: Dive")
        if self.current_speed == 0:
            print("Current Gear: Park")








