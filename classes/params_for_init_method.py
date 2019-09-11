class Rocket():
    # Rocket() simulates a rocket ship.
    def __init__(self, x=0, y=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y

    def move_up(self):
        # move_up() will increase the y-position of the rocket.
        self.y += 1

# Make a series of rockets at different starting places.
rockets = []
rockets.append(Rocket())
rockets.append(Rocket(0,10))
rockets.append(Rocket(100,0))

# Show where each rocket is.
for i, r in enumerate(rockets):
    print('Rocket %d is at (%d,%d)' %(i, r.x, r.y))