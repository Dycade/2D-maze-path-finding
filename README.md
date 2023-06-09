# Pathfinding System
This is a Python-based program that implements various algorithms to find the shortest path from start to end point in a 2D maze. The implemented algorithms include A*, Breadth-First Search (BFS), and Uniform-Cost Search (UCS).

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
then follows, where all elevation values are integers from 0 to 9 inclusive. the cost of a path is the
sum of the costs between two adjacent points of the path, and the cost between
adjacent points is 1 plus the difference between the elevation of the two points if
we climb “uphill”, or simply 1 if we stay “level” or slide “downhill”.



## Usage
Open terminal or command prompt and navigate to the directory where you cloned the repository.
To run the program, enter:
python main.py
Select one of three pathfinding algorithms (A*, BFS, UCS) from menu options.
Input maze layout along with starting and ending points on console as prompted.
Program will output optimal path on maze graphically using Pygame graphics library.
Authors
Your Name
Acknowledgments
This project was inspired by my passion towards gaming industry and practical applications of machine learning techniques.
Special thanks go to my professor who provided me guidance throughout this project as well as fellow students who helped test different aspects of it.
Feel free to provide any feedback or suggestions!
