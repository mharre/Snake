import pygame, sys, random
from pygame.math import Vector2

class Fruit:
    def __init__(self):
        #create an x/y pos
        # draw a square
        self.x = random.randint(0, cell_number-1)
        self.y = random.randint(0, cell_number-1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        #create a rectangle
        #draw rectangle
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size) #x,y,w,h
        pygame.draw.rect(screen,(126,166,114),fruit_rect) #surface to draw on, color, rectangle


pygame.init()

cell_size = 40
cell_number = 20

screen = pygame.display.set_mode((cell_number * cell_size , cell_number * cell_size))
clock = pygame.time.Clock()

fruit = Fruit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((175,215,70))
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(60)