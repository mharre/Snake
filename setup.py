import pygame, sys

pygame.init()
screen = pygame.display.set_mode((400,500))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #draw all of our elements (background,snake,fruits,etc)
    pygame.display.update()
    clock.tick(60)