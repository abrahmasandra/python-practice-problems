"""
Starter code for Advent of Code 2019 Day #6

You must implement functions part1 and part2
"""

import sys
import os
import re
import math

class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges_to = {}
        self.dist = math.inf
    
    def add_edge_to(self, vertex):
        self.edges_to[vertex.name] = vertex
    
    def num_orbits(self):
        total_orbits = len(self.edges_to)
        for neighbor in self.edges_to.values():
            total_orbits += neighbor.num_orbits()
        return total_orbits


def part1(orbits):
    """
    Solves Part 1 (see problem statement for more details)

    Parameter:
    - orbits: a dictionary mapping an object name (e.g., "B")
              to the name of the object it orbits (e.g., "COM")

    Returns an integer
    """
    ### Replace with your code
    gr = {}
    for planet, sun in orbits.items():
        gr[planet] = gr.get(planet, Vertex(planet))
        gr[sun] = gr.get(sun, Vertex(sun))
        gr[planet].add_edge_to(gr[sun])
    
    total_orbits = 0
    for obj in gr.values():
        total_orbits += obj.num_orbits()

    return total_orbits

def path_length(you, san):
    visited = set()
    queue = [you]
    you.dist = 0

    while len(queue) > 0:
        curr = queue.pop(0)
        if curr.name == san.name:
            return curr.dist
        
        for n in curr.edges_to.values():
            if n not in visited:
                n.dist = curr.dist+1
                queue.append(n)
        visited.add(curr)

def part2(orbits):
    """
    Solves Part 2 (see problem statement for more details)

    Parameter:
    - orbits: a dictionary mapping an object name (e.g., "B")
              to the name of the object it orbits (e.g., "COM")

    Returns an integer
    """

    # create the undirected graph
    gr = {}
    for planet, sun in orbits.items():
        gr[planet] = gr.get(planet, Vertex(planet))
        gr[sun] = gr.get(sun, Vertex(sun))
        gr[planet].add_edge_to(gr[sun])
        gr[sun].add_edge_to(gr[planet])
    
    you, san = gr["YOU"], gr["SAN"]
    return path_length(you, san) - 2



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
        objs = [line.split(")") for line in lines]
        orbits = {}
        for p1, p2 in objs:
            orbits[p2] = p1

    print(f"Part 1:", part1(orbits))
    
    # Uncomment the following line when you're ready to work on Part 2
    print(f"Part 2:", part2(orbits))
