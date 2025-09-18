import pygame
from pygame import Surface

class Text:

    def __init__(self, string:str, x:float, y:float) -> None:
        self.mX = x
        self.mY = y
        self.mString = string
        self.mColor: tuple(int, int, int) = (0, 0, 0)
        font_height = 100
        font_style = "CREAMPUF"
        self.mFont = pygame.font.Font("CREAMPUF.TTF", font_height)

    def setText(self, string:str) -> None:
        self.mString = string

    def setColor(self, color) -> None:
        self.mColor = color

    def setSize(self, size:int) -> None:
        self.mFont = pygame.font.SysFont(font_style, size)

    def draw(self, surface:Surface) -> None:
        text_object = self.mFont.render(self.mString, False, self.mColor)
        text_rect = text_object.get_rect()
        text_rect.center = (int(self.mX), int(self.mY))
        surface.blit(text_object, text_rect)


class Text2(Text):

    def __init__(self, string:str, x:float, y:float) -> None:
        super().__init__(string, x, y)
        font_height = 10
        


