from math import sqrt
from random import randint

shuttles = []
rockets = []

# 'fleet_create' creates a fleet of either Shuttles or ROckets of a number of
#   your choosing

def fleet_create(class_type, reps=1):
    for x in range(0,reps):
        x = randint(0,100)
        y = randint(1,100)
        flights_completed = randint(0,10)
        
        if class_type == Shuttle:
            shuttles.append(Shuttle(x, y, flights_completed))

        else:
            rockets.append(Rocket(x, y))


class Rocket():
    # Simulates a rocket.

    def __init__(self, x=0, y=0):
        # Each rocket has an x and y pos. 
        self.x = x
        self.y = y

    def move_rocket(self, x_increment=0, y_increment=1):
        # Move the rocket according to the parameters given.
        #   Default behavior is to move the rocket up one unit.
        self.x += x_increment
        self.y += y_increment

    def get_distance(self, other_rocket):
        # Calculates the distance from this rocket to another rocket,
        #   and returns that value.
        distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance

class Shuttle(Rocket):
    # Shuttle simulates a space shuttle, which is really
    #   just a reusable rocket.

    def __init__(self, x=0, y=0, flights_completed=0):
        super().__init__(x,y)
        self.flights_completed = flights_completed


# Create several shuttles and rockets, with random positions.
#   Shuttles have a random number of flights completed.

fleet_create(Shuttle, reps=3)
fleet_create(Rocket, reps=3)

print('hello')

