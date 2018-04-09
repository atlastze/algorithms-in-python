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

class EmptyListError(Exception):
    """EmptyListError is raised while accessing an empty list."""
    def __str__(self):
        return 'an empty list'

class DoublyLinkedList:
    """A base class providing a circular doubly linked list representation.
        self._sentinel._next reference to the head of the list;
        self._sentinel._prev reference to the tail of the list;
    The position of an element is defined as the previous node's reference,
    that is self._sentinel is position of the first element.

    """

    # -------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_prev', '_next'  # streamline memory

        def __init__(self, element, prev, next):  # initialize node's fields
            self._element = element  # user's element
            self._prev = prev  # previous node reference
            self._next = next  # next node reference

    # -------------------------- DoublyLinkedList methods ---------------------
    def __init__(self):
        """Create an empty list."""
        self._sentinel = self._Node(None, None, None)
        self._sentinel._next = self._sentinel  # reference to itself
        self._sentinel._prev = self._sentinel  # reference to itself
        self._size = 0                         # number of elements

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def _isend(self, node):
        """Return True if the node is the last node."""
        return node._next is self._sentinel

    def _positions(self):
        """Generate the positions of the list.
        (including the sentinel and last node).

        """
        p = self._sentinel
        while True:
            yield p
            if self._isend(p):
                break
            else:
                p = p._next

    def __repr__(self):
        """Return information for developers."""
        return '< %s object at %s >' % (self.__class__,
                                   hex(id(self)))

    def __iter__(self):
        """Return iterator."""
        for p in self._positions():
            if not self._isend(p):  # not the last node
                yield p._next._element

    def __str__(self):
        """Return information for users."""
        return str(list(iter(self)))

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0

    def insert(self, position, e):
        """Insert an element at the position and return the node."""
        node = self._Node(e, position, position._next)  # linked to neighbors
        position._next._prev = node
        position._next = node
        self._size += 1
        return node

    def remove(self, position):
        """Delete node at the position from the list and return its element."""
        if self.is_empty():
            raise EmptyListError
        answer = position._next._element
        position._next = position._next._next
        position._next._prev = position
        self._size -= 1
        return answer  # return deleted element

    def first(self):
        """Return the first element."""
        return self._sentinel._next._element

    def last(self):
        """Return the last element."""
        return self._sentinel._prev._element

    def push_front(self, e):
        """Prepend element e to the list."""
        return self.insert(self._sentinel, e)

    def push_back(self, e):
        """Append element e to the list."""
        return self.insert(self._sentinel._prev, e)

    def pop_front(self):
        """Delete the first node."""
        if self.is_empty():
            raise EmptyListError
        return self.remove(self._sentinel)

    def pop_back(self):
        """Delete the last node."""
        if self.is_empty():
            raise EmptyListError
        return self.remove(self._sentinel._prev._prev)

    def search(self, e):
        """Return the position of the element in the list,
        otherwise, None if not exsists.

        """
        for p in self._positions():
            if not self._isend(p) and p._next._element == e: # not the back
                return p
        return None

    def indexof(self, e):
        """Return the index of the element in the list,
        otherwise, -1 if not exsists.

        """
        for i, p in enumerate(self._positions()):
            if not self._isend(p) and p._next._element == e: # not the back
                return i
        return -1


if __name__ == '__main__':
    dl = DoublyLinkedList()
    first = dl.push_back(1)
    second = dl.push_back(2)
    third = dl.insert(first, 3)
    forth = dl.insert(third, 4)
    #dl.pop_front()
    dl.remove(dl.search(3))
    print(dl)
    print(dl.indexof(3))
    print(dl.indexof(4))
