import re 

nodes = list()
edges = dict()

with open('input.txt') as f:
    for line in f: 
        node, edge_list = re.match(r'^(.*?) bags contain (.*).$', line).groups()
        nodes.append(node)

        if edge_list != 'no other bags':
            for edge in edge_list.split(','):
                cnt, edge = re.match(r'\s*(\d+) (.*) bags?', edge).groups()
                if node not in edges: 
                    edges[node] = list()
                edges[node].append((edge, int(cnt)))
        else: 
            edges[node] = list()


def find_outer(node:str) -> set:

    contains_node = set()
    for n, edge_list in edges.items():
        if node in [n for n,c in edge_list]:
            contains_node.add(n)
    
    return contains_node

def total_bags(node:str) -> int:

    if len(edges[node]) == 0:
        return 1
    
    sum = 1
    for n, cnt in edges[node]:
        sum += cnt*total_bags(n)
    return sum 


def first_star(node:str) -> int: 

    contained_in = find_outer(node)

    # Make sure we don't have an infinite loop
    for i in range(1,100): 
        initial = len(contained_in)

        for n in contained_in:
            contained_in = contained_in.union(find_outer(n))
        
        if initial == len(contained_in):
            # We didn't add any more nodes, so we have the final list
            return len(contained_in)   
    
    return -1

def second_star(node: str) -> int: 
    # includes the current bag as well
    return total_bags(node) - 1

print(second_star('shiny gold'))
