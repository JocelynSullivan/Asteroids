import pygame
import random
from pygame import Surface
from ship import Ship
from rock import Rock
from star import Star
from bullet import Bullet
from text import Text
from text import Text2

class Asteroids:

    pygame.mixer.init()

    def __init__(self, world_width:float, world_height:float):
        self.mWorldWidth = world_width
        self.mWorldHeight = world_height
        self.mShip = Ship(world_width//2, world_height//2, world_width, world_height)
        self.mRocks = [Rock(random.uniform(0, world_width), random.uniform(0, world_height), world_width, world_height, Rock.LARGE) for i in range(10)]
        self.mObjects = [self.mShip] + self.mRocks
        self.mBullets = []
        self.mStars = [Star(random.uniform(0, world_width), random.uniform(0, world_height), world_width, world_height) for i in range(20)]
        self.mObjects = [self.mShip] + self.mRocks + self.mBullets + self.mStars

    def getWorldWidth(self) -> float:
        return self.mWorldWidth

    def getWorldHeight(self) -> float:
        return self.mWorldHeight

    def getShip(self) -> Ship:
        return self.mShip

    def getStars(self) -> list[Star]:
        return self.mStars

    def getBullets(self) ->list[Bullet]:
        return self.mBullets

    def getShip(self) -> Ship:
        return self.mShip

    def getRocks(self) -> list[Rock]:
        return self.mRocks

    def getObjects(self):
        return self.mObjects

    def turnShipLeft(self, delta_rotation):
        self.mShip.mRotation = (self.mShip.mRotation - delta_rotation)%360

    def turnShipRight(self, delta_rotation):
        self.mShip.mRotation = (self.mShip.mRotation + delta_rotation)%360

    def fire(self) -> None:
        self.pew()
        new_bullet = self.mShip.fire()
        self.mBullets.append(new_bullet)
        self.mObjects.append(new_bullet)

    def accelerateShip(self, delta_velocity):
        self.mShip.accelerate(delta_velocity)

    def evolve(self, dt):
        self.evolveAllObjects(dt)
        self.collideRocksAndBullets()
        self.collideShipAndRocks()
        self.removeInactiveObjects()

    def evolveAllObjects(self, dt):
        for i in self.mObjects:
            i.evolve(dt)

    def collideShipAndRocks(self) -> None:
        for rock in self.mRocks:
            if self.mShip.hits(rock) == True:
                self.mShip.setActive(False)
                for bullet in self.mBullets:
                    bullet.setActive(False)

    def collideRocksAndBullets(self) -> None:
        for rock in self.mRocks:
            for bullet in self.mBullets:
                if rock.hits(bullet) == True:
                    self.boom() 
                    size_down = rock.nextSize()
                    if size_down != 0:
                        r1 = Rock(rock.mX+(random.uniform(30, 60)), rock.mY+(random.uniform(30, 60)), self.mWorldWidth, self.mWorldHeight, size_down)
                        r2 = Rock(rock.mX+(random.uniform(30, 60)), rock.mY+(random.uniform(30, 60)), self.mWorldWidth, self.mWorldHeight, size_down)
                        self.mRocks.append(r1)
                        self.mRocks.append(r2)
                        self.mObjects.append(r1)
                        self.mObjects.append(r2)
                    rock.setActive(False)
                    bullet.setActive(False)
                    self.mBullets.remove(bullet)

    def removeInactiveObjects(self) -> None:
        for item in self.mObjects:
            if item.getActive() == False:
                self.mObjects.remove(item)

        for item in self.mBullets:
            if item.getActive() == False:
                self.mBullets.remove(item)

        for item in self.mRocks:
            if item.getActive() == False:
                self.mRocks.remove(item)

    def pew(self):
        pew_sfx = pygame.mixer.Sound("pew.wav")
        pew_sfx.play()

    def boom(self):
        pow_sfx = pygame.mixer.Sound("pow.wav")
        pow_sfx.play()

    def aww(self):
        aww_sfx = pygame.mixer.Sound("Awww.wav")
        aww_sfx.play()

    def yay(self):
        yay_sfx = pygame.mixer.Sound("Yayyy.wav")
        yay_sfx.play()

    def draw(self, surface):
        background = pygame.Rect(0, 0, self.mWorldWidth, self.mWorldHeight)
        pygame.draw.rect(surface, (255, 55, 222), background)
        for item in self.mObjects:
            item.draw(surface)

        if self.mShip.getActive() == False:
            gameOverText = Text("Game Over", 720, 350)
            replayText = Text2("press enter to replay", 720, 450)
            gameOverText.draw(surface)
            replayText.draw(surface)
            self.mBullets = []
            self.aww()

        if self.mRocks == []:
            self.yay()
            youWinText = Text("You Win!", 720, 350)
            replayText = Text2("press enter to replay", 720, 450)
            youWinText.draw(surface)
            replayText.draw(surface)
