import sys

test_input="""L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
test_input = [list(l) for l in test_input.split()]

with open('input.txt') as f:
    input = [list(l) for l in f.read().splitlines()]

def print_map (map):
    for row in map:
        print("".join(row))

def count_adjacent(map, row, col): 
    adjacency = []

    first_row = row == 0
    last_row = row + 1 == len(map)

    first_col = col == 0
    last_col = col + 1 == len(map[row])

    if not first_row: 
        if not first_col: 
            # top left
            adjacency.append(map[row-1][col-1])
        # top center
        adjacency.append(map[row-1][col])
        if not last_col:
            # top right
            adjacency.append(map[row-1][col+1])
    
    if not first_col: 
        # mid left
        adjacency.append(map[row][col-1])
    if not last_col:
        # mid right
        adjacency.append(map[row][col+1])
    
    if not last_row: 
        if not first_col: 
            # bottom left
            adjacency.append(map[row+1][col-1])
        # bottom center
        adjacency.append(map[row+1][col])
        if not last_col:
            # bottom right
            adjacency.append(map[row+1][col+1])

    return adjacency.count('#')



def count_adjacent_updated(map, row, col): 
    adjacency = []

    num_rows = len(map)
    num_cols = len(map[0])

    # top left 
    r = row - 1
    c = col - 1
    while r >= 0 and c >= 0:
        if map[r][c] != '.':
            adjacency.append(map[r][c])
            # print('[%s,%s] tl found: %s' % (row, col, map[r][col]))
            break
        r -= 1
        c -= 1
    
    # top center
    r = row - 1
    while r >= 0:
        if map[r][col] != '.':
            adjacency.append(map[r][col])
            # print('[%s,%s] tc found: %s' % (row, col, map[r][col]))
            break
        r -= 1

    # top right 
    r = row - 1
    c = col + 1
    while r >= 0 and c < num_cols:
        if map[r][c] != '.':
            adjacency.append(map[r][c])
            # print('[%s,%s] tr found: %s' % (row, col, map[r][c]))
            break
        r -= 1
        c += 1
    
    # mid left
    c = col - 1
    while c >= 0: 
        if map[row][c] != '.':
            adjacency.append(map[row][c])
            # print('[%s,%s] ml found: %s' % (row, col, map[row][c]))
            break
        c -= 1

    # mid right
    c = col + 1
    while c < num_cols: 
        if map[row][c] != '.':
            adjacency.append(map[row][c])
            # print('[%s,%s] mr found: %s' % (row, col, map[row][c]))
            break
        c += 1
    
    # bottom left 
    r = row + 1
    c = col - 1
    while r < num_rows and c >= 0:
        if map[r][c] != '.':
            adjacency.append(map[r][c])
            # print('[%s,%s] bl found: %s' % (row, col, map[r][c]))
            break
        r += 1
        c -= 1
    
    # bottom center
    r = row + 1
    while r < num_rows:
        if map[r][col] != '.':
            adjacency.append(map[r][col])
            # print('[%s,%s] bc found: %s' % (row, col, map[r][c]))
            break
        r += 1

    # bottom right 
    r = row + 1
    c = col + 1
    while r < num_rows and c < num_cols:
        if map[r][c] != '.':
            adjacency.append(map[r][c])
            # print('[%s,%s] br found: %s' % (row, col, map[r][c]))
            break
        r += 1
        c += 1

    return adjacency.count('#')

def next_phase(map, adjacent_fx:callable, num_occupied_seats:int=4): 
    next = []
    for row in range(0, len(map)): 
        r = []
        for col in range(0, len(map[row])): 

            coord = map[row][col]
            
            if coord == '.':
                r.append(coord)
                continue
            
            adjacent = adjacent_fx(map, row, col)
            if coord == 'L' and  adjacent == 0:
                r.append('#')
            elif coord == '#' and adjacent >= num_occupied_seats: 
                r.append('L')
            else: 
                r.append(coord)
        
        next.append(r)
    
    return next

def is_equal(map1, map2):
    for m1, m2 in zip(map1, map2):
        if m1 != m2:
            return False
    return True

def count_type(map, type='#'):
    cnt = 0
    for row in map: 
        cnt += row.count(type)
    return cnt


# Part 1
prev = next_phase(input, count_adjacent, 4)
for round in range(1,200): 
    next = next_phase(prev, count_adjacent, 4)
    if is_equal(prev, next):
        print("We finally reached stabilization @ round %d" % round)
        print(count_type(next))
        break    

    prev = next

# Part 2
prev = next_phase(input, count_adjacent_updated, 5)
for round in range(1,200): 
    next = next_phase(prev, count_adjacent_updated, 5)
    if is_equal(prev, next):
        print("We finally reached stabilization @ round %d" % round)
        print(count_type(next))
        break    

    prev = next
