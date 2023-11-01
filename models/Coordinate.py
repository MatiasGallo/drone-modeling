class Coordinate:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add (self, coordinate: "Coordinate"):
        return Coordinate(self.x + coordinate.x,
                          self.y + coordinate.y,
                          self.z + coordinate.z)
    
    def dif (self, coordinate: "Coordinate"):
        return abs(self.x - coordinate.x) + abs(self.y - coordinate.y) + abs(self.z - coordinate.z)
    
    def mul (self, mult):
        return Coordinate(self.x * mult,
                          self.y * mult,
                          self.z * mult)
    
    def __str__(self):
        return f"x: {self.x} / y: {self.y} / z: {self.z}"