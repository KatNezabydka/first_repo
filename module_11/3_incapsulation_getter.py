"""
In the Point class, add a check for the entered value to the setter mechanism of the x and y properties. 
Allow the x and y properties to be set for an instance of the class only if they have a numeric value (int or float).

Example:

point = Point("a", 10)

print(point.x)  # None
print(point.y)  # 10
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

    
    
point = Point("a", 10)
point = Point(5, 10)
point = Point(True, 10)

print(point.x)  # None
print(point.y)  # 10