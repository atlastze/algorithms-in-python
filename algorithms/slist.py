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

    # -------------------------- SinglyLinkedList methods ---------------------
    def __init__(self):
        """Create an empty list."""
        self._sentinel = self._Node(None, None)
        self._size = 0                         # number of elements

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def __isend(self, node):
        """Return True if the node is the last node."""
        return node._next is None

    def __positions(self):
        """Generate the positions of the list."""
        p = self._sentinel
        while True:
            yield p
            if self.__isend(p):
                break
            else:
                p = p._next

    def __repr__(self):
        """Return information for developers."""
        return '< %s object at %s >' % (self.__class__,
                                   hex(id(self)))

    def __iter__(self):
        """Return iterator."""
        for p in self.__positions():
            if not self.__isend(p):
                yield p._next._element

    def __str__(self):
        """Return information for users."""
        return str(list(iter(self)))

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0

    def insert(self, position, e):
        """Add an element at the specific position (after that node)."""
        node = self._Node(e, position._next)  # linked to neighbors
        position._next = node
        self._size += 1
        return node

    def remove(self, position):
        """Delete node at the specific position and return its element."""
        if self.is_empty():
            raise EmptyListError
        answer = position._next._element
        position._next = position._next._next
        self._size -= 1
        return answer  # return deleted element

    def first(self):
        """Return the first element."""
        if self.is_empty():
            raise EmptyListError
        return self._sentinel._next._element

    def last(self):
        """Return the last element."""
        if self.is_empty():
            raise EmptyListError
        positions = list(self.__positions())
        return self.positions[-2]._next._element

    def push_front(self, e):
        """Prepend element e to the list."""
        return self.insert(self._sentinel, e)

    def push_back(self, e):
        """Append element e to the list."""
        positions = list(self.__positions())
        return self.insert(positions[-1], e)

    def pop_front(self):
        """Delete the first node."""
        if self.is_empty():
            raise EmptyListError
        return self.remove(self._sentinel)

    def pop_back(self):
        """Delete the last node."""
        if self.is_empty():
            raise EmptyListError
        positions = list(self.__positions())
        return self.remove(positions[-2])

    def search(self, e):
        """Return the position of the element in the list.
        Return None if not exsists."""
        for p in self.__positions():
            if not self.__isend(p) and p._next._element == e: # not the back 
                return p
        return None

    def indexof(self, e):
        """Return the index of the element in the list.
        Return -1 if not exsists."""
        for i, p in enumerate(self.__positions()):
            if not self.__isend(p) and p._next._element == e: # not the back 
                return i 
        return -1 


if __name__ == '__main__':
    sl = SinglyLinkedList()
    first = sl.push_back(1)
    second = sl.push_back(2)
    third = sl.insert(first, 3)
    forth = sl.insert(third, 4)
    #sl.pop_front()
    sl.remove(sl.search(3))
    print(sl)
    print(sl.indexof(3))
    print(sl.indexof(4))
