class EmptyListError(Exception):
    """EmptyListError is raised while accessing an empty list."""
    def __str__(self):
        return 'an empty list'

class SinglyLinkedList:
    """A base class providing a singly linked list representation.
    self._sentinel._next reference to the head of the list;
    The position of an element is defined as the previous node's reference,
    that is self._sentinel is position of the first element.

    """

    # -------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'  # streamline memory

        def __init__(self, element, next):  # initialize node's fields
            self._element = element  # user's element
            self._next = next  # next node reference

    # -------------------------- nested Position class ------------------------
    class Position(_Node):
        """An abstraction representing the location of a single element.
        The position of an element is defined as the previous node's reference.

        """
        pass

    # -------------------------- SinglyLinkedList methods ---------------------
    def __init__(self):
        """Create an empty list."""
        self._sentinel = self._Node(None, None)
        self._size = 0                         # number of elements

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def __str__(self):
        """Return information for users."""
        s = '['
        p = self._sentinel._next
        while p:
            s += str(p._element)
            p = p._next
            if p:
                s += ', '
        s += ']'
        return s

    def __repr__(self):
        """Return information for developers."""
        return '%s (%r)' % (self.__class__, self._sentinel)

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0


    def insert_back(self, e, position):
        """Add element e at the back of position.
        NOTE: the default position is the first position.

        """
        if not isinstance(position, self._Node):
            raise TypeError('requires a position type')
        node = self._Node(e, position._next)  # linked to neighbors
        position._next = node
        self._size += 1
        return node

    def remove_back(self, position):
        """Delete node at the position from the list and return its element."""
        if self.is_empty():
            raise EmptyListError
        answer = position._next._element
        position._next = position._next._next
        self._size -= 1
        return answer  # return deleted element

    def first_position(self):
        """Return the position of the first element."""
        if self.is_empty():
            raise EmptyListError
        return self._sentinel

    def first_element(self):
        """Return the first element."""
        return self.first_position()._next._element

    def last_position(self):
        """Return the position of the last element."""
        if self.is_empty():
            raise EmptyListError
        p = self._sentinel
        while p._next._next:
            p = p._next
        return p

    def last_element(self):
        """Return the last element."""
        return self.last_position()._next._element

    def push_front(self, e):
        """Prepend element e to the list."""
        return self.insert_back(e, self._sentinel)

    def push_back(self, e):
        """Append element e to the list."""
        p = None
        try:
            p = self.last_position()._next
        except EmptyListError:
            p = self._sentinel

        return self.insert_back(e, p)

    def pop_front(self):
        """Delete the first node."""
        return self.remove_back(self._sentinel)

    def pop_back(self):
        """Delete the last node."""
        p = self.last_position()._next
        return self.remove_back(p)


if __name__ == '__main__':
    sl = SinglyLinkedList()
    first = sl.push_back(1)
    second = sl.push_back(2)
    third = sl.insert_back(3, first)
    forth = sl.insert_back(4, third)
    sl.pop_front()
    print(sl)
