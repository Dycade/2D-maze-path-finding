# Pathfinding System
This is a Python-based program that implements various algorithms to find the shortest path from start to end point in a 2D maze. The implemented algorithms include A*, Breadth-First Search (BFS), and Uniform-Cost Search (UCS).

# Cost of the path
The cost of a two adjacent points is 1 if we stay “level” or slide “downhill” and 1 plus the difference between the elevation of the two points.The total path cost would be the sum of all cost of a two adjacent points in the path.

## input map
input map text file formatted according to this example <br>
10 10<br>
1 1<br>
10 10<br>
1 1 1 1 1 1 4 7 8 X<br>
1 1 1 6 1 1 1 5 8 8<br>
4 1 1 1 1 1 1 4 6 7<br>
1 1 5 1 1 X 1 1 3 6<br>
1 1 1 1 1 X 1 9 1 1<br>
1 1 3 1 1 1 1 1 9 1<br>
6 1 1 1 1 X 1 1 1 2<br>
7 7 1 X X X 1 1 1 1<br>
8 8 1 1 1 1 1 1 1 1<br>
X 8 7 1 7 1 1 8 1 1<br>
The first line indicates the size of the map (rows by columns), while the second
and third line represent the start and end positions respectively. The map data
then follows, where all elevation values are integers from 0 to 9 inclusive and 'X' represent the road bloacks.


## Usage
1. Open terminal or command prompt and navigate to the directory where you cloned the repository.
2. edit the map.txt file as your wish
3. To run the program, enter command like:
```
 python pathfinder.py map.txt astar euclidean;
```
The first argument is the path of the map<br>
The second argument is the search algorithm to use choices are:bfs,ucs, and astar<br>
The third argument is the heuristic to use for A* search, choices are: uclidean and manhattan<br>
4. the out put would be similarly like:<br>
![output](https://github.com/Dycade/2D-maze-path-finding/assets/85650434/3066954b-fb61-4c2b-a3fa-3976ce32a98e)
where the * represent the finding path.
