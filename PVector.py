from Typing import Iterable
import math

class PVector:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

    def __repr__(self) -> Iterable[float]:
        return (self.x, self.y)

    def length(self) -> float:
        return (self.x**2 + self.y**2)**0.5

def rotate(pvector: PVector, radians: float) -> PVector:
    "Rotates the vector by the specified radians and returns a new PVector object"
    x = pvector.x * math.cos(radians) - pvector.y * math.sin(radians)
    y = pvector.x * math.sin(radians) + pvector.y * math.cos(radians)
    pvector.x = x
    pvector.y = y
    return PVector(x,y)

def add(pvector1: PVector, pvector2: PVector) -> PVector:
    "Adds two vectors and returns the result as a new PVector object."
    x = pvector1.x + pvector2.x
    y = pvector1.y + pvector2.y
    return PVector(x, y)

def sub(pvector1: PVector, pvector2: PVector) -> PVector:
    "Substracts two vectors and returns the result as a new PVector object."
    x = pvector1.x - pvector2.x
    y = pvector1.y - pvector2.y
    return PVector(x, y)

def mul(pvector, i: float) -> PVector:
    "Multiplies a vector with a number and returns the result as a new PVector object."
    x = pvector.x * i
    y = pvector.y * i
    return PVector(x,y)

def normalize(pvector: PVector) -> PVector:
    "returns the normalized vector as a new PVector object"
    l = pvector.length()
    x = pvector.x/l
    y = pvector.y/l
    return PVector(x,y)
    
