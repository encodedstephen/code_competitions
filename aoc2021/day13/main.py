#!/usr/bin/env python3
import numpy as np 

# Note - Inspiration for affine transformations taken from 
# https://medium.com/@benjamin.botto/mirroring-drawings-symmetry-with-affine-transformations-591d573667ec


pts = []
folds = []

with open("input.txt", "r") as f:
# with open("sample.txt", "r") as f:
    for line in f.readlines():
        if 'fold along' in line: 
            if 'x' in line: 
                folds.append(np.array([int(line.split('=')[1]), 0]))
            elif 'y' in line: 
                folds.append(np.array([0, int(line.split('=')[1])]))
        elif ',' in line:
            col, row = line.strip().split(',')
            pts.append((int(col), int(row)))
# pt 1

for i, fold in enumerate(folds): 
    new_pts = []
    for pt in pts: 

        if fold[0] == 0 and pt[1] > fold[1]: 
            # we have a y = ## fold
            tmp = pt - fold
            tmp = np.matmul(np.array([[1, 0],[0,-1]]), tmp)
            tmp += fold 
            new_pts.append(tuple(tmp))
        
        elif fold[1] == 0 and pt[0] > fold[0]:
            # we have a x = ## fold
            tmp = pt - fold
            tmp = np.matmul(np.array([[-1, 0],[0,1]]), tmp)
            tmp += fold 
            new_pts.append(tuple(tmp))

        else:
            new_pts.append(pt)
    
    if i == 0:
        # pt 1
        print(len(set(new_pts)))
    
    pts = new_pts

# pt 2
def print_paper(pts):
    cols = [pt[0] for pt in pts]
    rows = [pt[1] for pt in pts]

    paper = np.ndarray((max(rows) + 1, max(cols) + 1), dtype=object)
    paper.fill('.')
    for pt in pts: 
        paper[pt[1]][pt[0]] = '#'

    for row in paper:
        for col in row:
            print(col, end='')
        print()
    return paper

paper = print_paper(new_pts)
