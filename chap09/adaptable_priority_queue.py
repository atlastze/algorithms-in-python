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

from algorithms.pqueue import *


#  priority queue of user-defined objects
class Singer:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return '({0}: {1})'.format(self.name, self.priority)

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


if __name__ == '__main__':
    items = [Singer('Calvin Harris', 4),
             Singer('Chris Medina', 1),
             Singer('Sam Smith', 3),
             Singer('Martin Garrix', 2),
             Singer('Pharrelll Williams', 16),
             Singer('Craig David', 9),
             Singer('Ramin Djawadi', 10),
             Singer('Jason Mraz', 14),
             Singer('Steive Hoang', 8),
             Singer('John Denver', 7)]

    # Ordinary priority queue
    pq = PriorityQueue(items)
    print('>> The original order:') 
    while not pq.is_empty():
        print(pq.remove())
    print()

    # Adaptable priority queue
    pq = AdaptablePriorityQueue(items)
    pq.update(Singer('Sam Smith', 3), Singer('Daniel Powter', 5))
    print('>> The updated order:') 
    while not pq.is_empty():
        print(pq.remove())
