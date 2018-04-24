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
    a = Vertex('A')
    b = Vertex('B')
    c = Vertex('C')
    d = Vertex('D')
    e = Vertex('E')
    f = Vertex('F')
    g = Vertex('G')
    h = Vertex('H')

    ac = Edge(a, c, 'AC')
    ad = Edge(a, d, 'AD')
    bd = Edge(b, d, 'BD')
    bf = Edge(b, f, 'BF')
    cd = Edge(c, d, 'CD')
    ce = Edge(c, e, 'CE')
    df = Edge(d, f, 'DF')
    eg = Edge(e, g, 'EG')
    fg = Edge(f, g, 'FG')
    fh = Edge(f, h, 'FH')
    gh = Edge(g, h, 'GH')

    g = Digraph()
    g.insert_edge(ac)
    g.insert_edge(ad)
    g.insert_edge(bd)
    g.insert_edge(bf)
    g.insert_edge(cd)
    g.insert_edge(ce)
    g.insert_edge(df)
    g.insert_edge(eg)
    g.insert_edge(fg)
    g.insert_edge(fh)
    g.insert_edge(gh)

    print('>> the original digraph:')
    print(g)

    for v in toposort(g):
        print('{0}'.format(v))
