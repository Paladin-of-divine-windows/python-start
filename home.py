import pygame
from pygame.draw import rect, polygon, circle

 
pygame.init()

FPS = 30
height = 600
width = 1000
contours_thickness = 1
screen = pygame.display.set_mode((width,height))
sky_color = (0, 191, 255)
grass_color = (63, 155, 11)
home_color = (183, 125, 84)
roof_color = (178, 34, 34)
contours_color = (0, 0, 0)
window_color = (128, 166, 255)
window_conturs = (101, 67, 33)
leaves_color = (67, 106, 13)
cloud_color = (255, 255, 255)
sun_color = (255, 207, 72)


def grass():
    """The function draw grass"""

    rect(screen, grass_color, (0, height/2, width, height/2))


def sky():
    """The function draw sky"""

    rect(screen, sky_color, (0, 0, width, height/2))


def home():
    """The function draw home, roof and window"""

    rect(screen, home_color, (width/16, height/2.5, width/6, height/4.5))
    polygon(screen, roof_color, [[width/17, height/2.5], [width/4.3, height/2.5], [width/7, height/5]])
    rect(screen, contours_color, (width/16, height/2.5, width/6, height/4.5), contours_thickness)
    polygon(screen, contours_color, [[width/17, height/2.5], [width/4.3, height/2.5], [width/7, height/5]], contours_thickness)
    rect(screen, window_color, (width/9.2, height/2.2, width/14, height/10))
    rect(screen, window_conturs, (width/9.2, height/2.2, width/14, height/10), contours_thickness)

def tree():
     """The function draw tree with leaves"""
     rect(screen, (0, 0, 0), (width/1.5, height/2.7, width/70, height/4.5))
     circle(screen, leaves_color, (int(width/1.48), int(height/4.7)), 38)
     circle(screen, contours_color, (int(width/1.48), int(height/4.7)), 38, contours_thickness)
     circle(screen, leaves_color, (int(width/1.55), int(height/3.7)), 38)
     circle(screen, contours_color, (int(width/1.55), int(height/3.7)), 38, contours_thickness)
     circle(screen, leaves_color, (int(width/1.41), int(height/3.7)), 38)
     circle(screen, contours_color, (int(width/1.41), int(height/3.7)), 38, contours_thickness)
     circle(screen, leaves_color, (int(width/1.48), int(height/3.2)), 38)
     circle(screen, contours_color, (int(width/1.48), int(height/3.2)), 38, contours_thickness)
     circle(screen, leaves_color, (int(width/1.55), int(height/2.7)), 38)
     circle(screen, contours_color, (int(width/1.55), int(height/2.7)), 38, contours_thickness)          
     circle(screen, leaves_color, (int(width/1.41), int(height/2.7)), 38)
     circle(screen, contours_color, (int(width/1.41), int(height/2.7)), 38, contours_thickness)


def cloud():
     """The function draw cloud"""
     circle(screen, cloud_color, (int(width/3), int(height/7)), 38)
     circle(screen, contours_color, (int(width/3), int(height/7)), 38, contours_thickness)
     circle(screen, cloud_color, (int(width/2.53), int(height/7)), 38)
     circle(screen, contours_color, (int(width/2.53), int(height/7)), 38, contours_thickness)
     circle(screen, cloud_color, (int(width/2.33), int(height/7)), 38)
     circle(screen, contours_color, (int(width/2.33), int(height/7)), 38, contours_thickness)
     circle(screen, cloud_color, (int(width/2.48), int(height/12)), 38)
     circle(screen, contours_color, (int(width/2.48), int(height/12)), 38, contours_thickness)
     circle(screen, cloud_color, (int(width/2.85), int(height/12)), 38)
     circle(screen, contours_color, (int(width/2.85), int(height/12)), 38, contours_thickness)


def sun():
     """The function draw sun"""
     circle(screen, sun_color, (int(width/1.2), int(height/12)), 43)
  

grass()
sky()
home()
tree()
cloud()
sun()


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()