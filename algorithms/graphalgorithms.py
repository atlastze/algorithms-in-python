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

from .graph import *
from .queue import *
from .pqueue import *

def construct_path(start, end, predecessors):
    """Return a list of vertices comprising the directed path from start to end.
    Raise exception if there is no path.
    Arg:
        start: start vertex
        end: end vertex
        predecessors: a dictionary stores predecessor of vertices

    """
    if end not in predecessors:
        raise Exception('unable to reach the target')
    path = []
    current = end
    while currvent is not start:
        path.append(current)
        current = predecessors[current]
    path.reverse()
    return path


def depth_first_search(graph, start, predecessors):
    """Depth-first search algorithm
    Arg:
        graph: a directed or undirected graph
        start: start vertex
        predecessors: a dictionary stores predecessor of vertices when return

    """
    for v in graph.successors(start):
        if v not in predecessors:
            predecessors[v] = start
            depth_first_search(graph, v, predecessors)


def complete_depth_first_search(graph):
    """Depth-first search algorithm for all vertices"""
    forest = {}
    for v in graph.vertices():
        if v not in forest:
            forest[v] = None
            depth_first_search(graph, v, forest)
    return forest


def breadth_first_search(graph, start, predecessors):
    """Breadth-first search algorithm
    Arg:
        graph: a directed or undirected graph
        start: start vertex
        predecessors: a dictionary stores predecessor of vertices when return

    """
    queue = Queue()
    queue.enqueue(start)
    predecessors[start] = None
    while not queue.is_empty():
        u = queue.dequeue()
        for v in graph.successors(u):
            if v not in predecessors and v not in queue:
                queue.enqueue(v)
                predecessors[v] = u


def complete_breadth_first_search(graph):
    """Breadth-first search algorithm for all vertices"""
    forest = {}
    for v in graph.vertices():
        if v not in forest:
            forest[v] = None
            breadth_first_search(graph, v, forest)
    return forest


class VertexAttribute:
    def __init__(self, label, distance = float('inf'), predecessor = None):
        self._label = label
        self._distance = distance
        self._predecessor = predecessor

    def __lt__(self, other):
        return self._distance < other._distance

    def __repr__(self):
        return '<label:{0}, distance:{1}, predecessor:{2}>'.format(self._label,
                                                                   self._distance,
                                                                   self._predecessor)


def initialize_single_source(graph, src):
    """Initialization for shortest path problem."""
    for v in graph.vertices():
        v._attribute._distance = float('inf')
        v._attribute._predecessor = None
    src._attribute._distance = 0
    for v in graph.vertices():
        print(v)


def relax(graph, u, v):
    """Relaxation for shortest path problem."""
    e = graph.edge(u, v)
    if not e:
        return
    temp = u._attribute._distance + e._attribute
    if v._attribute._distance > temp:
        v._attribute._distance = temp
        v._attribute._predecessor = u


def bellman_ford(graph, src):
    """Bellman-Ford's algorithm of single source shortest path."""
    initialize_single_source(graph, src)
    for v in graph.vertices():
        print(v)
    for i in range(graph.vertex_count()-1):
        for e in graph.edges():
            relax(graph, e._head, e._tail)
        for v in graph.vertices():
            print(v)


def dijkstra(graph, src):
    """Dijkstra's algorithm of single source shortest path."""
    initialize_single_source(graph, src)
    pq = AdaptablePriorityQueue()
    while not pq.is_empty():
        u = pq.remove()
        print(u)
        for v in graph.successors(u):
            relax(graph, u, v)
            pq.update(v, v)
