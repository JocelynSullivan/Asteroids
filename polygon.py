import math, pygame
from pygame import Surface, Color
from rotatable import Rotatable

class Polygon(Rotatable):
    
    def __init__(self, x:float, y:float, dx:float, dy:float, rotation:float, world_width:float, world_height:float):
        super().__init__(x, y, dx, dy, rotation, world_width, world_height)
        self.mOriginalPolygon: list[tuple] = []
        self.mColor: Color = Color(0, 255, 255)

    def getColor(self):
        return self.mColor

    def getPolygon(self):
        return self.mOriginalPolygon

    def setPolygon(self, point_list: list[tuple]) -> tuple:
        self.mOriginalPolygon = point_list

    def setColor(self, color):
        self.mColor = color

    def draw(self, surface: Surface):
        rotated_points = self.rotateAndTranslatePointList(self.mOriginalPolygon) 
        pygame.draw.polygon(surface, self.mColor, rotated_points)

    def getRadius(self):
        total = 0 

        if len(self.mOriginalPolygon) > 0: 
            for i in self.mOriginalPolygon:
                c = math.sqrt(i[0]**2 + i[1]**2)

                total += c
            average = total/len(self.mOriginalPolygon)
            return average
        return 0
            
