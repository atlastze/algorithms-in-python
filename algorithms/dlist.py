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

    # -------------------------- nested Position class ------------------------
    class Position(_Node):
        """An abstraction representing the location of a single element.
        The position of an element is defined as the previous node's reference.

        """
        pass

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

    def _positions(self):
        """Generate the positions of the list."""
        p = self._sentinel
        while True:
            yield p
            p = p._next
            if p is self._sentinel:  # not the last node
                break

    def __str__(self):
        """Return information for users."""
        s = '['
        for p in self._positions():
            if p._next is not self._sentinel:  # p is a valid position
                s += str(p._next._element)
                if p._next._next is not self._sentinel: # not the last position
                    s += ', '
        s += ']'
        return s

    def __repr__(self):
        """Return information for developers."""
        return '< %s object at %s >' % (self.__class__,
                                   hex(id(self)))

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0


    def insert(self, position, e):
        """Add element e at the back of position.
        NOTE: the default position is the last position.

        """
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


if __name__ == '__main__':
    dl = DoublyLinkedList()
    first = dl.push_back(1)
    second = dl.push_back(2)
    third = dl.insert(first, 3)
    forth = dl.insert(third, 4)
    #dl.pop_front()
    print(dl)
