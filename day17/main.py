

def make_matrix(input): 
    matrix = []
    for line in input.splitlines(): 
        matrix.append([i for i in line ])
    return [matrix]

def next_round(matrix): 

    dim = (len(matrix), len(matrix[0]), len(matrix[0][0]))
    # Add a dimension on both side: 
    next_dim = (dim[0] + 2, dim[1] + 2, dim[2] + 2)

    print("Before dimension: ", dim)
    print("Next dimension: ", next_dim)

    # Build up the matrix
    m = []
    for z in range(0, next_dim[0]):    
        square = []        
        for x in range(0, next_dim[1]): 
            row = []
            for y in range(0, next_dim[2]): 
                if (z == 0 or x == 0 or y == 0) or \
                    (z == next_dim[0] - 1 or x == next_dim[1] - 1 or y == next_dim[2] - 1): 
                    row.append('.')
                else:
                    row.append(matrix[z-1][x-1][y-1])
            square.append(row)
        m.append(square)

    # print("Expanded Prior:")
    # print_matrix(m)

    n = []
    for z in range(0, next_dim[0]):    
        square = []        
        for x in range(0, next_dim[1]): 
            row = []
            for y in range(0, next_dim[2]): 
                
                num_active = 0
                for i in range(-1, 2):
                    for j in range(-1,2):
                        for k in range(-1,2):
                            if i == 0 and j == 0 and k == 0: 
                                continue
                            # print("(%2d, %2d', %2d)" % (i, j, k))
                            if z + i >= 0 and z + i < next_dim[0] \
                                and x + j >= 0 and x + j < next_dim[1] \
                                and y + k >= 0 and y + k < next_dim[2] \
                                and m[z + i][x + j][y + k] == '#':
                                    num_active += 1
                
                if m[z][x][y] == '#':
                    if (num_active == 2 or num_active == 3):
                        row.append('#')
                    else: 
                        row.append('.')
                elif m[z][x][y] == '.' and num_active == 3: 
                    row.append('#')
                else:
                    row.append('.')
                
            square.append(row)
        n.append(square)

    dim = (len(n), len(n[0]), len(n[0][0]))
    print("Next dimension (actual): ", dim)
    

    return n

def print_matrix (m):
    
    num_active = 0
    for i, z in enumerate(m): 
        print("Section %d" % i)
        for x in z: 
            for y in x: 
                if y == '#':
                    num_active += 1
                print(y, end= ' ')       
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

# print_matrix(next_round(matrix))


