import pygame
import random

# Variables
WIDTH = 1280
HEIGHT = 720
FPS = 120
RECT_SIZE = 1
VERTICES = [(WIDTH/2, HEIGHT/8), (WIDTH/4, HEIGHT/8*7), (WIDTH/4*3, HEIGHT/8*7)]
point = [500, 500]  # Starting point
counter = 0

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Initialize pygame and create window
pygame.init()
font = pygame.font.Font(None, 25)
screen = pygame.display.set_mode((WIDTH*RECT_SIZE, HEIGHT*RECT_SIZE))
pygame.display.set_caption("Chaos Game Animation")
clock = pygame.time.Clock()
running = True


def get_mid_point(p1, p2):
    """"
    Calculating the point halfway between two given points
    """
    p3 = ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)
    return p3


while running:
    clock.tick(FPS)
    counter += 1    # Keeping track on how many dots are drawn
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    rand_vertex = random.choice(VERTICES)   # Random point out of the three vertices of the triangle
    point = get_mid_point(point, rand_vertex)   # New point
    pygame.draw.rect(screen, GREEN, pygame.Rect(point[0] * RECT_SIZE, point[1] * RECT_SIZE, RECT_SIZE, RECT_SIZE))
    label = font.render("Dots drawn: " + str(counter), 1, WHITE)    # Printing counter to the screen
    pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, 300, 300))    # Hiding the previous counter printing
    screen.blit(label, (10, 10))

    pygame.display.flip()
pygame.quit()

