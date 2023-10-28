from models.Drone import Drone
from models.World import World
from models.Coordinate import Coordinate
from models.Command import Command

def test_creating_dron_destination():
    world = World(10,10,10)
    drone = Drone(Coordinate(5,5,5))
    command = Command(1,"LEFT", 7)
    destination = world.destinationFromCommand(drone,command)
    assert (destination.x == -2)

def test_valid_dron_destination_fail():
    world = World(10,10,10)
    drone = Drone(Coordinate(5,5,5))
    command = Command(1,"LEFT", 7)

    assert (not world.validMovemtByComand(drone,command))

def test_valid_dron_destination_correct():
    world = World(10,10,10)
    drone = Drone(Coordinate(5,5,5))
    command = Command(1,"LEFT", 2)
    assert (world.validMovemtByComand(drone,command))

def test_moving_dron():
    world = World(10,10,10)
    drone = Drone(Coordinate(5,5,5))
    command = Command(1,"LEFT", 2)
    world.moveDron(drone,command)
    assert (drone.coordinate.x == 3)

def test_moving_dron_crash():
    world = World(10,10,10)
    drone = Drone(Coordinate(5,5,5))
    command = Command(1,"UP", 11)
    world.moveDron(drone,command)
    assert (drone.coordinate.y == 10)

def test_land_drone():
    world = World(10,10,10)
    drone = Drone(Coordinate(5,5,5))
    world.landDrone(drone)
    assert (drone.coordinate.y == 0)