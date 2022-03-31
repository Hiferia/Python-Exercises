from circle import Circle
from math import pi
import pytest

@pytest.fixture
def circle():
    return Circle(10)

def test_init_circle():
    my_circle = Circle(5)
    assert my_circle.radius == 5
    assert my_circle.diameter == 10
    assert my_circle.area == 78.53981633974483
    
    diameter_circle = Circle(diameter=25)
    assert diameter_circle.radius == 12.5
    assert diameter_circle.diameter == 25
    assert diameter_circle.area == 490.8738521234052
    
    float_circle = Circle(43.34)
    assert float_circle.radius == 43.34
    assert float_circle.diameter == 86.68
    assert float_circle.area == 5901.028153789249
    
def test_str_circle(circle):
    assert str(circle) == "Circle properties:\n Radius: 10\n Diameter: 20\n Area: 314.1592653589793"

def test_add_circle(circle):
    other_circle = Circle(5)
    circle += other_circle
    
    assert circle.radius == 15
    assert circle.diameter == 30
    
def test_eq_circle(circle):
    other_circle = Circle(10)
    
    assert circle == other_circle
    
def test_lt_circle(circle):
    other_circle = Circle(20)
    
    assert circle < other_circle

def test_gt_circle(circle):
    other_circle = Circle(5)
    
    assert circle > other_circle
    
def test_scale(circle):
    circle.scale(5)
    assert circle.radius == 15
    
def test_sort_circle():
    circle_list = [Circle(25), Circle(90), Circle(diameter = 100), Circle(5), Circle(20.25)]
    
    circle_list.sort()
    assert circle_list[0].radius == 5
    assert circle_list[1].radius == 20.25
    assert circle_list[2].radius == 25
    assert circle_list[3].radius == 50
    assert circle_list[4].radius == 90
