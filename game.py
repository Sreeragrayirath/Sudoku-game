import pygame
import sys
from pygame.locals import *

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 540, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sudoku Game')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
RED = (255, 0, 0)

# Fonts
FONT = pygame.font.SysFont('Arial', 40)

# Board (0 means empty)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Draw grid
def draw_grid(win):
    win.fill(WHITE)
    for i in range(10):
        if i % 3 == 0 and i != 0:
            thickness = 4
        else:
            thickness = 1
        pygame.draw.line(win, BLACK, (i * 60, 0), (i * 60, 540), thickness)
        pygame.draw.line(win, BLACK, (0, i * 60), (540, i * 60), thickness)

# Draw numbers
def draw_numbers(win, board):
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                text = FONT.render(str(board[i][j]), True, BLACK)
                win.blit(text, (j * 60 + 20, i * 60 + 15))

# Main function
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        draw_grid(WINDOW)
        draw_numbers(WINDOW, board)
        pygame.display.update()

if __name__ == '__main__':
    main()
