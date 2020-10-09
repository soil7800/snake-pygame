import pygame
import random

COL = 19
ROW = 19
GRID_CELL = 40
RESOLUTION = COL * GRID_CELL, ROW * GRID_CELL
FPS = 8
GRID = [[pygame.Rect(x * GRID_CELL, y * GRID_CELL, GRID_CELL, GRID_CELL) for y in range(ROW)] for x in range(COL)]
BACKGROUND = pygame.Surface(RESOLUTION)

class Snake:
    default_x = 0
    default_y = 10
    default_len = 3
    default_head_x = 2
    default_head_y = 10
    color = (76, 122, 244)

    def __init__(self):
        self.parts = [GRID[self.default_x + i][self.default_y] for i in range(self.default_len)]
        self.dx = 1
        self.dy = 0
        self.len = self.default_len
        self.head_x = self.default_head_x
        self.head_y = self.default_head_y
    
    def move(self, apple):
        self.head_x += self.dx
        self.head_y += self.dy
        
        if self.head_x < 0 or self.head_x > COL - 1 or self.head_y < 0 or self.head_y > ROW - 1 or GRID[self.head_x][self.head_y].collidelist(self.parts[:-2]) != -1:
            self.__init__()
        elif GRID[self.head_x][self.head_y].colliderect(GRID[apple.x][apple.y]):
            self.parts.append(GRID[self.head_x][self.head_y])
            self.len += 1
            apple.change_coords() 
        else:
            self.parts.append(GRID[self.head_x][self.head_y])
            self.parts = self.parts[-self.len:]

    def change_vector(self, event):
        if event.key == pygame.K_LEFT :
            self.dx , self.dy  = -1, 0
        elif event.key == pygame.K_RIGHT: 
            self.dx , self.dy  = 1, 0
        elif event.key == pygame.K_UP: 
            self.dx , self.dy  = 0, -1
        elif event.key == pygame.K_DOWN: 
            self.dx , self.dy  = 0, 1

    def draw(self, scr):
        for part in self.parts:
            pygame.draw.rect(scr, self.color, part)


class Apple:
    def __init__(self):
        self.x = random.randrange(0, COL)
        self.y = random.randrange(0, ROW)
    
    def draw(self, scr):
        pygame.draw.rect(scr, (228, 73, 27), GRID[self.x][self.y])
    
    def change_coords(self):
        self.x = random.randrange(0, COL)
        self.y = random.randrange(0, ROW)

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(RESOLUTION)
    apple = Apple()
    snake = Snake()
    
    # main cycle
    while True:
        screen.fill(pygame.Color('black'))
        
        for x in range(COL):
            for y in range(ROW):
                if x % 2 != 0:
                    if y % 2 != 0:
                        pygame.draw.rect(screen, (171, 214, 81), GRID[x][y])
                    else:
                        pygame.draw.rect(screen, (161, 207, 72), GRID[x][y])
                else:
                    if y % 2 == 0:
                        pygame.draw.rect(screen, (171, 214, 81), GRID[x][y])
                    else:
                        pygame.draw.rect(screen, (161, 207, 72), GRID[x][y])
                
        apple.draw(screen)
        snake.move(apple)
        snake.draw(screen)
        pygame.display.update()
        clock.tick(FPS)
        # check event list
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
               snake.change_vector(event)
               break
        
        
