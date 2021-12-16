#!/usr/bin/env python3
from queue import PriorityQueue
from dataclasses import dataclass
import numpy as np 

# Inspiration from https://www.pythonpool.com/a-star-algorithm-python/ but obviously numpy addition

weights = []
with open("input.txt", "r") as f:
# with open("sample.txt", "r") as f:
    weights = [list(map(int,list(line.strip()))) for line in f.readlines()]

@dataclass(frozen=True)
class Node:
    x: int
    y: int

class AStarGraph:

    def __init__(self, weights):
        self.weights = weights
        # print(weights.shape)
        # print(weights.shape[0] * weights.shape[1])
        
    def get_neighbors(self, n):
        neighbors = []
        if n.x > 0:
            neighbors.append(
                (Node(n.x-1, n.y), self.weights[n.x-1][n.y])
            )
        if n.x < len(self.weights) - 1:
            neighbors.append(
                (Node(n.x+1, n.y), self.weights[n.x+1][n.y])
            )
        if n.y > 0:
            neighbors.append(
                (Node(n.x, n.y-1), self.weights[n.x][n.y-1])
            )
        if n.y < len(self.weights[n.x]) - 1:
            neighbors.append(
                (Node(n.x, n.y+1), self.weights[n.x][n.y+1])
            ) 
        return neighbors

    def h(self, n):
        return 1

    def a_star(self, start:Node, stop:Node):

        open_list = set([start])
        closed_list = set()

        # Calculated distances from start to all other nodes
        dist_from_start = {}
        dist_from_start[start] = 0 

        # Adjacency mapping of all nodes
        adj_list = {}
        adj_list[start] = start

        while len(open_list) > 0:
            print(len(open_list), len(closed_list))
            n = None

            for v in open_list:
                if n == None or dist_from_start[v] + self.h(v) < dist_from_start[n] + self.h(n):
                    n = v

            if n == None:
                print("Path does not exist!")
                return None

            if n == stop:
                reconstructed_path = []

                while adj_list[n] != n:
                    reconstructed_path.append(n)
                    n = adj_list[n]

                reconstructed_path.append(start)
                reconstructed_path.reverse()

                # print('Path found: {}'.format(reconstructed_path))
                return reconstructed_path 

            for (m, weight) in self.get_neighbors(n):

                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    adj_list[m] = n
                    dist_from_start[m] = dist_from_start[n] + weight

                else:
                    if dist_from_start[m] > dist_from_start[n] + weight:
                        dist_from_start[m] = dist_from_start[n] + weight
                        adj_list[m] = n
 
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
 
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

# pt 1
graph = AStarGraph(weights)
path = graph.a_star(Node(0,0), Node(len(weights) - 1, len(weights[0]) - 1))

summed = 0
for n in path[1:]: 
    summed += weights[n.x][n.y]
print(summed)

# pt 2

row_len = len(weights) * 5
col_len = len(weights[0]) * 5

weights = np.array(weights)
full = np.zeros((row_len, col_len))
for r in range(5):
    for c in range(5):
        
        sub_weights = weights + (r + c)
        sub_weights[sub_weights > 9] -= 9

        # Figure out how to distribute the grid
        br = r * weights.shape[0]
        er = br + weights.shape[0]
        bc = c * weights.shape[1]
        ec = bc + weights.shape[1]
        full[br:er, bc:ec] = sub_weights

graph = AStarGraph(full)
path = graph.a_star(Node(0,0), Node(len(full) - 1, len(full[0]) - 1))

summed = 0
for n in path[1:]: 
    summed += full[n.x][n.y]
print(summed)
