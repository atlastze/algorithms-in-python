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

import sys
sys.path.append('..')

from algorithms.graphalgorithms import *


if __name__ == '__main__':
    g = Digraph()
    s = g.insert_vertex(VertexAttribute('s', 0))
    t = g.insert_vertex(VertexAttribute('t'))
    x = g.insert_vertex(VertexAttribute('x'))
    y = g.insert_vertex(VertexAttribute('y'))
    z = g.insert_vertex(VertexAttribute('z'))
    g.insert_edge(s, t, 10)
    g.insert_edge(s, y, 5)
    g.insert_edge(t, x, 1)
    g.insert_edge(t, y, 2)
    g.insert_edge(x, z, 4)
    g.insert_edge(y, t, 3)
    g.insert_edge(y, x, 9)
    g.insert_edge(y, z, 2)
    g.insert_edge(z, s, 7)
    g.insert_edge(z, x, 6)
    bellman_ford(g, s)
    for v in g.vertices():
        print(v)