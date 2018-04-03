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

    def __str__(self):
        """Return information for users."""
        s = '['
        p = self._sentinel._next
        while p is not self._sentinel:
            s += str(p._element)
            p = p._next
            if p is not self._sentinel:
                s += ', '
        s += ']'
        return s

    def __repr__(self):
        """Return information for developers."""
        return '%s (%r)' % (self.__class__, self._sentinel)

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0


    def insert_back(self, e, position = None):
        """Add element e at the back of position.
        NOTE: the default position is the last position.

        """
        if position is None:
            position = self._sentinel._prev
        elif not isinstance(position, self._Node):
            raise TypeError('requires a position type')
        node = self._Node(e, position, position._next)  # linked to neighbors
        position._next = node
        node._next._prev = node
        self._size += 1
        return node

    def remove_back(self, position):
        """Delete node at the position from the list and return its element."""
        if self.is_empty():
            raise EmptyListError
        answer = position._next._element
        position._next = position._next._next
        position._next._prev = position
        self._size -= 1
        return answer  # return deleted element

    def first_element(self):
        """Return the first element."""
        if self.is_empty():
            raise EmptyListError
        return self._sentinel._next._element

    def remove_first(self):
        """Delete the first node."""
        return self.remove_back(self._sentinel)


if __name__ == '__main__':
    dl = DoublyLinkedList()
    first = dl.insert_back(1)
    second = dl.insert_back(2)
    third = dl.insert_back(3, first)
    forth = dl.insert_back(4, third)
    print(dl)
