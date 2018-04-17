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
    """Representation of a simple graph using an adjacency map:
        graph = { u: { v: edge for edge(u, v) in graph.edges}
                  for u in graph.vertices }                    (map of maps)
    """

    # ------------------------- nested Vertex class -------------------------
    class Vertex:
        """Lightweight vertex structure for a graph."""

        def __init__(self, attribute):
            """Do not call constructor directly.
            Use Graph's insert_vertex(x).

            """
            self._attribute = attribute

        def __hash__(self):  # will allow vertex to be a map/set key
            return hash(id(self))

        def __str__(self):
            return str(self._attribute)

        def __repr__(self):
            return '< %s object at %s >' % (self.__class__, hex(id(self)))


    # ------------------------- nested Edge class -------------------------
    class Edge:
        """Lightweight edge structure for a graph."""
        __slots__ = '_origin', '_destination', '_attribute'

        def __init__(self, u, v, attribute):
            """Do not call constructor directly.
            Use Graph's insert_edge(u,v,x).

            """
            self._origin = u
            self._destination = v
            self._attribute = attribute

        def endpoints(self):
            """Return (u,v) tuple for vertices u and v."""
            return (self._origin, self._destination)

        def opposite(self, v):
            """Return the vertex that is opposite v on this edge."""
            if not isinstance(v, Graph.Vertex):
                raise TypeError('vertex type expected')
            if v is self._origin:
                return self._destination
            elif v is self._destination:
                return self._origin
            else:
                raise ValueError('vertex not incident to the edge')

        def __hash__(self):  # will allow edge to be a map/set key
            return hash((self._origin, self._destination))

        def __str__(self):
            return '({0} -- {1} : {2})'.format(self._origin,
                                               self._destination,
                                               self._attribute)

        def __repr__(self):
            return '< %s object at %s >' % (self.__class__, hex(id(self)))


    # ------------------------- Graph methods -------------------------
    def __init__(self, directed = False):
        """Create an empty graph (undirected, by default)."""
        self._outgoing = {}
        # only create second map for directed graph; use alias for undirected
        self._incoming = {} if directed else self._outgoing

    def __contains__(self, v):
        """Override 'in'(membership) operator."""
        if not isinstance(v, self.Vertex):
            raise TypeError('vertex type expected')
        if v in self.vertices():
            return True
        else:
            return False

    def __repr__(self):
        text = '============== GRAPH ==============\nvertices: '
        text += ', '.join([str(v) for v in self.vertices()])
        text += '\nedges:\n'
        text += '\n'.join([str(e) for e in self.edges()])
        text += '\n\nthe map of outgoing edges:\n'
        for v in self.vertices():
            text += str(v) + ': '
            text += '; '.join([str(e) for e in self.outgoing_edges(v)])
            text += '\n'
        text += '\nthe map of incoming edges:\n'
        for v in self.vertices():
            text += str(v) + ': '
            text += '; '.join([str(e) for e in self.incoming_edges(v)])
            text += '\n'
        text += '==================================='
        return text

    def _validate_vertex(self, v):
        """Verify that v is a Vertex of this graph."""
        if v not in self:
            raise ValueError('vertex not in the graph')

    def is_directed(self):
        """Return True if this is a directed graph; False if undirected."""
        # directed if maps are distinct
        return self._incoming is not self._outgoing

    def vertex_count(self):
        """Return the number of vertices in the graph."""
        return len(self._outgoing)

    def vertices(self):
        """Return an iteration of all vertices of the graph."""
        return self._outgoing.keys()

    def edge_count(self):
        """Return the number of edges in the graph."""
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        # for undirected graphs, make sure not to double-count edges
        return total if self.is_directed() else total // 2

    def edges(self):
        """Return an iteration of all edges of the graph."""
        result = set()  # avoid double-reporting edges of undirected graph
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())  # add edges to resulting set
        return result

    def edge(self, u, v):
        """Return the edge from u to v, or None if not adjacent."""
        self._validate_vertex(u)
        self._validate_vertex(v)
        if v in self._outgoing[u].keys():
            return self._outgoing[u][v]
        else:
            return None

    def out_degree(self, v):
        """Return number of (outgoing) edges incident to vertex v in the graph."""
        self._validate_vertex(v)
        return len(self._outgoing[v])

    def in_degree(self, v):
        """Return number of (incoming) edges incident to vertex v in the graph."""
        self._validate_vertex(v)
        return len(self._incoming[v])

    def outgoing_edges(self, v):
        """Return all (outgoing) edges incident to vertex v in the graph."""
        self._validate_vertex(v)
        return self._outgoing[v].values()

    def incoming_edges(self, v):
        """Return all (incoming) edges incident to vertex v in the graph."""
        self._validate_vertex(v)
        return self._incoming[v].values()

    def insert_vertex(self, attribute):
        """Insert and return a new vertex"""
        v = self.Vertex(attribute)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}  # need distinct map for incoming edges
        return v

    def remove_vertex(self, v):
        """Remove a vertex."""
        self._validate_vertex(v)
        for u in self.vertices():
            self.remove_edge(u, v)
            self.remove_edge(v, u)
        self._incoming.pop(v)
        if self.is_directed():
            self._outgoing.pop(v)   # if undirected, _outgoing is _incomming

    def update_vertex(self, v, attribute):
        """Update a vertex."""
        self._validate_vertex(v)
        v._attr = attribute

    def insert_edge(self, u, v, attribute):
        """Insert and return a new Edge from u to v with auxiliary element x.
        Raise a ValueError if u and v are not vertices of the graph.

        """
        if self.edge(u, v):
            return self.update_edge(u, v, attribute)
        e = self.Edge(u, v, attribute)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e    # if undirected, _incoming is _outgoing
        return e

    def remove_edge(self, u, v):
        """Remove and return an edge."""
        e = self.edge(u, v)
        if e:
            self._outgoing[u].pop(v)
            self._incoming[v].pop(u)
        return e

    def update_edge(self, u, v, attribute):
        """Update and return an edge."""
        e = self.edge(u, v)
        if e:
            e._attribute = attribute
        return e


class Digraph(Graph):
    """Class Digraph, derived from class Graph."""
    def __init__(self):
        Graph.__init__(self, True)


if __name__ == '__main__':
    dg = Digraph()
    a = dg.insert_vertex('A')
    b = dg.insert_vertex('B')
    c = dg.insert_vertex('C')
    d = dg.insert_vertex('D')
    ab = dg.insert_edge(a, b, 'AB')
    ba = dg.insert_edge(b, a, 'BA')
    ac = dg.insert_edge(a, c, 'AC')
    ca = dg.insert_edge(c, a, 'CA')
    ad = dg.insert_edge(a, d, 'AD')
    bc = dg.insert_edge(b, c, 'BC')
    bd = dg.insert_edge(b, d, 'BD')

    print('>> the original digraph:')
    print(dg)

    print('\n>> remove edge (b->a):')
    dg.remove_edge(b, a)
    print(dg)

    print('\n>> remove vertex (a):')
    dg.remove_vertex(a)
    print(dg)
