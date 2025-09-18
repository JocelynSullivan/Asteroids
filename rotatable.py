from pygame import Surface
from movable import Movable
import math

class Rotatable(Movable):
    
    def __init__(self, x:float, y:float, dx:float, dy:float, rotation:float, world_width:float, world_height:float):
        super().__init__(x, y, dx, dy, world_width, world_height)
        self.mRotation = rotation

    def getRotation(self):
        return self.mRotation

    def rotate(self, delta_rotation:float) -> None:
        self.mRotation = (self.mRotation + delta_rotation) % 360

    def splitDeltaVIntoXAndY(self, rotation:float, delta_velocity:float) -> tuple:
        radian = math.radians(rotation)

        new_x = math.cos(radian) * delta_velocity
        new_y = math.sin(radian) * delta_velocity

        return(new_x, new_y)

    def accelerate(self, delta_velocity:float) -> None:
        x_and_y = self.splitDeltaVIntoXAndY(self.mRotation, delta_velocity)

        self.mDX += x_and_y[0]
        self.mDY += x_and_y[1]

    def rotatePoint(self, x:float, y:float) -> tuple:
        radian = math.radians(self.mRotation)
        new_x = (math.cos(radian) * x) - (math.sin(radian) * y)
        new_y = (math.sin(radian) * x) + (math.cos(radian) * y)

        return (new_x, new_y)

    def translatePoint(self, x:float, y:float) -> tuple:
        x += self.mX
        y += self.mY

        return (x, y)

    def rotateAndTranslatePoint(self, x:float, y:float) -> tuple:
        rotated_point = self.rotatePoint(x,y)
        translated_point = self.translatePoint(rotated_point[0], rotated_point[1])
        return translated_point
        
    def rotateAndTranslatePointList(self, point_list:list[tuple]) -> list[tuple]:
        new_point_list = []

        for i in point_list:
            new_point = self.rotateAndTranslatePoint(i[0], i[1])

            new_point_list.append(new_point)

        return new_point_list

