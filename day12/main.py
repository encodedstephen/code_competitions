
import sys
import re
import math

test_input="""F10
N3
F7
R90
F11"""
test_input = [re.match('([NSEWLRF]{1})(\d+)', l).groups() for l in test_input.split()]


with open('./input.txt') as f:
    input = [re.match('([NSEWLRF]{1})(\d+)', l).groups() for l in f.read().splitlines()]

class Ship():

    def __init__(self):
        self.x = 0
        self.y = 0

        self.degrees = 0
    
    def position(self):
        return (self.x, self.y)
    
    def direction(self):
        return self.degrees

    def move(self, action:str, val:int):
        if action == 'F':
            radians = self.degrees * math.pi / 180.0
            self.x += val * math.cos(radians)
            self.y += val * math.sin(radians)
        elif action == 'N':
            self.y += val
        elif action == 'S':
            self.y -= val
        elif action == 'E':
            self.x += val
        elif action == 'W':
            self.x -= val
        elif action == 'L':
            self.degrees += val
        elif action == 'R':
            self.degrees -= val

        return (self.x, self.y)


ship = Ship()

# Part 1
for line in input:
    # print('%s: %s' % (ship.position(), ship.direction()))
    ship.move(line[0], int(line[1]))
print("Part 1 = ", round(sum([abs(num) for num in ship.position()])))


class WaypointShip(Ship):

    def __init__(self, x = 0, y = 0, wx = 10, wy = 1):
        self.x = x
        self.y = y
        self.wx = wx
        self.wy = wy

    def move(self, action:str, val:int):
        if action == 'F':
            for i in range(0, val):
                self.x += self.wx
                self.y += self.wy
        elif action == 'N':
            self.wy += val
        elif action == 'S':
            self.wy -= val
        elif action == 'E':
            self.wx += val
        elif action == 'W':
            self.wx -= val
        elif action == 'L':
            radians = val * math.pi / 180.0
            s = math.sin(radians)
            c = math.cos(radians)

            new_x = self.wx * c - self.wy * s
            new_y = self.wx * s + self.wy * c

            self.wx = round(new_x)
            self.wy = round(new_y)

        elif action == 'R':
            radians = val * math.pi / 180.0
            s = math.sin(radians)
            c = math.cos(radians)

            new_x = self.wx * c + self.wy * s
            new_y = -1 * self.wx * s + self.wy * c

            self.wx = round(new_x)
            self.wy = round(new_y)

        return (self.x, self.y)

# Part 2
ship = WaypointShip()
for line in input:
    # print('%s: %s' % (ship.position(), ship.direction()))
    # print(line)
    ship.move(line[0], int(line[1]))

# print(ship.position())
print("Part 2 = ", round(sum([abs(num) for num in ship.position()])))

