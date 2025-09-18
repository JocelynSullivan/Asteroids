from circle import Circle

class Bullet(Circle):

    def __init__(self, x:float, y:float, dx:float, dy:float, rotation:float, world_width:float, world_height:float):
        super().__init__(x, y, dx, dy, rotation, 3, world_width, world_height)
        self.mAge: float = 0
        self.accelerate(200.0)
        self.move(0.1)

    def getAge(self) -> float:
        return self.mAge

    def setAge(self, age:float) -> None:
        if age > 0:
            self.mAge = age

    def evolve(self, dt) -> None:
        self.move(dt)
        self.mAge += dt

        if self.mAge > 4:
            self.setActive(False)
