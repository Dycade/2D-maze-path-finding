import sys
import numpy as np
import math

#find the possible next steps
def expand_node(current_node,map,row,col):
    current_x,current_y = current_node
    expand = dict()
    if current_y-1 >= 0 and  map[current_x][current_y-1] != 'X':
        expand['left'] = map[current_x][current_y-1]
    else:
        expand['left'] = None
    if current_x-1 >= 0 and map[current_x-1][current_y] != 'X':
        expand['up'] = map[current_x-1][current_y]
    else:
        expand['up'] = None
    if current_x+1 < row and map[current_x+1][current_y] != 'X':
        expand['down'] = map[current_x+1][current_y]
    else:
        expand['down'] = None
    if current_y+1 < col and map[current_x][current_y+1] != 'X':
        expand['right'] = map[current_x][current_y+1]
    else:
        expand['right'] = None
    return expand

#expand node in the order up down left and right
def next_move(current_node,dict):
    current_x,current_y = current_node
    possible_move = []
    if dict['up'] is not None:
        possible_move.append([current_x-1,current_y])
    if dict['down'] is not None:
        possible_move.append([current_x+1,current_y])
    if dict['left'] is not None:
        possible_move.append([current_x,current_y-1])
    if dict['right'] is not None:
        possible_move.append([current_x,current_y+1])
    return possible_move

#print out the map
def print_map(map):
    for row in map:
        for cell in row:
            print(cell, end=' ')
        print()

#calculate the cost
def path_cost(map,start,end):
    cost = 0
    if map[end[0]][end[1]] > map[start[0]][start[1]]:
        cost = 1 + map[end[0]][end[1]] - map[start[0]][start[1]]
    else:
        cost = 1
    return cost

#calculate estimated_distance for A*
def estimated_distance(start,end,heuristic):
    if heuristic == 'euclidean':
        distance = math.sqrt(sum([(v1-v2)**2 for v1, v2 in zip(start,end)]))
    if heuristic == 'manhattan':
        distance = sum(abs(v1-v2) for v1, v2 in zip(start,end))
    return distance

def BFS(map_location):
    with open(map_location) as f:
        row, col = [int(x) for x in next(f).split()] 
        start_x, start_y = [int(x)-1 for x in next(f).split()] 
        end_x, end_y = [int(x)-1 for x in next(f).split()] 
        map = []
        for line in f: 
            map.append(['X' if element == 'X' else int(element) for element in line.split()])

        trace ={}
        start_node = [start_x, start_y]
        visited_node = []
        visited_node.append(start_node)
        end_node = [end_x, end_y]
        current_position = 0
        while end_node not in visited_node:
            current_node = visited_node[current_position]
            fringe = next_move(current_node,expand_node(current_node,map,row,col))
            for node in fringe:
                if node not in visited_node:
                    visited_node.append(node)
                    trace[str(node)] = current_node
            current_position += 1
        
        path =[end_node]
        node = end_node
        while trace[str(node)] != [start_x, start_y]:
            node = trace[str(node)]
            path.append(node)
        path.append([start_x, start_y])


        for position in path:
            map[position[0]][position[1]] = '*'
        
        print_map(map)
        return map


def UCS(map_location):
    with open(map_location) as f:
        row, col = [int(x) for x in next(f).split()] 
        start_x, start_y = [int(x)-1 for x in next(f).split()] 
        end_x, end_y = [int(x)-1 for x in next(f).split()] 
        map = []
        for line in f: 
            map.append(['X' if element == 'X' else int(element) for element in line.split()])
        trace ={}
        start_node = [start_x, start_y]
        visited_node = []
        cost = {}
        visited_node.append(start_node)
        end_node = [end_x, end_y]
        cost[str(start_node)] = 0
        while end_node not in visited_node:
            current_node = eval(min(cost, key=cost.get))
            fringe = next_move(current_node,expand_node(current_node,map,row,col))
            for node in fringe:
                if node not in visited_node:
                    visited_node.append(node)
                    trace[str(node)] = current_node
                    cost[str(node)] = cost[str(current_node)]+path_cost(map,current_node,node)
            cost.pop(str(current_node))
            
        path =[end_node]
        node = end_node
        while trace[str(node)] != [start_x, start_y]:
            node = trace[str(node)]
            path.append(node)
        path.append([start_x, start_y])

        for position in path:
            map[position[0]][position[1]] = '*'

        print_map(map)

def A_star(map_location,heuristic):
    with open(map_location) as f:
        row, col = [int(x) for x in next(f).split()] 
        start_x, start_y = [int(x)-1 for x in next(f).split()] 
        end_x, end_y = [int(x)-1 for x in next(f).split()] 
        map = []
        for line in f: 
            map.append(['X' if element == 'X' else int(element) for element in line.split()])

        trace ={}
        heuristic = heuristic
        start_node = [start_x, start_y]
        visited_node = []
        cost = {}
        h_cost ={}
        visited_node.append(start_node)
        end_node = [end_x, end_y]
        cost[str(start_node)] = 0
        h_cost[str(start_node)] = 0
        current_node = eval(min(cost, key=cost.get))
        while current_node!= end_node:
            current_node = eval(min(cost, key=cost.get))
            visited_node.append(current_node)
            fringe = next_move(current_node,expand_node(current_node,map,row,col))
            for node in fringe:
                if node not in visited_node:
                    visited_node.append(node)
                    h_cost[str(node)] = h_cost[str(current_node)]+path_cost(map,current_node,node)
                    cost[str(node)] = h_cost[str(node)]+estimated_distance(node,end_node,heuristic)
                    trace[str(node)] = current_node
            cost.pop(str(current_node))
            if cost == {}:
                print('null')
                sys.exit()

                
        path =[end_node]
        node = end_node
        while trace[str(node)] != [start_x, start_y]:
            node = trace[str(node)]
            path.append(node)
        path.append([start_x, start_y])

        for position in path:
            map[position[0]][position[1]] = '*'

        print_map(map)


if __name__== "__main__":
    if sys.argv[2] == 'bfs':
        BFS(sys.argv[1])
    if sys.argv[2] == 'ucs':
        UCS(sys.argv[1])
    if sys.argv[2] == 'astar':
        A_star(sys.argv[1],sys.argv[3])

    



