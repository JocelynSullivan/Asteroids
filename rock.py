import math, random
from polygon import Polygon
from rotatable import Rotatable
from movable import Movable

class Rock(Polygon):

    LARGE = 5
    MEDIUM = 3
    SMALL = 1

    def __init__(self, x:float, y:float, world_width:float, world_height:float, size:float):
        super().__init__(x, y, 10, 10, random.uniform(0.0, 359.9),world_width, world_height)
        self.mSpinRate = random.uniform(-90, 90)
        self.accelerate(random.uniform(100/size, 150/size))
        self.mRandomPolygon = self.createRandomPolygon((5*size), 5)
        self.setPolygon(self.mRandomPolygon)
        self.mSize = size
    
    def createRandomPolygon(self, radius:float, number_of_points:float) -> list[float,float]:
        points_list = []
        angle = math.radians(360/number_of_points)
        for i in range(number_of_points):
            random_radius = random.uniform(1.5, 3) * radius
            x = math.cos(angle * i) * random_radius
            y = math.sin(angle * i) * random_radius

            points_list.append((x, y))
        
        return points_list
   
    def nextSize(self) -> int:
        if self.mSize == Rock.LARGE:
            return Rock.MEDIUM
        elif self.mSize == Rock.MEDIUM:
            return Rock.SMALL
        elif self.mSize == Rock.SMALL:
            return 0

    def getSpinRate(self) -> None:
        return self.mSpinRate

    def setSpinRate(self, spin_rate:float) -> None:
        self.mSpinRate = spin_rate

    def evolve(self, dt:float) -> float:
        self.move(dt)
        self.rotate(dt * self.mSpinRate) 
        
