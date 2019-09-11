class Rocket():
    # Rocket() simulates a rocket ship.
    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0

    def move_up(self):
        # move_up() will increase the y-position of the rocket.
        self.y += 1

# Create a fleet of 5 rockets, and store them in a list.
my_rockets = [ Rocket() for x in range(0,5)]

# Move the first Rocket up.

my_rockets[0].move_up()

# Show that only the fist rocket has moved.
for r in my_rockets:
    print('Rocket altitude:', r.y)