"""
Starter code for Advent of Code 2021 Day #9

You must implement functions part1 and part2
"""

import sys
import os
import re


def part1(grid):
    """
    Solves Part 1 (see problem statement for more details)

    Parameter:
    - grid: a list of lists of integers representing
            a heightmap

    Returns an integer
    """
    ### Replace with your code
    total_sum = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            low = True
            if i > 0:
                low = low and grid[i][j] < grid[i-1][j]
            if i < len(grid)-1:
                low = low and grid[i][j] < grid[i+1][j]
            if j > 0:
                low = low and grid[i][j] < grid[i][j-1]
            if j < len(grid[0]) - 1:
                low = low and grid[i][j] < grid[i][j + 1]
            if low:
                total_sum += (grid[i][j] + 1)
    
    return total_sum

def part2(grid):
    """
    Solves Part 2 (see problem statement for more details)

    Parameter:
    - grid: a list of lists of integers representing
            a heightmap

    Returns an integer
    """
    def find_low(grid):
        lows = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                low = True
                if i > 0:
                    low = low and grid[i][j] < grid[i-1][j]
                if i < len(grid)-1:
                    low = low and grid[i][j] < grid[i+1][j]
                if j > 0:
                    low = low and grid[i][j] < grid[i][j-1]
                if j < len(grid[0]) - 1:
                    low = low and grid[i][j] < grid[i][j + 1]
                if low:
                    lows.append((i, j))
        return lows

    lows = find_low(grid)

    def size(i, j, seen=set()):
        if grid[i][j] == 9 or (i,j) in seen:
            return 0
        seen.add((i,j))
        s = 1
        neighbors = ((i-1, j), (i+1, j), (i, j-1), (i, j+1))
        for x, y in neighbors:
            if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]>grid[i][j]:
                s += size(x,y,seen)
        return s
    
    size_lst = []
    for low in lows:
        size_lst.append(size(low[0], low[1]))
    
    size_lst = sorted(size_lst)
    ### Replace with your code
    return size_lst[-1]*size_lst[-2]*size_lst[-3]


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
            grid.append([int(c) for c in line])

    print(f"Part 1:", part1(grid))
    
    # Uncomment the following line when you're ready to work on Part 2
    print(f"Part 2:", part2(grid))
