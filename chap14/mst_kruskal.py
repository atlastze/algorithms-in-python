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

from algorithms.graphalgo import *


if __name__ == '__main__':
    g = Graph()
    v = [Vertex(i+1) for i in range(9)]
    d = [4, 8, 7, 9, 10, 2, 1, 7]
    tag = [str(i) for i in range(14)]
    e = [Edge(v[i], v[i+1], tag[i], d[i]) for i in range(8)]
    e.append(Edge(v[0], v[7], tag[8], 8))
    e.append(Edge(v[7], v[1], tag[9], 11))
    e.append(Edge(v[8], v[2], tag[10], 2))
    e.append(Edge(v[8], v[6], tag[11], 6))
    e.append(Edge(v[2], v[5], tag[12], 4))
    e.append(Edge(v[3], v[5], tag[13], 14))
    for i in range(14):
        g.insert_edge(e[i])
    kruskal(g, v[0])
    print(g)
    for v in g.vertices():
        print('{0}: {1}, from {2}'.format(v, v.distance, v.predecessor))