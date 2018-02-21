adversarial_search
======================

Introduction
------------

In this project designed agents for the classic version of Pacman, including ghosts and along the way implemented minimax and expectimax search and tried hand at evaluation function design. This is part of Pacman projects developed at [UC Berkeley](http://ai.berkeley.edu/multiagent.html). 

Directory Structure
-------------------


---[lab.pdf](lab.pdf)

---README.md

---[report.pdf](report.pdf)


Executing
---------

Then run the autograder using $python autograder.py

It gave us a score of 25/25.


Finding a Fixed Food Dot using Depth First Search
-------------------------------------------------
$python pacman.py -l tinyMaze -p SearchAgent

$python pacman.py -l mediumMaze -p SearchAgent

$python pacman.py -l bigMaze -z .5 -p SearchAgent

Breadth First Search
--------------------
$python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs

$python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5

$python eightpuzzle.py

Varying the Cost Function
-------------------------
$python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs

$python pacman.py -l mediumDottedMaze -p StayEastSearchAgent

$python pacman.py -l mediumScaryMaze -p StayWestSearchAgent

A* search
---------
$python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

Finding All the Corners
-----------------------
$python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

$python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem


Developed by
------------
[Sai Srinadhu K](https://www.linkedin.com/in/sai-srinadhu-katta-a189ab11b/), [Venkat Sainath T](https://www.linkedin.com/in/thota-sainath-236571118/).
