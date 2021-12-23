#!/usr/bin/env python3
"""
SNAILFISH addition

To add two snailfish numbers, form a pair from the left and right parameters of the addition operator. For example, [1,2] + [[3,4],5] becomes [[1,2],[[3,4],5]].

To reduce a snailfish number, you must repeatedly do the first action in this list that applies to the snailfish number:

- If any pair is nested inside four pairs, the leftmost such pair explodes.
- If any regular number is 10 or greater, the leftmost such regular number splits.

Once no action in the above list applies, the snailfish number is reduced.

During reduction, at most one action applies, after which the process returns to the top of the list of actions. For example, if split produces a pair that meets the explode criteria, that pair explodes before other splits occur.

To explode a pair, the pair's left value is added to the first regular number to the left of the exploding pair (if any), and the pair's right value is added to the first regular number to the right of the exploding pair (if any). Exploding pairs will always consist of two regular numbers. Then, the entire exploding pair is replaced with the regular number 0.
"""
import json 
import sys
import math 

class Node:

    def __init__(self, value=None):
        self.parent = None
        self.left = None
        self.right = None
        self.value = value

    def has_value(self):
        return self.value != None

    def magnitude(self):
        if self.has_value():
            return self.value
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def __repr__(self):
        if self.value != None: 
            return f'{self.value}'
        return f'[{self.left},{self.right}]'

    def construct(paired):
        n = Node()
        l, r = paired

        if type(l) == int: 
            n.left = Node(l)
        else:
            n.left = Node.construct(l)
        n.left.parent = n
        
        if type(r) == int:
            n.right = Node(r)
        else:
            n.right = Node.construct(r)
        n.right.parent = n
        return n

    def explode(root):
        queue = [(root, 0)]
        while queue:
            n, depth = queue.pop()
            if depth >= 4:
                # Add left to the previous left value
                search = n
                while search.parent and search.parent.left == search: 
                    search = search.parent
                if search.parent: 
                    search = search.parent.left
                    while not search.has_value(): 
                        search = search.right
                    search.value += n.left.value

                # Add right to the next right value 
                search = n
                while search.parent and search.parent.right == search:
                    search = search.parent 
                if search.parent: 
                    search = search.parent.right
                    while not search.has_value(): 
                        search = search.left
                    search.value += n.right.value

                res = [n.left.value, n.right.value]
                n.left = None
                n.right = None
                n.value = 0
                return res
                    
            if n.right and not n.right.has_value():
                queue.append((n.right, depth+1))
            if n.left and not n.left.has_value():
                queue.append((n.left, depth+1))
        
        return False
    
    def split(root):
        queue = [(root, 0)]
        while queue: 
            n, depth = queue.pop()
            if n.value != None and n.value >= 10:
                n.left = Node(math.floor(n.value / 2.0))
                n.left.parent = n
                n.right = Node(math.ceil(n.value / 2.0))
                n.right.parent = n
                res = n.value
                n.value = None
                return res
        
            if n.right:
                queue.append((n.right, depth+1))
            if n.left:
                queue.append((n.left, depth+1))

        return False

    def add(node1, node2):
        head = Node()
        head.left = node1
        node1.parent = head

        head.right = node2
        node2.parent = head

        while True: 
            exploded = Node.explode(head)
            if exploded: 
                # print(" - exploded %s" % exploded)
                # print(head)
                continue

            split = Node.split(head)
            if split != False: 
                # print(" - split %s" % split)
                # print(head)
                continue

            # We didn't have any operation completed
            break
            
        return head

    

lines = []
with open("input.txt", "r") as f:
# with open("sample.txt", "r") as f:
    lines = [json.loads(line.strip()) for line in f.readlines()]

# pt 1
result = Node.construct(lines[0])
for line in lines[1:]: 
# for line in [[1,1]]:
    node = Node.construct(line)
    result = Node.add(result, node)
print(result)
print(result.magnitude())

# pt 2
max_sum = 0
cache = {}
for i, line1 in enumerate(lines):
    for j, line2 in enumerate(lines):
        if i == j: 
            continue 

        # We manipulate the nodes so we have to construct them each time
        # TODO: Go back and make Node.add return a new instance of Node, not manipulate the current
        node1 = Node.construct(line1)
        node2 = Node.construct(line2)
        result = Node.add(node1, node2)

        mag = result.magnitude()
        if max_sum < mag:
            max_sum = mag

print(max_sum)
