"""
Implement the __str__ magic method for the Point and Vector classes. For the Point class, the method must return a string of the form Point(x,y), and for the Vector class - the string Vector(x,y), as in the example below (instead of x/y, you must substitute the coordinates of the class instance):

point = Point(1, 10)
vector = Vector(point)

print(point)  # Point(1,10)
print(vector)  # Vector(1,10)
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
    def __str__(self):
        return f"Point({self.x},{self.y})"

    
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
    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"

# Example usage:
vector = Vector(Point(1, 10))

print(vector.coordinates.x)  # Output: 1
print(vector.coordinates.y)  # Output: 10

vector[0] = 10  # Set the x coordinate of the vector to 10