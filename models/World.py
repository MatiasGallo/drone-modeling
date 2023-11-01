import constants.dimensions as dimensions
import constants.commands as Commands
from models.Coordinate import Coordinate
from models.Drone import Drone
from models.Command import Command

class World:

    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    # Giving a Drone and a command creates the potential destination
    def destinationFromCommand(self, drone: Drone, command: Command) -> Coordinate:
        if command.direction == Commands.COMMAND_RIGHT:
            return Coordinate(drone.coordinate.x + command.distance,drone.coordinate.y,drone.coordinate.z)
        if command.direction == Commands.COMMAND_LEFT:
            return Coordinate(drone.coordinate.x - command.distance,drone.coordinate.y,drone.coordinate.z)
        if command.direction == Commands.COMMAND_UP:
            return Coordinate(drone.coordinate.x,drone.coordinate.y + command.distance,drone.coordinate.z)
        if command.direction == Commands.COMMAND_DOWN:
            return Coordinate(drone.coordinate.x,drone.coordinate.y - command.distance,drone.coordinate.z)
        if command.direction == Commands.COMMAND_FORWARD:
            return Coordinate(drone.coordinate.x,drone.coordinate.y,drone.coordinate.z + command.distance)
        if command.direction == Commands.COMMAND_BACKWARD:
            return Coordinate(drone.coordinate.x,drone.coordinate.y,drone.coordinate.z - command.distance)

        return Coordinate(drone.coordinate.x,drone.coordinate.y,drone.coordinate.z)

    # Checks if a command for a drone is out of bounds of the world
    def validMovemtByComand(self, drone: Drone, command: Command):
        if command.direction == Commands.COMMAND_FORWARD:
            destination = drone.coordinate.z + command.distance
            return destination <= self.width
        
        if command.direction == Commands.COMMAND_BACKWARD:
            destination = drone.coordinate.z - command.distance
            return destination >= dimensions.MIN_DEPTH
        
        if command.direction == Commands.COMMAND_UP:
            destination = drone.coordinate.y + command.distance   
            return destination <= self.width
        
        if command.direction == Commands.COMMAND_DOWN:
            destination = drone.coordinate.y - command.distance
            return destination >= dimensions.MIN_HEIGHT
        
        if command.direction == Commands.COMMAND_RIGHT:
            destination = drone.coordinate.x + command.distance
            return destination <= self.width
        
        if command.direction == Commands.COMMAND_LEFT:
            destination = drone.coordinate.x - command.distance
            return destination >= dimensions.MIN_WIDTH

    # Corrects destination if out of bounds of the world
    def validdestination(self,  destination: Coordinate):
        if destination.x > self.width:
            destination.x = self.width
            return destination
        if destination.x < dimensions.MIN_WIDTH:
            destination.x = dimensions.MIN_WIDTH
            return destination
        if destination.y > self.height:
            destination.y = self.height
            return destination
        if destination.y < dimensions.MIN_HEIGHT:
            destination.y = dimensions.MIN_HEIGHT
            return destination        
        if destination.z > self.depth:
            destination.z = self.depth
            return destination
        if destination.z < dimensions.MIN_DEPTH:
            destination.z = dimensions.MIN_DEPTH
            return destination
        
    def moveDron(self, drone: Drone, command: Command):
        destination = self.destinationFromCommand(drone,command)

        if self.validMovemtByComand(drone,command):
            drone.move(destination)
        else:
            print("CRASH IMMINENT - AUTOMATIC COURSE CORRECTION")
            drone.move(self.validdestination(destination))

    def __str__(self):
        return f"World: (x=range({dimensions.MIN_WIDTH}, {self.width}),y=range({dimensions.MIN_HEIGHT}, {self.height}),z=range({dimensions.MIN_DEPTH}, {self.depth}))"