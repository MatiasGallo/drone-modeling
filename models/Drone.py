class Drone:

    totalDistance = 0

    def __init__(self, coordinate):
        self.coordinate = coordinate
        print("Drone's initial position is: " + str(self.coordinate))

    # Moves the Drone to destination
    def move(self, destination):
        self.totalDistance = self.totalDistance + self.coordinate.dif(destination)
        self.coordinate = destination
        print("Drone's new position is: " + str(self.coordinate) + f" [{self.totalDistance}]")