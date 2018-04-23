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

from algorithms.graph import *


if __name__ == '__main__':
    a = BaseVertex('A')
    b = BaseVertex('B')
    c = BaseVertex('C')
    d = BaseVertex('D')
    ab = BaseEdge(a, b, 'AB')
    ba = BaseEdge(b, a, 'BA')
    ac = BaseEdge(a, c, 'AC')
    ca = BaseEdge(c, a, 'CA')
    ad = BaseEdge(a, d, 'AD')
    bc = BaseEdge(b, c, 'BC')
    bd = BaseEdge(b, d, 'BD')

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
