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
    g = Digraph()
    s = WeightedVertex('s')
    t = WeightedVertex('t')
    x = WeightedVertex('x')
    y = WeightedVertex('y')
    z = WeightedVertex('z')
    st = WeightedEdge(s, t, 'st', 6)
    sy = WeightedEdge(s, y, 'sy', 7)
    tx = WeightedEdge(t, x, 'tx', 5)
    ty = WeightedEdge(t, y, 'ty', 8)
    tz = WeightedEdge(t, z, 'tz', -4)
    xt = WeightedEdge(x, t, 'xt', -2)
    yx = WeightedEdge(y, x, 'yx', -3)
    yz = WeightedEdge(y, z, 'yz', 9)
    zs = WeightedEdge(z, s, 'zs', 2)
    zx = WeightedEdge(z, x, 'zx', 7)
    g.insert_edge(st)
    g.insert_edge(sy)
    g.insert_edge(tx)
    g.insert_edge(ty)
    g.insert_edge(tz)
    g.insert_edge(xt)
    g.insert_edge(yx)
    g.insert_edge(yz)
    g.insert_edge(zs)
    g.insert_edge(zx)
    bellman_ford(g, s)
    print(g)
    for v in g.vertices():
        print('{0}: {1}, from {2}'.format(v, v.distance, v.predecessor))