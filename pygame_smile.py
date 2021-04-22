import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
rect(screen, (100, 235, 45), (0, 0, 400, 400))
circle(screen, (255, 255, 0), (200, 175), 100)
circle(screen, (255, 0, 0), (150, 150), 20)
circle(screen, (0, 0, 0), (150, 150), 20, 1)
circle(screen, (0, 0, 0), (150, 150), 8)
circle(screen, (255, 0, 0), (250, 150), 17)
circle(screen, (0, 0, 0), (250, 150), 17, 1)
circle(screen, (0, 0, 0), (250, 150), 8)
circle(screen, (0, 0, 0), (200, 175), 100, 1)

rect(screen, (0, 0, 0), (155, 210, 100, 20))
polygon(screen, (255, 255, 255), [[285, 125],[285, 110], [220, 130], [220,140]])
polygon(screen, (255, 255, 255), [[120, 110], [120,95], [180, 130], [180,142]])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()