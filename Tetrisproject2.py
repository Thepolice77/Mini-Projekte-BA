import pygame
import random
import time


# Konstanten für das Spielfeld
WIDTH, HEIGHT = 300, 600
CELL_SIZE = 30
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Farben
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
CYAN=(0,255,255)
ORANGE = (255, 165, 0)
PURPLE=(128,0,128)
YELLOW=(255,255,0)
GREEN=(0,128,0)
BLUE=(0,0,255)

#Formen des Spiels
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[1, 1, 1], [0, 1, 1]]
]
#Farben der Formen 
COLORS=[CYAN,RED,ORANGE,PURPLE,YELLOW,GREEN,BLUE]

#Konstanten für Zeitverzögerung und Beschleunigung 
DELAY=1000 #anpassbar
ACCELERATION=10  # auch anpassbar

#Funktion zum Zeichnen des Spielfelds 
def draw_grid(screen,grid):
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            color=grid[y][x]
            if color:
                pygame.draw.rect(screen,color,(x*CELL_SIZE,y*CELL_SIZE,CELL_SIZE,CELL_SIZE),0)
            pygame.draw.rect(screen,BLACK,(x*CELL_SIZE,y*CELL_SIZE,CELL_SIZE,CELL_SIZE),1)

#Funktion damit eine Random tetromino (Figur im Spiel Tetris) erscheint
def get_random_tetromino():
    shape=random.choice(SHAPES)
    color=random.choice(COLORS)
    return shape,color

#Funktion, welche überprüft ob das Tetromino plaziert werden kann
def is_valid(grid,tetromino,tetromino_x,tetromino_y):
    for y in range(len(tetromino)):
        for x in range(len(tetromino[0])):
            if tetromino[x][y]:
                if (tetromino_x+x<0 or tetromino_x +x >=GRID_WIDTH
                        or tetromino_y+y >= GRID_HEIGHT or grid[tetromino_y+y][tetromino_x+x]):
                    return False
    return True
#Funktion um game over anzuzeigen.
def game_over(screen):
    font=pygame.font.Font(None,36)
    text=font.render("Game Over",True,WHITE)
    text_rect=text.get_rect(center=(WIDTH//2,HEIGHT//2))
    screen.blit(text,text_rect)
    pygame.display.update()

#Funktion um da Game wieder zu starten.
def restart_game(grid):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            grid[y][x] = 0
    return get_random_tetromino(), GRID_WIDTH // 2 - len(current_tetromino[0]) // 2, 0, False

def main():
    global current_tetromino,current_color,current_x,current_y,game_over








