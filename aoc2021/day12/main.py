#!/usr/bin/env python3
from collections import defaultdict
import sys


nodes = set()
edges = defaultdict(list)

with open("input.txt", "r") as f:
# with open("sample.txt", "r") as f:
# with open("sample2.txt", "r") as f:
# with open("sample3.txt", "r") as f:
    for l in f.readlines():
        n_a, n_b = l.strip().split('-')
        nodes.add(n_a)
        nodes.add(n_b)
        edges[n_a].append(n_b)
        edges[n_b].append(n_a)
        
# pt 1
paths = []
def dfs1(begin, end, visited, path):
    if begin.lower() == begin: 
        visited[begin] = True
    path.append(begin)

    if begin == end:
        paths.append(path.copy())
    else:
        for node in edges[begin]:
            if visited[node]== False:
                dfs1(node, end, visited, path)
    
    path.pop()
    visited[begin] = False

visited = { key: False for key in edges.keys() }
path = []
dfs1('start', 'end', visited, path)
print(len(paths))

# pt 2
paths = []
def dfs2(begin, end, visited, path):

    prev_double = visited['double']
    prev_visited = visited[begin]

    if begin.lower() == begin: 
        if begin in path or visited['double']: 
            visited[begin] = True

        visited['double'] = visited['double'] or (begin in path)
    path.append(begin)

    if begin == end:
        paths.append(path.copy())
    else:
        for node in edges[begin]:
            if node.lower() != node: 
                # No restrictions on uppercase values
                dfs2(node, end, visited, path)
            elif visited[node] == False and visited['double'] == False: 
                # We have a lowercase, we haven't seen a double yet, and we haven't visited this node
                dfs2(node, end, visited, path)
            elif visited[node] == False and visited['double'] and node not in path:
                # We have a lowercase, we have seen a double, so make sure we haven't seen it previously
                dfs2(node, end, visited, path)
            
    path.pop()
    visited[begin] = prev_visited
    visited['double'] = prev_double

visited = { key: False for key in edges.keys() }
visited['start'] = True
visited['double'] = False
path = []

dfs2('start', 'end', visited, path)
# for p in paths: 
#     print(','.join(p))
print(len(paths))
