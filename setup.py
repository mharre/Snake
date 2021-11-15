import pygame, sys, random
from pygame.math import Vector2

class Snake:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

        self.head_up = pygame.image.load('graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('graphics/head_left.png').convert_alpha()
        
        self.tail_up = pygame.image.load('graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('graphics/body_bl.png').convert_alpha()

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for i,block in enumerate(self.body):
            #rect for positioning
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            
            #what direction the face is heading
            if i == 0:
                screen.blit(self.head, block_rect)
            elif i == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[i + 1] - block
                next_block = self.body[i - 1] - block
                if previous_block.x == next_block.x: #if both have same x we know it will be a vertical block, if same y = horizontal
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect) #corner is going up and left (topleft)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)



            # else:
            #     pygame.draw.rect(screen,(150,100,100), block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): #means head is to left of next block
            self.head = self.head_left
        elif head_relation == Vector2(-1,0):
            self.head = self.head_right
        elif head_relation == Vector2(0,1): #block below snake that means we are moving up
            self.head = self.head_up
        elif head_relation == Vector2(0,-1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): 
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): 
            self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1):
            self.tail = self.tail_down

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def grow_snake(self):
        self.new_block = True

class Fruit:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size) #x,y,w,h
        screen.blit(apple,fruit_rect) #always need a rect or surface/position
        # pygame.draw.rect(screen,(126,166,114),fruit_rect) #surface to draw on, color, rectangle

    def randomize(self):
        self.x = random.randint(0, cell_number-1)
        self.y = random.randint(0, cell_number-1)
        self.pos = Vector2(self.x, self.y)

class Main():
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.grow_snake()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number: #if not between 0 and the number of cells
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()
        
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size , cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load('graphics/apple.png').convert_alpha()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150) #in milliseconds

main_game = Main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SCREEN_UPDATE:
            main_game.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)

            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)

            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)

            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)


    screen.fill((175,215,70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
