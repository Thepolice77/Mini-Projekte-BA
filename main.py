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
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)

# Tetromino-Formen
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[1, 1, 1], [0, 1, 1]]
]

# Farben der Tetrominos
COLORS = [CYAN, YELLOW, ORANGE, BLUE, GREEN, RED, PURPLE]

# Konstanten für Zeitverzögerung und Beschleunigung
INITIAL_DELAY = 1000
ACCELERATION = 10

# Funktion zum Zeichnen des Spielfelds
def draw_grid(screen, grid):
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            color = grid[y][x]
            if color:
                pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 0)
            pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

# Funktion zum Erstellen eines zufälligen Tetrominos
def get_random_tetromino():
    shape = random.choice(SHAPES)
    color = random.choice(COLORS)
    return shape, color

# Funktion zum Überprüfen, ob ein Tetromino im Spielfeld platziert werden kann
def is_valid_move(grid, tetromino, tetromino_x, tetromino_y):
    for y in range(len(tetromino)):
        for x in range(len(tetromino[0])):
            if tetromino[y][x]:
                if (tetromino_x + x < 0 or tetromino_x + x >= GRID_WIDTH or
                        tetromino_y + y >= GRID_HEIGHT or grid[tetromino_y + y][tetromino_x + x]):
                    return False
    return True

# Funktion zum Überprüfen und Löschen vollständiger Linien
def check_lines(grid):
    lines_to_clear = []
    for y in range(GRID_HEIGHT):
        if all(grid[y]):
            lines_to_clear.append(y)

    for y in lines_to_clear:
        grid.pop(y)
        grid.insert(0, [0] * GRID_WIDTH)

# Funktion zum Anzeigen der Game-Over-Nachricht
# Funktion zum Anzeigen der Game-Over-Nachricht
def show_game_over(screen, grid):
    pygame.init()
    font = pygame.font.Font(None, 36)  # Verwenden der Standardschriftart
    text = font.render("Game Over", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.update()
    time.sleep(2)  # Eine kurze Verzögerung, damit der Spieler das Ergebnis sehen kann
    return True


# Funktion zum Neustarten des Spiels
def restart_game(grid):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            grid[y][x] = 0

    current_tetromino, current_color = get_random_tetromino()
    current_x = GRID_WIDTH // 2 - len(current_tetromino[0]) // 2
    current_y = 0
    game_over = False

    return current_tetromino, current_x, current_y, game_over

# Hauptspiel
# Hauptspiel
def main():
    global current_tetromino, current_color, current_x, current_y, game_over, grid, screen  # Hinzufügen der globalen Variablen

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tetris")

    clock = pygame.time.Clock()

    grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]

    current_tetromino, current_color = get_random_tetromino()
    current_x = GRID_WIDTH // 2 - len(current_tetromino[0]) // 2
    current_y = 0

    game_over = False

    last_time = 0
    delay = INITIAL_DELAY

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if current_x > 0 and is_valid_move(grid, current_tetromino, current_x - 1, current_y):
                current_x -= 1

        if keys[pygame.K_RIGHT]:
            if current_x < GRID_WIDTH - len(current_tetromino[0]) and is_valid_move(grid, current_tetromino, current_x + 1, current_y):
                current_x += 1

        if keys[pygame.K_DOWN]:
            if current_y < GRID_HEIGHT - len(current_tetromino) and is_valid_move(grid, current_tetromino, current_x, current_y + 1):
                current_y += 1

        if keys[pygame.K_UP]:
            # Drehen des Tetrominos (90 Grad im Uhrzeigersinn)
            new_tetromino = [[current_tetromino[x][y] for x in range(len(current_tetromino))] for y in range(len(current_tetromino[0]))]
            if current_x + len(new_tetromino[0]) <= GRID_WIDTH and is_valid_move(grid, new_tetromino, current_x, current_y):
                current_tetromino = new_tetromino

        current_time = time.time()
        if current_time - last_time > delay / 1000:
            if not is_valid_move(grid, current_tetromino, current_x, current_y + 1):
                for y in range(len(current_tetromino)):
                    for x in range(len(current_tetromino[0])):
                        if current_tetromino[y][x]:
                            grid[current_y + y][current_x + x] = current_color

                check_lines(grid)  # Überprüfe und lösche vollständige Linien

                current_tetromino, current_color = get_random_tetromino()
                current_x = GRID_WIDTH // 2 - len(current_tetromino[0]) // 2
                current_y = 0

                # Spielende überprüfen
                if not is_valid_move(grid, current_tetromino, current_x, current_y):
                    game_over = show_game_over(screen, grid)  # Hier setzen Sie game_over auf True, wenn das Spiel vorbei ist

            current_y += 1
            last_time = current_time

        screen.fill(BLACK)
        draw_grid(screen, grid)

        # Zeichnen des aktuellen Tetrominos
        for y in range(len(current_tetromino)):
            for x in range(len(current_tetromino[0])):
                if current_tetromino[y][x]:
                    pygame.draw.rect(screen, current_color, ((current_x + x) * CELL_SIZE, (current_y + y) * CELL_SIZE, CELL_SIZE, CELL_SIZE), 0)
                pygame.draw.rect(screen, BLACK, (
                    (current_x + x) * CELL_SIZE, (current_y + y) * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

        pygame.display.update()
        clock.tick(5)

        # Beschleunigung der Tetrominos
        if delay > ACCELERATION:
            delay -= ACCELERATION

    show_game_over(screen, grid)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Starte das Spiel neu
                    current_tetromino, current_x, current_y, game_over = restart_game(grid)
                    delay = INITIAL_DELAY
                    last_time = 0
                    screen.fill(BLACK)
                    draw_grid(screen, grid)
                    pygame.display.update()
                    break

if __name__ == "__main__":
    current_tetromino, current_color, current_x, current_y, game_over, grid, screen = None, None, 0, 0, False, None, None
    main()



