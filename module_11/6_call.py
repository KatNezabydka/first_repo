"""
You have to implement a functor for an instance of the Vector class. Create a __call__ method for the Vector class. 
It should realize the following behavior:

vector = Vector(Point(1, 10))

print(vector())  # (1, 10)
When you call a class instance as a function, it returns a tuple with the coordinates of the vector.

If we transfer the number parameter when calling, we perform the product of the vector by the number: 
we multiply each coordinate by the specified number and return a tuple with the new vector coordinates.

vector = Vector(Point(1, 10))

print(vector(5))  # (5, 50)
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
    
    def __call__(self, value=1):
        return (self.coordinates.x*value, self.coordinates.y*value)
    

# Example usage:
vector = Vector(Point(1, 10))

print(vector.coordinates.x)  # Output: 1
print(vector.coordinates.y)  # Output: 10
print(vector()) 
print(vector(5))  

vector[0] = 10  # Set the x coordinate of the vector to 10