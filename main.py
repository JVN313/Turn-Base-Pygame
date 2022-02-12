import pygame
from classes import Screen

pygame.init()

#Screen/Window creation
screen = Screen(800,400)

#Game Loop
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()