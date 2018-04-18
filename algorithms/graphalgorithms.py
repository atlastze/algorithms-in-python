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