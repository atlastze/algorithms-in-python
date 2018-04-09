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

class EmptyPQueueError(Exception):
    """EmptyPQueueError is raised while accessing an empty queue."""
    def __str__(self):
        return 'an empty priority queue'

class PriorityQueue:
    """A min-oriented priority queue implemented with a binary heap.
    Items should implement the following operators: __lt__, __str__, and __repr__.

    """
    #------------------------------ nonpublic behaviors ------------------------------
    def _parent(self, j):
        return (j-1) // 2

    def _left(self, j):
        return 2*j + 1

    def _right(self, j):
        return 2*j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._items)     # index beyond end of list?

    def _has_right(self, j):
        return self._right(j) < len(self._items)    # index beyond end of list?

    def _swap(self, i, j):
        """Swap the elements at indices i and j of array."""
        self._items[i], self._items[j] = self._items[j], self._items[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._items[j] < self._items[parent]:
            self._swap(j, parent)
            self._upheap(parent)             # recur at position of parent

    def _downheap(self, j):
        if self._has_left(j):
            child = self._left(j)
            if self._has_right(j):
                right = self._right(j)
                if self._items[right] < self._items[child]:
                    child = right
            if self._items[child] < self._items[j]:
                self._swap(j, child)
                self._downheap(child)    # recur at position of smaller child

    #------------------------------ public behaviors ------------------------------
    def __init__(self, items = []):
        """Create a new priority queue. By default, queue will be empty.
        If items are given, a heap of the items will be created.

        """
        self._items = items
        self._heapify()

    def _heapify(self):
      """Create a heap."""
      start = self._parent(len(self) - 1)
      for j in range(start, -1, -1):
          self._downheap(j)

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._items)

    def __str__(self):
        """Return information for users."""
        return str(self._items)

    def __repr__(self):
        """Return information for developers."""
        return '< %s object at %s >' % (self.__class__,
                               hex(id(self)))

    def is_empty(self):
        """Return True if heap is empty."""
        return len(self) == 0

    def insert(self, item):
        """Add an item to the priority queue."""
        self._items.append(item)
        self._upheap(len(self._items) - 1)     # upheap newly added position
        return item

    def min(self):
        """Return but do not remove item with minimum key.
        Raise EmptyPQueueError exception if empty.

        """
        if self.is_empty():
            raise EmptyPQueueError
        return self._items[0]

    def remove(self):
        """Remove and return item with minimum key.
        Raise EmptyPQueueError exception if empty.

        """
        if self.is_empty():
            raise EmptyPQueueError
        self._swap(0, len(self._items) - 1)     # put minimum item at the end
        item = self._items.pop()                 # and remove it from the list;
        self._downheap(0)                       # then fix new root
        return item


class AdaptablePriorityQueue(PriorityQueue):
    """A locator-based priority queue implemented with a binary heap."""

    # ------------------------------ nested AdaptableItem class ----------------------
    class AdaptableItem:
        """Entry of the adaptable priority queue, adding index as additional field used
        to track the position of the item in the heap.
        """
        __slots__ = '_item', '_index'

        def __init__(self, item, index = -1):
            self._item = item
            self._index = index

        def __repr__(self):
            return '{{{0}: {1}}}'.format(self._index, self._item)

        def __lt__(self, other):
            return self._item < other._item

    # ------------------------------ class methods ----------------------
    # override swap to record new indices
    def _swap(self, i, j):
        PriorityQueue._swap(self, i, j)       # perform the swap
        self._items[i]._index = i             # reset locator index (post-swap)
        self._items[j]._index = j             # reset locator index (post-swap)

    def _reheapify(self, j):
        if j > 0 and self._items[j] < self._items[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    def insert(self, adaptable_item):
        """Add a key-value pair to the priority queue."""
        adaptable_item._index = len(self._items)
        return PriorityQueue.insert(self, adaptable_item)

    def update(self, adaptable_item1, adaptable_item2):
        """Update the key and value for the entry identified by Locator loc."""
        index = adaptable_item2._index = adaptable_item1._index
        self._items[index] = adaptable_item2
        self._reheapify(index)
        return adaptable_item2


if __name__ == '__main__':
    #  priority queue of primitive objects
    pq = PriorityQueue([14, 5, 8, 25, 9, 11, 17,
                        16, 15, 4, 12, 6, 7, 23, 20])
    print(pq)