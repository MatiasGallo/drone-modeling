from models.Coordinate import Coordinate

def test_adding_coordinate():
    coordinate_src = Coordinate(1,2,5)
    coordinate_add = Coordinate(1,3,4)
    coordinate_result = coordinate_src.add(coordinate_add)
    assert (coordinate_result.x == coordinate_src.x + coordinate_add.x
            and coordinate_result.y == coordinate_src.y + coordinate_add.y
            and coordinate_result.z == coordinate_src.z + coordinate_add.z)

def test_str_coordinate():
    coordinate = Coordinate(1,2,5)
    assert (str(coordinate) == f"x: {coordinate.x} / y: {coordinate.y} / z: {coordinate.z}")