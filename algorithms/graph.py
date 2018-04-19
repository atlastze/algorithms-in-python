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


class Vertex:
    """Lightweight vertex structure for a graph. If the vertex object is used in a
    priority queue (such as Dijkstra's algorithm, you should subclass this class and
    implement operator '__lt__'.

    """
    def __init__(self, tag):
        """Intialize a vertex with a tag."""
        self._tag = tag

    def __hash__(self):  # will allow vertex to be a map/set key
        return hash(id(self))

    def __lt__(self, other):
        raise NotImplementedError('__lt__ not implemented')

    def __repr__(self):
        return str(self._tag)

    
class Edge:
    """Lightweight edge/arrow structure for a graph. If an edge is added to a graph,
    then its endpoints are added to the graph.

    """
    __slots__ = '_head', '_tail', '_tag'

    def __init__(self, u, v, tag):
        """Intialize an edage with endpoints and a tag."""
        self._head = u
        self._tail = v
        self._tag = tag

    def endpoints(self):
        """Return (u,v) tuple for vertices u and v."""
        return (self._head, self._tail)

    def opposite(self, v):
        """Return the vertex that is opposite v on this edge."""
        if not isinstance(v, Graph.Vertex):
            raise TypeError('vertex type expected')
        if v is self._head:
            return self._tail
        elif v is self._tail:
            return self._head
        else:
            raise ValueError('vertex not incident to the edge')

    def __hash__(self):  # will allow edge to be a map/set key
        return hash((self._head, self._tail))

    def __repr__(self):
        return '{0} ({1}, {2})'.format(self._tag, self._head, self._tail)


class Digraph:
    """Representation of a directed graph using an adjacency map(map of maps):
        self._outgoing = { u: { v: edge for edge(u, v) in graph.edges}
                           for u in graph.vertices }
        self._incoming = { u: { v: edge for edge(v, u) in graph.edges}
                           for u in graph.vertices }
    """
    def __init__(self):
        """Create an empty graph (undirected, by default)."""
        self._outgoing = {}
        self._incoming = {}

    def __contains__(self, v):
        """Override 'in'(membership) operator."""
        if not isinstance(v, Vertex):
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
            text += '  '.join([str(e) for e in self.outgoing_edges(v)])
            text += '\n'
        text += '\nthe map of incoming edges:\n'
        for v in self.vertices():
            text += str(v) + ': '
            text += '  '.join([str(e) for e in self.incoming_edges(v)])
            text += '\n'
        text += '==================================='
        return text

    def _validate_vertex(self, v):
        """Verify that v is a Vertex of this graph."""
        if v not in self:
            raise ValueError('vertex not in the graph')

    def vertex_count(self):
        """Return the number of vertices in the graph."""
        return len(self._outgoing)

    def vertices(self):
        """Return an iteration of all vertices of the graph."""
        return self._outgoing.keys()

    def edge_count(self):
        """Return the number of edges in the graph."""
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total

    def edges(self):
        """Return an iteration of all edges of the graph."""
        result = set()  # avoid double-reporting edges of undirected graph
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())  # add edges to result
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
        """Return number of outgoing edges incident to vertex v in the graph."""
        self._validate_vertex(v)
        return len(self._outgoing[v])

    def in_degree(self, v):
        """Return number of incoming edges incident to vertex v in the graph."""
        self._validate_vertex(v)
        return len(self._incoming[v])

    def predecessors(self, v):
        """Vertices coming before a given vertex in a directed graph."""
        self._validate_vertex(v)
        return self._incoming[v].keys()

    def successors(self, v):
        """Vertices coming after a given vertex in a directed graph."""
        self._validate_vertex(v)
        return self._outgoing[v].keys()

    def outgoing_edges(self, v):
        """Return all outgoing edges incident to vertex v in the graph."""
        self._validate_vertex(v)
        return self._outgoing[v].values()

    def incoming_edges(self, v):
        """Return all incoming edges incident to vertex v in the graph."""
        self._validate_vertex(v)
        return self._incoming[v].values()

    def insert_vertex(self, v):
        """Insert and return a new vertex"""
        if v not in self:
            self._outgoing[v] = {}
            self._incoming[v] = {}
        return v

    def remove_vertex(self, v):
        """Remove a vertex."""
        self._validate_vertex(v)
        for u in self.vertices():
            # if not adjacent, do nothing
            self.remove_edge(u, v)
            self.remove_edge(v, u)
        self._incoming.pop(v)
        self._outgoing.pop(v)

    def insert_edge(self, e):
        """Insert and return an edge. If the endpoints of the edge are not
        vertices of the graph, then add them to the graph.

        """
        u, v = e.endpoints()
        if u not in self:
            self.insert_vertex(u)
        if v not in self:
            self.insert_vertex(v)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e
        return e

    def remove_edge(self, u, v):
        """Remove and return an edge from u to v. If not adjacent,
        do nothing.

        """
        e = self.edge(u, v)
        if e:
            self._outgoing[u].pop(v)
            self._incoming[v].pop(u)
        return e


class Graph(Digraph):
    """Class Graph, derived from class Digraph.
        self._incoming is redundant and identical to self._outgoing.

    """

    def insert_edge(self, e):
        """Insert and return an edge. If the endpoints of the edge are not
        vertices of the graph, then add them to the graph.

        """
        u, v = e.endpoints()
        if u not in self:
            self.insert_vertex(u)
        if v not in self:
            self.insert_vertex(v)
        self._outgoing[u][v] = e     # add (u, v)
        self._incoming[v][u] = e
        self._outgoing[v][u] = e     # add (v, u)
        self._incoming[u][v] = e
        return e

    def remove_edge(self, u, v):
        """Remove and return an edge, if not adjacent, do nothing."""
        Digraph.remove_edge(self, u, v)
        return Digraph.remove_edge(self, v, u)


if __name__ == '__main__':
    a = Vertex('A')
    b = Vertex('B')
    c = Vertex('C')
    d = Vertex('D')
    ab = Edge(a, b, 'AB')
    ba = Edge(b, a, 'BA')
    ac = Edge(a, c, 'AC')
    ca = Edge(c, a, 'CA')
    ad = Edge(a, d, 'AD')
    bc = Edge(b, c, 'BC')
    bd = Edge(b, d, 'BD')

    g = Digraph()
    g.insert_edge(ab)
    g.insert_edge(ba)
    g.insert_edge(ac)
    g.insert_edge(ca)
    g.insert_edge(ad)
    g.insert_edge(bc)
    g.insert_edge(bd)

    print('>> the original digraph:')
    print(g)

    print('\n>> remove ege (b->a):')
    g.remove_edge(b, a)
    print(g)

    print('\n>> remove vertex (a):')
    g.remove_vertex(a)
    print(g)
