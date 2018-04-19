# Copyright (C) 2018, bruinspaw <bruinspaw@gmail.com>
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""Implementation of graph algorithms
Contents:
    Depth-first Search
    Breadth-first Search
    Bellman-Ford's algorithm
    Dijkstra's algorithm

References:
    Cormen, Leiserson et al, Introduction to Algorithms, 3rd, 2009

"""

from .graph import *
from .queue import *
from .pqueue import *


class AlgoVertex(Vertex):
    """Heavyweight vertex structure used for graph algorithms."""
    def __init__(self, tag):
        Vertex.__init__(self, tag)
        self.color = 'white'           # mark used in graph traversal
        self.predecessor = None        # previous vertex in a directed path
        self.distance = float('inf')   # distance from the source

    def __lt__(self, other):
        return self.distance < other.distance

class WeightedEdge(Edge):
    """Weighted edge structure."""
    def __init__(self, u, v, tag, distance):
        """Intialize an edage with endpoints and a tag."""
        Edge.__init__(self, u, v, tag)
        self.distance = distance


def initialize_graph_traversal(graph):
    """Initialization for graph traversal problem."""
    for v in graph.vertices():
        v.color = 'white'
        v.predecessor = None


def construct_path(start, end):
    """Return a list of vertices comprising the directed path from start
    to end. Return an empty list if there is no path.

    """
    path = []
    v = end
    while v:
        path.append(v)
        if v is start:    # found
            path.reverse()
            return path
        v = v.precedessor
    return []             # not found


def depth_first_search(graph, start):
    """Depth-first search algorithm"""
    start.color = 'gray'
    for v in graph.successors(start):
        if v.color == 'white':
            v.predecessor = start
            depth_first_search(graph, v)  # recursively search
    start.color = 'black'


def complete_depth_first_search(graph):
    """Depth-first search algorithm for all vertices"""
    initialize_graph_traversal(graph)
    for v in graph.vertices():
        if v.color == 'white':
            depth_first_search(graph, v)


def breadth_first_search(graph, start):
    """Breadth-first search algorithm
    Arg:
        graph: a directed or undirected graph
        start: start vertex
        predecessors: a dictionary stores predecessor of vertices when return

    """
    start.color = 'gray'
    queue = Queue()
    queue.enqueue(start)
    while not queue.is_empty():
        u = queue.dequeue()
        for v in graph.successors(u):
            if v.color == 'white':
                v.color = 'gray'
                v.predecessor = u
                queue.enqueue(v)
        u.color = 'black'


def complete_breadth_first_search(graph):
    """Breadth-first search algorithm for all vertices"""
    initialize_graph_traversal(graph)
    for v in graph.vertices():
        if v.color == 'white':
            breadth_first_search(graph, v)


def initialize_single_source(graph, src):
    """Initialization for shortest path problem."""
    for v in graph.vertices():
        v.distance = float('inf')
        v.predecessor = None
    src.distance = 0


def relax(graph, u, v):
    """Relaxation for shortest path problem."""
    e = graph.edge(u, v)
    if not e:
        return
    if v.distance > u.distance + e.distance:
        v.distance = u.distance + e.distance
        v.predecessor = u


def bellman_ford(graph, src):
    """Bellman-Ford's algorithm of single source shortest path."""
    initialize_single_source(graph, src)
    for i in range(graph.vertex_count()-1):
        for e in graph.edges():
            relax(graph, e._head, e._tail)


def dijkstra(graph, src):
    """Dijkstra's algorithm of single source shortest path."""
    initialize_single_source(graph, src)
    pq = AdaptablePriorityQueue()
    for v in graph.vertices():
        pq.insert(v)
    while not pq.is_empty():
        u = pq.remove()
        u.color = 'gray'
        for v in graph.successors(u):
            if v.color == 'white':
                relax(graph, u, v)
                pq.update(v, v)         # the first v used as a key
        u.color = 'black'
