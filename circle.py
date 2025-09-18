import pygame
from rotatable import Rotatable

class Circle(Rotatable):
    
    def __init__(self, x:float, y:float, dx:float, dy:float, rotation:float, radius:float, world_width:float, world_height:float):
        super().__init__(x, y, dx, dy, rotation, world_width, world_height)
        self.mRadius = radius
        self.mColor = (255, 255, 255)

    def getRadius(self) -> float:
        return self.mRadius

    def getColor(self) -> tuple:
        return self.mColor

    def setRadius(self, radius:float) -> None:
        if radius >= 1:
            self.mRadius = radius

    def setColor(self, color:tuple) -> None:
        self.mColor = color

    def draw(self, surface) -> None:
        pygame.draw.circle(surface, (255, 255, 255), [self.mX, self.mY], self.mRadius)
