#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 00:23:28 2020

@author: shiwanshu
"""

'''
A grid is considered solved if it is of the following configuration.

0 1 2
3 4 5
6 7 8

Sample Input

3
0
3
8
4
1
7
2
6
5

Sample Output

70
RIGHT
DOWN
...
...
...

The board given as input is

0 3 8
4 1 7
2 6 5
After RIGHT, the board's configuration is

3 0 8
4 1 7
2 6 5

Print all the moves made from the given configuration to the final solved board configuration.

'''

import sys
import queue


def distance(grid, val):
    t_row, t_col = divmod(val - 1, k)
    row, col = divmod(grid.index(val), k)
    #print()
    return abs(row - t_row) + abs(col - t_col)

def cost(grid):
    cost = 0
    
    for val in grid:
        cost += distance(grid, val)
    return cost

def adjacent_grids(grid):
    grids = []

    row, col = divmod(grid.index(0), k)

    #UP
    if row != 0:
        up = grid[:]
        old_pos = row * k + col
        new_pos = (row - 1) * k + col
        up[old_pos], up[new_pos] = up[new_pos], up[old_pos]
        grids.append(("UP", up))

    #DOWN
    if row != (k - 1):
        down = grid[:]
        old_pos = row * k + col
        new_pos = (row + 1) * k + col
        down[old_pos], down[new_pos] = down[new_pos], down[old_pos]
        grids.append(("DOWN", down))

    #RIGHT
    if col != (k - 1):
        right = grid[:]
        old_pos = row * k + col
        new_pos = row * k + col + 1
        right[old_pos], right[new_pos] = right[new_pos], right[old_pos]
        grids.append(("RIGHT", right))

    #LEFT
    if col != 0:
        left = grid[:]
        old_pos = row * k + col
        new_pos = row * k + col - 1
        left[old_pos], left[new_pos] = left[new_pos], left[old_pos]
        grids.append(("LEFT", left))

    return grids

def astar(grid):
    # Visit set 
    encountered = set()
    # Heap -- priority Queue
    q = queue.PriorityQueue()
    
    encountered.add(tuple(grid))
    q.put((cost(grid), [], grid))
    
    while not q.empty():
        already_cost, path, grid = q.get()
        
        if grid == target:
            return path
        
        adj = adjacent_grids(grid)

        for direction, grid in adj:
            if tuple(grid) not in encountered:
                p = path[:]
                p.append(direction)
                q.put((already_cost + cost(grid), p, grid))
                
            encountered.add(tuple(grid))

k = int(input())
print(k)
grid = []
target = list(range(k*k))
print(target)

for row in range(k*k):
    grid.append(int(input()))
print('initial grid passed',grid)
solution = astar(grid)
print(len(solution))