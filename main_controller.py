from models.Drone import Drone
from models.World import World
from models.Coordinate import Coordinate
from models.Command import Command
import constants.commands as Commands
import constants.dimensions as Dimension

def inputValidNumber():
    validNumber = False
    while not validNumber:
        try:
            validNumberValue = int(input("Please input the distance: "))
            if validNumberValue < 0:
                print("Invalid input. Please enter a positive integer.")
            else:
                validNumber = True
        except ValueError:
            print("Invalid input. Please enter an integer.")

    return validNumberValue

def inputValidOrder():
    valid_order = False
    while not valid_order:
        order = input(f"Please input a valid order {Commands.VALID_COMMANDS}: ")
        if order not in Commands.VALID_COMMANDS:
            print('The comand: ' + order + " is invalid. Please try again")
        else:
            valid_order = True

    return order

# Create World
print("=== Volodrone Initialising")
print("=== Volodrone Sensor Data read.")
world = World(10,10,10)
print(world)

#Create Drone
drone = Drone(Coordinate(5,5,5))

#Create Commands
nextCommand = 'Y'
orderNumber = 1
while nextCommand == 'Y':

    #Create Commands
    order = inputValidOrder()
    distance = inputValidNumber() 
    command = Command(orderNumber, order, distance)
    orderNumber = orderNumber + 1

    #Move Drone
    world.moveDron(drone, command)

    nextCommand = input("Would you like to input a new command ? \'Y\' to continue: ")

    
# Land Drone
if not drone.coordinate.y == Dimension.MIN_HEIGHT:
    print('Landing drone')
    drone.move(Coordinate(drone.coordinate.x,Dimension.MIN_HEIGHT,drone.coordinate.z))