import pygame, sys

pygame.init()
screen = pygame.display.set_mode((400,500))
clock = pygame.time.Clock()
test_surface = pygame.Surface((100,200)) #then need to add it to our game
test_surface.fill((15,220,243))
# test_rect = pygame.Rect(100,200,100,100) #rect to wrap around stuff to keep track of movement,collisions,placement, used for drawing etc ## x,y,w,h
test_rect = test_surface.get_rect(center = (200,250))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #draw all of our elements (background,snake,fruits,etc)
    screen.fill((175,215,70))
    # pygame.draw.rect(screen, pygame.Color('red'), test_rect) #surface to draw on, color, and rect
    test_rect.right += 1
    screen.blit(test_surface,test_rect) 
                                        #created a new surface(100,200 pixels wide)
                                        #wrapped it with a rect object
                                        #centered the entire thing from the middle point(instead of top left)
                                        #used blit to actually place it on the screen
    pygame.display.update()
    clock.tick(60)