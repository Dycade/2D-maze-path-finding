import random
import math
import sys
import pathfinder
import os

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

#remove the node that has already visited in the path
def remove_repeat(path):
    new = []
    for node in path:
        if node not in new:
            new.append(node)
    return new

#calculate cost between adjcant points
def path_cost(map,start,end):
    cost = 0
    if map[end[0]][end[1]] > map[start[0]][start[1]]:
        cost = 1 + map[end[0]][end[1]] - map[start[0]][start[1]]
    else:
        cost = 1
    return cost

#calculate total cost through the entire path
def total_cost(map,path):
    total = 0
    for i in range(len(path)-1):
        total = total + path_cost(map,path[i],path[i+1])
    return total

def random_BFS(start,end,map):
    row = len(map)
    col = len(map[0])
    trace ={}
    start_node = start
    visited_node = []
    visited_node.append(start_node)
    end_node = end
    current_position = 0
    while end_node not in visited_node:
        current_node = visited_node[current_position]
        fringe = next_move(current_node,expand_node(current_node,map,row,col))
        random.shuffle(fringe)
        for node in fringe:
            if node not in visited_node:
                visited_node.append(node)
                trace[str(node)] = current_node
        current_position += 1
    if trace == {}:
        return None
    else:
        path =[end_node]
        node = end_node
        while trace[str(node)] != start_node:
            node = trace[str(node)]
            path.append(node)
        path.append(start_node)
        path.reverse()
        return path


def random_local_adjust(p,d,map):
    path = remove_repeat(p)
    rand_pt = random.randrange(len(path))
    if rand_pt + d < len(path):
        new_path = random_BFS(path[rand_pt],path[rand_pt+d],map)
        if new_path:
            path[rand_pt : rand_pt + d] = random_BFS(path[rand_pt],path[rand_pt+d],map)
            return remove_repeat(path)
        else:
            return path
    else:
        new_path = random_BFS(path[rand_pt],path[-1],map)
        if new_path:
            path[rand_pt : -1] = random_BFS(path[rand_pt],path[-1],map)
            return remove_repeat(path)
        else:
            return path
   
def opt_path(P_0, T_in, T_fin, r,d,map):
    T = T_in
    P = P_0
    history =[]
    while T > T_fin:
        history.append([T,total_cost (map,P)])
        P_h = random_local_adjust(P,d,map)
        diff = total_cost (map,P) - total_cost (map,P_h)
        if diff > 0:
            P = P_h
        else:
            prob = random.random()
            if prob < math.exp(diff/T):
                P = P_h
        T = r*T
    return P,history

def find_next_pt(current_pt,map,history):
    row = len(map)
    col = len(map[0])
    if current_pt[1]-1 >= 0 and map[current_pt[0]][current_pt[1]-1] == '*':
        if [current_pt[0],current_pt[1]-1] not in history:
            return [current_pt[0],current_pt[1]-1]
    if current_pt[1]+1 < col and map[current_pt[0]][current_pt[1]+1] == '*':
        if [current_pt[0],current_pt[1]+1] not in history:
            return [current_pt[0],current_pt[1]+1]
    if current_pt[0]-1 >= 0 and map[current_pt[0]-1][current_pt[1]] == '*':
        if [current_pt[0]-1,current_pt[1]] not in history:
            return [current_pt[0]-1,current_pt[1]]
    if current_pt[0]+1 < row and map[current_pt[0]+1][current_pt[1]] == '*':
        if [current_pt[0]+1,current_pt[1]] not in history:
            return [current_pt[0]+1,current_pt[1]]

def read_path(path_found,start,end):
    temp_map = []
    for line in path_found: 
        temp_map.append(['X' if element == 'X' else ('*' if element == '*' else int(element)) for element in line])
    path = [start]
    next_pt = start
    while next_pt != end:
        next_pt= find_next_pt(next_pt,temp_map,path)
        path.append(next_pt)
    return path



    
if __name__== "__main__":
    with open(sys.argv[1]) as f:
        row, col = [int(x) for x in next(f).split()] 
        start_x, start_y = [int(x)-1 for x in next(f).split()] 
        end_x, end_y = [int(x)-1 for x in next(f).split()] 
        map = []
        for line in f: 
            map.append(['X' if element == 'X' else int(element) for element in line.split()])
    sys.stdout = open(os.devnull, 'w')
    path_map = pathfinder.BFS(sys.argv[1])
    sys.stdout = sys.__stdout__
    P_0 = read_path(path_map,[start_x, start_y],[end_x, end_y])
    optimal,history = opt_path(P_0, float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]),int(sys.argv[6]),map)
    
    for position in optimal:
        map[position[0]][position[1]] = '*'
    print_map(map)

    for eval in history:
        print("T = ",eval[0], ", cost = ",eval[1])



   




