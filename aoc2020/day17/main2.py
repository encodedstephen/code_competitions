import sys

def make_matrix(input): 
    matrix = []
    for line in input.splitlines(): 
        matrix.append([i for i in line ])
    return [[matrix]]

def next_round(matrix): 

    dim = (len(matrix), len(matrix[0]), len(matrix[0][0]), len(matrix[0][0][0]))
    # Add a dimension on both side: 
    next_dim = (dim[0] + 2, dim[1] + 2, dim[2] + 2, dim[3] + 2)

    print("Before dimension: ", dim)
    print("Next dimension: ", next_dim)

    # Build up the matrix
    m = []
    for w in range(0, next_dim[0]):
        cube = []
        for z in range(0, next_dim[1]):    
            square = []        
            for x in range(0, next_dim[2]): 
                row = []
                for y in range(0, next_dim[3]): 
                    if (w == 0 or z == 0 or x == 0 or y == 0) or \
                        (w == next_dim[0] - 1 or z == next_dim[1] - 1 or x == next_dim[2] - 1 or y == next_dim[3] - 1): 
                        row.append('.')
                    else:
                        row.append(matrix[w-1][z-1][x-1][y-1])
                square.append(row)
            cube.append(square)
        m.append(cube)

    print("Expanded Prior:")
    print_matrix(m)
    

    n = []
    for w in range(0, next_dim[0]): 
        cube = []
        for z in range(0, next_dim[1]):    
            square = []        
            for x in range(0, next_dim[2]): 
                row = []
                for y in range(0, next_dim[3]): 
                    
                    num_active = 0
                    for i in range(-1, 2):
                        for j in range(-1,2):
                            for k in range(-1,2):
                                for l in range(-1, 2):
                                    if i == 0 and j == 0 and k == 0 and l == 0: 
                                        continue

                                    # print("(%2d, %2d', %2d)" % (i, j, k))
                                    if w + i >= 0 and w + i < next_dim[0] \
                                        and z + j >= 0 and z + j < next_dim[1] \
                                        and x + k >= 0 and x + k < next_dim[2] \
                                        and y + l >= 0 and y + l < next_dim[3] \
                                        and m[w + i][z + j][x + k][y + l] == '#':
                                            num_active += 1
                    
                    if m[w][z][x][y] == '#':
                        if (num_active == 2 or num_active == 3):
                            row.append('#')
                        else: 
                            row.append('.')
                    elif m[w][z][x][y] == '.' and num_active == 3: 
                        row.append('#')
                    else:
                        row.append('.')
                square.append(row)
            cube.append(square)
        n.append(cube)

    dim = (len(n), len(n[0]), len(n[0][0]), len(n[0][0][0]))
    print("Next dimension (actual): ", dim)
    
    return n

def print_matrix (m):
    
    num_active = 0
    for i, w in enumerate(m): 
        for j, z in enumerate(w):
            print("w = %d, z = %d" % (i, j))
            for x in z: 
                for y in x: 
                    if y == '#':
                        num_active += 1
                    print(y, end= ' ')       
                print("")
            print("")
        print("")
    return num_active
                
    
test_input = """.#.
..#
###"""

with open('input.txt') as f:
    input = f.read()

next_cycle = make_matrix(input)
print_matrix(next_cycle)
for i in range(0, 6):
    next_cycle = next_round(next_cycle)
    print("After %d cycle:" % (i + 1))
    num_active = print_matrix(next_cycle)
    print(num_active)


