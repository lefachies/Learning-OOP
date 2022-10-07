import unittest
from base_car import Average_Car
from fancy_car import Fancy

FancyCar = Fancy("FancyCar", 2, 1, 1)
AverageCar = Average_Car("AverageCar", 1, 1, 1)


class TestBaseCar(unittest.TestCase):

    def test_engine_toggle(self):
        # This checks if the engine is toggled on if it's off
        # This checks if the engine is toggled off if it's on
        AverageCar.engine_state = False
        AverageCar.current_speed = 0
        AverageCar.engine_toggle()
        self.assertTrue(AverageCar.engine_state)

        AverageCar.engine_state = True
        AverageCar.current_speed = 0
        AverageCar.engine_toggle()
        self.assertFalse(AverageCar.engine_state)

        AverageCar.engine_state = True
        AverageCar.current_speed = 10
        AverageCar.engine_toggle()
        self.assertTrue(AverageCar.engine_state)


    def test_gas(self):
        # This only tests base cars
        # This tests that gas function adds the correct amount of speed to the car
        # Makes sure that the input value is being checked
        # Makes sure that it can only run if engine is on
        # Makes sure that distance is not being affected
        AverageCar.engine_state = True
        AverageCar.home_distance = 0
        AverageCar.distance_traveled = 0

        AverageCar.current_speed = 0
        AverageCar.gas(0)
        self.assertEqual(AverageCar.current_speed, 0)
        self.assertEqual(AverageCar.distance_traveled, 0)
        self.assertEqual(AverageCar.home_distance, 0)

        AverageCar.current_speed = 0
        AverageCar.gas(2)
        self.assertEqual(AverageCar.current_speed, 10)
        self.assertEqual(AverageCar.distance_traveled, 0)
        self.assertEqual(AverageCar.home_distance, 0)

        AverageCar.current_speed = 0
        AverageCar.gas(11)
        self.assertEqual(AverageCar.current_speed, 50)
        self.assertEqual(AverageCar.distance_traveled, 0)
        self.assertEqual(AverageCar.home_distance, 0)

        AverageCar.current_speed = 0
        self.assertRaises(AssertionError, AverageCar.gas, -1)
        self.assertEqual(AverageCar.distance_traveled, 0)
        self.assertEqual(AverageCar.home_distance, 0)

        AverageCar.current_speed = 10
        AverageCar.gas(0)
        self.assertEqual(AverageCar.current_speed, 10)
        self.assertEqual(AverageCar.distance_traveled, 0)
        self.assertEqual(AverageCar.home_distance, 0)

        AverageCar.current_speed = 10
        AverageCar.gas(2)
        self.assertEqual(AverageCar.current_speed, 20)
        self.assertEqual(AverageCar.distance_traveled, 0)
        self.assertEqual(AverageCar.home_distance, 0)

        AverageCar.current_speed = 20
        AverageCar.gas(11)
        self.assertEqual(AverageCar.current_speed, 50)
        self.assertEqual(AverageCar.distance_traveled, 0)
        self.assertEqual(AverageCar.home_distance, 0)

        AverageCar.current_speed = 10
        self.assertRaises(AssertionError, AverageCar.gas, -1)

        AverageCar.engine_state = False
        AverageCar.current_speed = 0
        AverageCar.gas(0)
        self.assertEqual(AverageCar.current_speed, 0)
        self.assertEqual(AverageCar.distance_traveled, 0)
        self.assertEqual(AverageCar.home_distance, 0)

        AverageCar.current_speed = 0
        AverageCar.gas(2)
        self.assertEqual(AverageCar.current_speed, 0)
        self.assertEqual(AverageCar.distance_traveled, 0)
        self.assertEqual(AverageCar.home_distance, 0)

        AverageCar.current_speed = 0
        AverageCar.gas(11)
        self.assertEqual(AverageCar.current_speed, 0)
        self.assertEqual(AverageCar.distance_traveled, 0)
        self.assertEqual(AverageCar.home_distance, 0)

    def test_drive(self):
        #This makes sure that the only thing that changes is the distance traveled and distance from home
        # Checks that the program is only accepting positive numbers for seconds
        # Checks taht there is no change in acceleration
        AverageCar.engine_state = True

        AverageCar.home_distance = 0
        AverageCar.distance_traveled = 0
        AverageCar.current_speed = 0
        AverageCar.drive(10)
        self.assertEqual(AverageCar.home_distance, 0)
        self.assertEqual(AverageCar.home_distance, 0)

        AverageCar.home_distance = 0
        AverageCar.distance_traveled = 0
        AverageCar.current_speed = 1
        AverageCar.drive(10)
        self.assertEqual(AverageCar.home_distance, 10)
        self.assertEqual(AverageCar.home_distance, 10)

        AverageCar.home_distance = 0
        AverageCar.distance_traveled = 0
        AverageCar.current_speed = 1
        self.assertRaises(AssertionError, AverageCar.drive, -1)

        AverageCar.engine_state = False

        AverageCar.home_distance = 0
        AverageCar.distance_traveled = 0
        AverageCar.current_speed = 0
        AverageCar.drive(10)
        self.assertEqual(AverageCar.home_distance, 0)
        self.assertEqual(AverageCar.home_distance, 0)

        AverageCar.home_distance = 0
        AverageCar.distance_traveled = 0
        AverageCar.current_speed = 1
        AverageCar.drive(10)
        self.assertEqual(AverageCar.home_distance, 0)
        self.assertEqual(AverageCar.home_distance, 0)

    def test_headlights(self):
        # checks that headlights can be toggled on if off and vise - versa
        AverageCar.headlights = True
        AverageCar.headlights_toggle()
        self.assertFalse(AverageCar.headlights)

        AverageCar.headlights = False
        AverageCar.headlights_toggle()
        self.assertTrue(AverageCar.headlights)

    def test_fancy_drive(self):
        # This test that gear can only be changed while parked
        # This test that the distance traveled is postive even when gear is reverse
        # This test that home distance is subtracted when we are travling in revese
        FancyCar.engine_state = True

        FancyCar.home_distance = 0
        FancyCar.distance_traveled = 0
        FancyCar.current_speed = 0
        FancyCar.drive(10)
        self.assertEqual(FancyCar.home_distance, 0)
        self.assertEqual(FancyCar.home_distance, 0)

        FancyCar.home_distance = 0
        FancyCar.distance_traveled = 0
        FancyCar.current_speed = 1
        FancyCar.drive(10)
        self.assertEqual(FancyCar.home_distance, 10)
        self.assertEqual(FancyCar.home_distance, 10)

        FancyCar.home_distance = 0
        FancyCar.distance_traveled = 0
        FancyCar.current_speed = 0
        FancyCar.forward_gear = True
        FancyCar.change_gear()
        FancyCar.current_speed = 1
        FancyCar.drive(10)
        self.assertEqual(FancyCar.home_distance, -10)
        self.assertEqual(FancyCar.home_distance, -10)

        FancyCar.home_distance = 0
        FancyCar.distance_traveled = 0
        FancyCar.current_speed = 0
        FancyCar.forward_gear = False
        FancyCar.change_gear()
        FancyCar.current_speed = 1

        FancyCar.drive(10)
        self.assertEqual(FancyCar.home_distance, 10)
        self.assertEqual(FancyCar.home_distance, 10)

        FancyCar.forward_gear = True
        FancyCar.home_distance = 0
        FancyCar.distance_traveled = 0
        FancyCar.current_speed = 1
        FancyCar.change_gear()
        FancyCar.drive(10)
        self.assertEqual(FancyCar.home_distance, 10)
        self.assertEqual(FancyCar.home_distance, 10)


    def test_breaking(self):
        # Makes sure that the input to the break funciton is always >= 0
        # makes sure that the function only works if the enigne is on
        # makes sure that the car comes to a complete stop when told to
        self.assertRaises(AssertionError, AverageCar.breaking, False, -1)
        AverageCar.break_efficiency = -5
        AverageCar.engine_state = True
        AverageCar.current_speed = 50
        AverageCar.breaking(False, 2)
        self.assertEqual(40, AverageCar.current_speed)

        AverageCar.break_efficiency = -5
        AverageCar.engine_state = False
        AverageCar.current_speed = 50
        AverageCar.breaking(False, 3)
        self.assertEqual(50, AverageCar.current_speed)

        AverageCar.break_efficiency = -5
        AverageCar.engine_state = True
        AverageCar.current_speed = 50
        AverageCar.breaking(True)
        self.assertEqual(0, AverageCar.current_speed)

if __name__ == '__main__':
    unittest.main()
