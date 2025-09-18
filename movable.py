import math
import pygame
from pygame import Surface

class Movable:
    
    def __init__(self, x:float, y:float, dx:float, dy:float, world_width:float, world_height:float):
        self.mX = x
        self.mY = y
        self.mDX = dx
        self.mDY = dy
        self.mWorldWidth = world_width
        self.mWorldHeight = world_height
        self.mActive: bool = True

    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getDX(self):
        return self.mDX

    def getDY(self):
        return self.mDY

    def getWorldWidth(self):
        return self.mWorldWidth

    def getWorldHeight(self):
        return self.mWorldHeight

    def getActive(self):
        return self.mActive

    def setActive(self, active):
        self.mActive = active

    def move(self, dt) -> None:
        self.mX = self.mX + (self.mDX * dt)
        self.mY = self.mY + (self.mDY * dt)
        self.mX = self.mX % self.mWorldWidth
        self.mY = self.mY % self.mWorldHeight
       
    def hits(self, other: "Movable") -> bool:
        distance = math.sqrt(((self.getX() - other.getX()) **2) + ((self.getY() - other.getY()) **2))

        if distance <= self.getRadius() + other.getRadius():
            return True
        return False

    def accelerate(self, delta_velocity:float) -> None:
        raise NotImplementedError

    def evolve(self, dt:float) -> None: 
        raise NotImplementedError

    def draw(self, surface: Surface) -> None:
        raise NotImplementedError
        
    def getRadius(self):
        raise NotImplementedError
