import pygame
import random

COL = 19
ROW = 19
GRID_CELL = 40
RESOLUTION = COL * GRID_CELL, ROW * GRID_CELL
FPS = 8
GRID = []
AVIABLE_COORDS = set()
for x in range(COL):
    GRID.append([])
    for y in range(ROW):
        GRID[x].append(pygame.Rect(x * GRID_CELL, y * GRID_CELL, GRID_CELL, GRID_CELL))
        AVIABLE_COORDS.add((x, y))

class Snake:
    color = (76, 122, 244)

    def __init__(self):
        self.parts = [(0 + i, 9) for i in range(3)]
        self.dx = 1
        self.dy = 0
        self.head_x = 2
        self.head_y = 9
    
    def move(self, apple):
        self.head_x += self.dx
        self.head_y += self.dy
        if self.head_x < 0 or self.head_x > COL - 1 or self.head_y < 0 or self.head_y > ROW - 1 or (self.head_x, self.head_y) in set(self.parts):
            self.__init__()
            apple.__init__()
        elif GRID[self.head_x][self.head_y].colliderect(GRID[apple.x][apple.y]):
            self.parts.append((self.head_x, self.head_y))
            apple.aviable_coords.discard((self.head_x, self.head_y))
            apple.change_coords()
        else:
            self.parts.append((self.head_x, self.head_y))
            apple.aviable_coords.discard((self.head_x, self.head_y))
            apple.aviable_coords.add((self.parts[0][0], self.parts[0][1]))
            self.parts = self.parts[1:]

    def change_vector(self, event):
        if event.key == pygame.K_LEFT and self.dx != 1:
            self.dx , self.dy  = -1, 0
        elif event.key == pygame.K_RIGHT and self.dx != -1: 
            self.dx , self.dy  = 1, 0
        elif event.key == pygame.K_UP and self.dy != 1: 
            self.dx , self.dy  = 0, -1
        elif event.key == pygame.K_DOWN and self.dy != -1: 
            self.dx , self.dy  = 0, 1

    def draw(self, scr):
        for x, y in self.parts:
            pygame.draw.rect(scr, self.color, GRID[x][y])


class Apple:
    
    def __init__(self):
        self.aviable_coords = AVIABLE_COORDS.difference({(0, 9), (1, 9), (2, 9)})
        self.x, self.y = self.aviable_coords.pop()
    
    def draw(self, scr):
        pygame.draw.rect(scr, (228, 73, 27), GRID[self.x][self.y])
    
    def change_coords(self):
        self.x, self.y = self.aviable_coords.pop()
        print(len(self.aviable_coords))


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
        
        
