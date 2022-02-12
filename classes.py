import pygame

class Screen():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.title = pygame.display.set_caption("Battle")
        self.background_img = pygame.image.load("background.png")
        self.background = self.window.blit(self.background_img, (0,0))