from fancy_car import FancyCar
from fast_car import FastCar
from slow_car import SlowCar

cars = [FancyCar, FastCar, SlowCar]
# All 3 cars start their engines
for car in cars:
    car.engine_toggle()
# FancyCar and FastCar turn on their headlights
FastCar.headlights_toggle()
FancyCar.headlights_toggle()

# All three cars gas for 11 seconds
# All three cars drive for 30 seconds
for car in cars:
    car.gas(11)
    car.drive(30)
# FancyCar brakes for 5 seconds, slowing down in order to enjoy the scenery around it, then continues driving for 3 seconds
FancyCar.breaking(5)
FancyCar.drive(3)
# SlowCar brakes for 6 seconds, curious what FancyCar is looking at
SlowCar.breaking(False, 6)
# FancyCar realizes they left their lucky keychain behind and immediately
# brakes to a full stop, changes to reverse, gases for 20 seconds, then drives for an additional 30 seconds
FancyCar.breaking(True)
FancyCar.change_gear()
FancyCar.gas(20)
FancyCar.drive(30)

# After realizing headlights aren't that useful while going in reverse, FancyCar turns off its lights
FancyCar.headlights_toggle()
# FastCar, all the while, continues driving
# for another 30 seconds, gasses 20 seconds, and drives an addition 60 seconds
FastCar.drive(30)
FastCar.gas(20)
FastCar.drive(60)
# SlowCar feels lonely (now that both cars have left it behind), comes to a full stop, then turns off its engine
SlowCar.breaking(True)
SlowCar.engine_toggle()
# AAll three cars check their dashboards
for car in cars:
    print('\n', car.name)
    car.check_dash()

# Fancy car honks his horn twice,  celebrating that it found its lost keychain
FancyCar.honk()
FancyCar.honk()

