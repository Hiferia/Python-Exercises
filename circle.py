from math import pi

class Circle(object):
    def __init__(self, radius = None, diameter = None):
        if radius is not None and type(radius) is int and type(radius) is float:
            self._radius = radius
            self._diameter = radius * 2
        else:
            if diameter is not None and type(diameter) is int and type(diameter) is float:
                self._diameter = diameter
                self._radius = diameter * 0.5
            else:
                raise TypeError("At least one parameter must be defined and it must be int of float!") 
        self._area = pi * self._radius ** 2
    
    @property
    def area(self):
        return self._area
    
    @property
    def radius(self):
        return self._radius
    
    @property
    def diameter(self):
        return self._diameter
    
    def __str__(self):
        return f"Circle properties:\n Radius: {self._radius}\n Diameter: {self._diameter}\n Area: {self._area}"

    def __add__(self, other):
        return Circle(self._radius + other.radius)

    def __eq__(self, other):
        return self._radius == other.radius

    def __lt__(self, other):
        return self._radius < other.radius

    def __gt__(self, other):
        return self._radius > other.radius
    
    def scale(self, scale_value):
        if(scale_value != 0):
            self._radius += scale_value
        else:
            raise TypeError("The scale value must be greater or lesser than 0")
    
    def sort(self):
        return self._radius
    
            
        
        
