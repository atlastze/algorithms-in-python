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

class Graph:
    """Representation of a simple graph using an adjacency map and an edge map.
    vertices = { vertex: adjacency deges }
    edges = { (start_vertex, end_vertex): edges }
    """

    # ------------------------- nested Vertex class -------------------------
    class Vertex:
        """Lightweight vertex structure for a graph."""

        def __init__(self, vattr):
            """Do not call constructor directly. Use Graph's insert_vertex(x)."""
            self._vattr = vattr

        def __hash__(self):  # will allow vertex to be a map/set key
            return hash(id(self))

        def __str__(self):
            return str(self._vattr)

        def __repr__(self):
            return '< %s object at %s >' % (self.__class__, hex(id(self)))


    # ------------------------- nested Edge class -------------------------
    class Edge:
        """Lightweight edge structure for a graph."""
        __slots__ = '_origin', '_destination'

        def __init__(self, u, v, eattr):
            """Do not call constructor directly. Use Graph's insert_edge(u,v,x)."""
            self._origin = u
            self._destination = v
            self._eattr = eattr

        def endpoints(self):
            """Return (u,v) tuple for vertices u and v."""
            return (self._origin, self._destination)

        def opposite(self, v):
            """Return the vertex that is opposite v on this edge."""
            if not isinstance(v, Graph.Vertex):
                raise TypeError('vertex type expected')
            if v is self._origin:
                return self._destination
            elif v is  self._destination:
                return self._origin
            else:
                raise ValueError('vertex not incident to the edge')

        def __hash__(self):  # will allow edge to be a map/set key
            return hash((self._origin, self._destination))

        def __str__(self):
            return '({0} -> {1} : {2})'.format(self._origin,
                                          self._destination,
                                          self._eattr)

        def __repr__(self):
            return '< %s object at %s >' % (self.__class__, hex(id(self)))


    # ------------------------- Graph methods -------------------------
    def __init__(self, directed = False):
        """Create an empty graph (undirected, by default)."""
        self._vertices = {}
        self._edges = {}
        self._directed = directed

    def _validate_vertex(self, v):
        """Verify that v is a Vertex of this graph."""
        if not isinstance(v, self.Vertex):
            raise TypeError('vertex type expected')
        if v not in self.vertices():
            raise ValueError('vertex not in the graph')
        return True

    def is_directed(self):
        """Return True if this is a directed graph; False if undirected."""
        return self._directed

    def vertex_count(self):
        """Return the number of vertices in the graph."""
        return len(self._vertices)

    def vertices(self):
        """Return an iteration of all vertices of the graph."""
        return self._vertices.keys()

    def edge_count(self):
        """Return the number of edges in the graph."""
        total = len(self._edges)
        # for undirected graphs, make sure not to double-count edges
        return total if self.is_directed() else total // 2

    def edges(self):
        """Return an iteration of all edges of the graph."""
        return self._edges.values()

    def edge(self, u, v):
        """Return the edge from u to v, or None if not adjacent."""
        self._validate_vertex(u)
        self._validate_vertex(v)
        if (u, v) in self._edges.keys():
                return self._edges[(u, v)]
        elif not self._directed and (v, u) in self._edges.keys():
            return self._edges[(v, u)]
        else:
            return None

    def degree(self, v):
        """Return number of (outgoing) edges incident to vertex v in the graph."""
        self._validate_vertex(v)
        return len(self._vertices[v])

    def incident_edges(self, v, outgoing=True):
        """Return all (outgoing) edges incident to vertex v in the graph."""
        self._validate_vertex(v)
        return iter(self._vertices[v].values())

    def insert_vertex(self, vattr):
        """Insert and return a new vertex"""
        v = self.Vertex(vattr)
        self._vertices[v] = {}
        return v

    def insert_edge(self, u, v, eattr):
        """Insert and return a new Edge from u to v with auxiliary element x.
        Raise a ValueError if u and v are not vertices of the graph.

        """
        if self.edge(u, v) is not None:
            self._edges[(u, v)]._eattr = eattr
            return self._edges[(u, v)]
        e = self.Edge(u, v, eattr)
        self._vertices[u][v] = e
        self._edges[(u, v)] = e
        return e


if __name__ == '__main__':
    graph = Graph()
    a = graph.insert_vertex('A')
    b = graph.insert_vertex('B')
    edge = graph.insert_edge(a, b, 'AB')
    print(edge)
    print(repr(edge))
    print(graph.edge(a, b))

    print('edges: ')
    for edge in graph.edges():
        print(edge)
    print('vertices: ')
    for v in graph.vertices():
        print(v)

    edge = graph.insert_edge(a, b, 'CD')
    print(edge)
    print(repr(edge))