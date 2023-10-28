from models.Drone import Drone
from models.World import World
from models.Coordinate import Coordinate
from models.Command import Command

def test_creating_coordinate():
    coordinate = Coordinate(1,2,5)
    assert (coordinate.x == 1 and coordinate.y == 2 and coordinate.z == 5)

def test_creating_dron():
    drone = Drone(Coordinate(3,5,7))
    assert (drone.coordinate.x == 3 and drone.coordinate.y == 5 and drone.coordinate.z == 7)

def test_creating_dron():
    world = World(9,10,12)
    assert (world.width == 9 and world.height == 10 and world.depth == 12)

def test_creating_Command():
    command = Command(2,'UP',4)
    assert (command.order == 2 and command.direction == 'UP' and command.distance == 4)