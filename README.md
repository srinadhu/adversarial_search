Adversarial search
======================

Introduction
------------

In this project designed agents for the classic version of Pacman, including ghosts and along the way implemented minimax and expectimax search and tried hand at evaluation function design. This is part of Pacman projects developed at [UC Berkeley](http://ai.berkeley.edu/multiagent.html). 


Directory Structure
-------------------

---multiagent

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [multiAgents.py](multiagent/multiAgents.py)

---[lab.pdf](lab.pdf)

---README.md

---[report.pdf](report.pdf)


Executing
---------

Then run the autograder using $python autograder.py

It gave us a score of 25/25.


Reflex Agent
------------
$python pacman.py -p ReflexAgent -l testClassic

$python pacman.py --frameTime 0 -p ReflexAgent -k 1

$python pacman.py --frameTime 0 -p ReflexAgent -k 2

Minimax
-------
$python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4

$python pacman.py -p MinimaxAgent -l trappedClassic -a depth=3

Alpha-Beta Pruning
------------------
$python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic

Expectimax
----------
$python pacman.py -p ExpectimaxAgent -l minimaxClassic -a depth=3

$python pacman.py -p AlphaBetaAgent -l trappedClassic -a depth=3 -q -n 10

$python pacman.py -p ExpectimaxAgent -l trappedClassic -a depth=3 -q -n 10

Evaluation Function
-------------------
$python autograder.py -q q5

Developed by
------------
[Sai Srinadhu K](https://www.linkedin.com/in/sai-srinadhu-katta-a189ab11b/), [Venkat Sainath T](https://www.linkedin.com/in/thota-sainath-236571118/).
