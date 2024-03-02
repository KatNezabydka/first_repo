"""
Implement the Vector class. The coordinates property defines the coordinates of the vector and is an instance of the Point class. As you know, a vector is a directed segment with a beginning and an end. The beginning will be at the point (0, 0), and the end of the vector will be set by the coordinates attribute.

Implement the ability to access the coordinates of an instance of the Vector class through square brackets:

vector = Vector(Point(1, 10))

print(vector.coordinates.x)  # 1
print(vector.coordinates.y)  # 10

vector[0] = 10  # Set the x coordinate of the vector to 10

print(vector[0])  # 10
print(vector[1])  # 10
To get a value using the square brackets of the print(vector[0]) object, you have to implement the __getitem__ method of the Vector class.

To store the value of a vector's coordinates using an index, like vector[0] = 10, implement the method __setitem__ in the Vector class.

The x coordinate is accessed at index 0, and the y coordinate is accessed at index 1.
"""
class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) in (int, float):
            self.__x = value
    
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) in (int, float):
            self.__y = value
class Vector:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        
    def __getitem__(self, index):
        match index:
            case 0:
                return self.coordinates.x
            case 1:
                return self.coordinates.y
            case _:
                raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        match index:
            case 0:
                self.coordinates.x = value
            case 1:
                self.coordinates.y = value
            case _:
                raise IndexError("Index out of range")

# Example usage:
vector = Vector(Point(1, 10))

print(vector.coordinates.x)  # Output: 1
print(vector.coordinates.y)  # Output: 10

vector[0] = 10  # Set the x coordinate of the vector to 10