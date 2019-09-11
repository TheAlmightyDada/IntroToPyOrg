class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.

    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0

    def move_up(self):
        # Increment the y-pos of the rocket.
        self.y += 1

# Create a Rocket Object, and have it start to move up.

my_rocket = Rocket()
print('Rocket altitude:', my_rocket.y)

my_rocket.move_up()
print('Rocket altitude:', my_rocket.y)
