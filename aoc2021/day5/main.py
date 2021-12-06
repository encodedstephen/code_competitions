#!/usr/bin/env python3
import re 
import numpy as np 

def print_board(board:dict):
    print('   ', end=' ')
    for i in range(0,10): 
        print(i, end=' ')
    print() 
    print('   ' + '-'*20)
    for r in range(0,10):
        print('%-2d|' % r, end=' ')
        for c in range(0,10):
            print(board.get(r, {}).get(c, '.'), end=' ')
        print()

pattern = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')
input = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        x1, y1, x2, y2 = list(map(int, pattern.match(line).groups()))
        input.append((x1, y1, x2, y2))

# pt 1
board = {}
for coords in input:
    x1, y1, x2, y2 = coords
    # print(f'({x1}, {y1}) -> ({x2}, {y2})')
    if x1 == x2 or y1 == y2:
        if y1 == y2: 
            for i in range(min(x1, x2), max(x1, x2) + 1):
                if y1 not in board:
                    board[y1] = {}
                if i not in board[y1]:
                    board[y1][i] = 0
                
                board[y1][i] += 1
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1): 
                
                if i not in board:
                    board[i] = {}
                if x1 not in board[i]:
                    board[i][x1] = 0

                board[i][x1] += 1

cnt = 0
for row, cols in board.items(): 
    for col, val in cols.items():
        if val > 1:
            cnt += 1
print(cnt)

# pt 2
for coords in input:
    c1, r1, c2, r2 = coords
    
    if c1 != c2 and r1 != r2:
        col_dir = int((c1 > c2) * -1 + (c1 < c2) * 1)
        row_dir = int((r1 > r2) * -1 + (r1 < r2) * 1)
        for r in range(r1, r2 + row_dir, row_dir):
            offset = (r - r1) * row_dir
            c = c1 + col_dir * offset

            if r not in board: 
                board[r] = {c: 0}
            if c not in board[r]:
                board[r][c] = 0
            board[r][c] += 1


cnt = 0
for row, cols in board.items(): 
    for col, val in cols.items():
        if val > 1:
            cnt += 1
print(cnt)
