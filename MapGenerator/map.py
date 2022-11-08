import numpy as np

scale = 1
board = np.zeros([scale*9, scale*16])
width = scale*(1920/16)
height = scale*(1080/9)

for i in range(1, 9 * scale - 1):
    for j in range(1, 16 * scale - 1):
        board[i][j] = 1

for i in range(2, 9 * scale - 2):
    for j in range(2, 16 * scale - 2):
        board[i][j] = 0

