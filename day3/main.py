
with open('./input.txt') as f:
    maze = [list(l.strip('\n')) for l in f.readlines()]

num_rows = len(maze)
num_cols = len(maze[0]) # assumes all rows have same number of columns 

def num_trees(movement=(1,1), position=(0,0)): 
    ''' movement is (# down, # right) '''
    num_trees = 0
    
    while position[0] < num_rows - 1: 
        next_spot = (position[0] + movement[0], (position[1] + movement[1]) % num_cols)
        if maze[next_spot[0]][next_spot[1]] == '#':
            num_trees += 1

        position = next_spot

    return num_trees

def first_star ():
    print(num_trees((1,3)))

def second_star(): 
    slopes = [
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 1)
    ]
    combination = 1
    for slope in slopes: 
        combination *= num_trees(slope)

    print(combination)
