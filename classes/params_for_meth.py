class Rocket():
    #Rocket Sim

    def __init__(self, x=0, y=0):
        # x & y pos
        self.x = x
        self.y = y

    def move_rocket (self, x_increment=0, y_increment=0):
        # Move rocket acording to perams given.
        self.x += x_increment
        self.y += y_increment

# Create three rockets.
rockets = [Rocket() for x in range(0,3)]

# Show where each rocket is.
for index, rocket in enumerate(rockets):
    print("Rocket %d is at (%d, %d)." % (index, rocket.x, rocket.y))


# Move each rocket a different amount.
rockets[0].move_rocket()
rockets[1].move_rocket(10,10)
rockets[2].move_rocket(-10,0)
          
# Show where each rocket is.
for index, rocket in enumerate(rockets):
    print("Rocket %d is at (%d, %d)." % (index, rocket.x, rocket.y))