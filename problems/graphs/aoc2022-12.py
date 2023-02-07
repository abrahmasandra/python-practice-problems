"""
Starter code for Advent of Code 2022 Day #12

You must implement functions part1 and part2
"""

import sys
import os
import re
import math 

def bfs(start, end, grid):
        n, m = len(grid), len(grid[0])
        visited = set()
        visited.add(start)
        queue = [(start[0], start[1], 0)]
        while queue:
            i, j, num_steps = queue.pop(0)
            if (i, j) == end:
                return num_steps
            
            neighbors = ((i+1, j), (i-1, j), (i, j+1), (i, j-1))
            for row,col in neighbors:
                if 0<=row<n and 0<=col<m and grid[row][col]-grid[i][j]<=1 and (row,col) not in visited:
                    queue.append((row, col, num_steps+1))
                    visited.add((row, col))

def part1(grid):
    """
    Solves Part 1 (see problem statement for more details)

    Parameter:
    - grid: a list of lists of single-characters strings
            representing a heightmap

    Returns an integer
    """
    ### Replace with your code
    n, m = len(grid), len(grid[0])
    start, end = None, None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "S":
                start = (i, j)
                grid[i][j] = ord("a")
            elif grid[i][j] == "E":
                end = (i, j)
                grid[i][j] = ord("z")
            else:
                grid[i][j] = ord(grid[i][j])
            
    
    return bfs(start, end, grid), end 

def part2(grid, end):
    """
    Solves Part 2 (see problem statement for more details)

    Parameter:
    - grid: a list of lists of single-characters strings
            representing a heightmap

    Returns an integer
    """

    ### Replace with your code
    n, m = len(grid), len(grid[0])
    min_steps = math.inf
    for i in range(n):
        for j in range(m):
            if grid[i][j] == ord("a"):
                min_steps = min(min_steps, bfs((i,j), end, grid))
    
    return min_steps


############################################
###                                      ###
###      Do not modify the code below    ###
###                EXCEPT                ###
###    to comment/uncomment the calls    ###
###        to the functions above        ###
###                                      ###
############################################

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"USAGE: python3 {os.path.basename(sys.argv[0])} <INPUT FILE>")
        sys.exit(1)

    input_file = sys.argv[1]

    if not os.path.exists(input_file):
        print(f"ERROR: No such file: {input_file}")
        sys.exit(1)

    with open(input_file) as f:
        lines = f.read().strip().split("\n")
        grid = []
        for line in lines:
            grid.append([c for c in line])

    ans1, end = part1(grid)
    print(f"Part 1:", ans1)
    
    # Uncomment the following line when you're ready to work on Part 2
    print(f"Part 2:", part2(grid, end))
