import math

def pow(base, exponent):
    	return math.pow(3,4)

def pi(circumference, diameter):
	return round(circumference/diameter,2)

def test_answer():
    	assert pow(3, 4) == 27

def test_pi():
	assert round(math.pi,2) == pi(21, 7)

