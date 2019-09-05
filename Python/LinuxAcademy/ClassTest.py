from Car import Car
from Tire import Tire

tires = Tire('P', 205, 65, 15)
Honda = Car('4-cylinder', [tires])

Honda.description()