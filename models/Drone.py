class Drone:

    totalDistance = 0

    def __init__(self, coordinate):
        self.coordinate = coordinate
        print(self)

    # Moves the Drone to destination
    def move(self, destination):
        self.totalDistance = self.totalDistance + self.coordinate.dif(destination)
        self.coordinate = destination
        print(self)

    def __str__(self):
        return f"Drone's position is: " + str(self.coordinate) + f" [{self.totalDistance}]"