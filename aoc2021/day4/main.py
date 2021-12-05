#!/usr/bin/env python3
import numpy as np 

input = []
boards = []
with open("input.txt", "r") as f:
    input = list(map(int, f.readline().split(',')))

    while True:
        blank = f.readline()
        if not blank:
            break 

        board = np.zeros((5,5), dtype=int)
        for i in range(5):
            board[i] = list(map(int, f.readline().strip().split()))
        
        boards.append(board)

def has_won(board): 
    horiz = np.amax(board, axis=0)
    vert = np.amax(board, axis=1)

    return np.any(horiz <= 0) or np.any(vert <= 0)


won = False
board_cnt = np.zeros(len(boards), dtype=int)
last_num = np.zeros(len(boards), dtype=int)

for i, board in enumerate(boards):
    for idx, num in enumerate(input): 
        if len(board[board == num]):
            board_cnt[i] += 1
            board[board == num] *= -1
            board[board == num] -= 1
            if has_won(board):
                board_cnt[i] = idx
                last_num[i] = num
                break

# pt 1
index = np.argmin(board_cnt)
board = boards[index]
print(board)
summed = np.sum(board[board > 0])
print(summed, last_num[index])
print(summed * last_num[index])

# # pt 2
index = np.argmax(board_cnt)
board = boards[index]
print(board)
summed = np.sum(board[board > 0])
print(summed, last_num[index])
print(summed * last_num[index])
