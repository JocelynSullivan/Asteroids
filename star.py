import random
from circle import Circle

class Star(Circle):

    def __init__(self, x:float, y:float, world_width:float, world_height:float):
        super().__init__(x, y, 0, 0, 0, 2, world_width, world_height)
        self.mBrightness:int = random.uniform(0, 255)

    def getBrightness(self) -> int:
        return self.mBrightness

    def setBrightness(self, brightness) -> None:
        if brightness >= 0 and brightness <= 255:
            self.mBrightness = brightness
            self.mColor = (self.mBrightness, self.mBrightness, self.mBrightness)

    def evolve(self, dt):
        change_brightness = [10, -10, 0]
        random_brightness = random.choice(change_brightness)
        
        self.mBrightness = self.mBrightness + random_brightness
        self.mColor = (self.mBrightness, self.mBrightness, self.mBrightness)
