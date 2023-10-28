from models.Drone import Drone
from models.Coordinate import Coordinate

def test_moving_dron():
    drone = Drone(Coordinate(3,5,7))
    destination = Coordinate(1,2,7)
    drone.move(destination)
    assert (drone.coordinate == destination)