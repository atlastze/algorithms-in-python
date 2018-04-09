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
class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.key < other.key

    def __repr__(self):
        return '({0}, {1})'.format(self.key, self.value)


if __name__ == '__main__':
    items = [Item(4, 'Tokyo'),
             Item(1, 'Dehi'),
             Item(3, 'Shanghai'),
             Item(2, 'Sao Paulo'),
             Item(16, 'Mumbai'),
             Item(9, 'Mexico City'),
             Item(10, 'Beijing'),
             Item(14, 'Osaka'),
             Item(8, 'Cairo'),
             Item(7, 'New York')]
    print('>> The original items:\n{0}'.format(items))

    # Adaptable priority queue
    adaptable_items = [
        AdaptablePriorityQueue.AdaptableItem(item, i)
        for i, item in enumerate(items)
    ]
    item = adaptable_items[0]
    pq = AdaptablePriorityQueue(adaptable_items)
    print('>> The heap of items:\n{0}'.format(pq))
    pq.update(item, AdaptablePriorityQueue.AdaptableItem(Item(1, 'Dalian')))
    print('>> The heap after updating:\n{0}'.format(pq))