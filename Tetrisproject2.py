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
SHAPES= [[1,1,1,1],
         [1,1],[1,1],
         [1,1,1],[0,1,0]
         [1,1,0],[0,1,1]
         [1,1,1],[0,0,1],
         [1,1,1],[0,1,1],
         [1,1,1],[1,0,0]]
#Farben der Formen 
COLORS=[CYAN,RED,ORANGE,PURPLE,YELLOW,GREEN,BLUE]