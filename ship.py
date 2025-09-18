from pygame import Color
from polygon import Polygon
from bullet import Bullet

class Ship(Polygon):

    def __init__(self, x:float, y:float, world_width:float, world_height:float):
        super().__init__(x, y, 0, 0, 0, world_width, world_height)
        self.mColor = Color(0, 255, 255)
        self.mShip = self.setPolygon([(15, 15), (-15, 15), (15, -15), (-15, -15)])

    def fire(self):
        bullet_xy = self.rotateAndTranslatePoint(0, 0)
        bullet = Bullet(bullet_xy[0], bullet_xy[1], self.mDX, self.mDY, self.mRotation, self.mWorldWidth, self.mWorldHeight)
        return bullet

    def evolve(self, dt:float):
        self.move(dt)

