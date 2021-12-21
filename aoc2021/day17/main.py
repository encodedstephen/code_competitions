#!/usr/bin/env python3
import re
import sys 

class Target:

    def __init__(self, x_start, x_end, y_start, y_end):
        self.x_start = x_start
        self.x_end = x_end
        self.y_start = y_start
        self.y_end = y_end

    def hit_target(self, x, y):
        return x >= self.x_start and x <= self.x_end \
            and y >= self.y_start and y <= self.y_end

    def passed_target(self, x, y):
        if self.y_end < 0: 
            return x >= self.x_end and y <= self.y_end
        else:
            return x >= self.x_end and y >= self.y_end

    def __repr__(self):
        return f"target: {self.x_start} <= x <= {self.x_end} AND {self.y_start} <= y <= {self.y_end}"

def step(x, y, v_x, v_y):
    x += v_x
    y += v_y
    if v_x > 0:
        v_x -= 1
    elif v_x < 0:
        v_x += 1
    else:
        # don't do anything if it's already 0
        pass
        
    v_y -= 1

    return x, y, v_x, v_y


with open("input.txt", "r") as f:
# with open("sample.txt", "r") as f:
    line = f.readline().strip()


x_start, x_end, y_start, y_end = re.search('target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)', line).groups()
target = Target(int(x_start), int(x_end), int(y_start), int(y_end))

max_v = {'x': 0, 'y':0, 'h': 0}
hit_target = set()
for xi in range(1, max(target.x_start, target.x_end) + 1):
    for yi in range(target.y_start, abs(target.y_start) + 1):
        
        start_vx, start_vy = (xi, yi)
        x, y, v_x, v_y = (0, 0, start_vx, start_vy)
        max_height = 0

        for i in range(1, 500):
            # print(f"Step {i}: ({x}, {y}) with velocity = ({v_x}, {v_y}).")
            x, y, v_x, v_y = step(x, y, v_x, v_y)
            max_height = max(max_height, y)
            
            if target.hit_target(x, y):
                # print(f"Maximum height for ({start_vx}, {start_vy}) = {max_height}\n")
                hit_target.add((start_vx, start_vy))
                if max_v['h'] <= max_height:
                    max_v = {'x': xi, 'y':yi, 'h': max_height}
                    # print(max_v)
                break
            elif target.passed_target(x, y):
                # print(f"We have passed the target @ point ({x}, {y})")
                break

        if x < target.x_start and y > target.y_end:
            print(f"We didn't go far enough! ({start_vx}, {start_vy}): ({x}, {y}) ({v_x}, {v_y})")
            sys.exit(1)



# pt 1
print(max_v)

# pt 2
print(len(hit_target))
