class EmptyStackError(Exception):
    """EmptyStackError is raised while accessing an empty stack."""
    def __str__(self):
        return 'an empty stack'


class LinkedStack(list):
    """LIFO Stack implementation using a singly linked list for storage."""

    #-------------------- nested _Node class ------------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):  # initialize node's fields
            self._element = element         # reference to user's element
            self._next = next               # reference to next node

    #--------------------------- Stack methods ----------------------------
    def __init__(self):
        """Create an empty stack."""
        self._head = None
        self._size = 0

    def __len__(self):
        """Return the size of the stack."""
        return self._size

    def __str__(self):
        """Return information for users."""
        s = '['
        p = self._head
        while p:
            s += str(p._element)
            p = p._next
            if p:
                s += ', '
        s += ']'
        return s

    def __repr__(self):
        """Return information for developers."""
        return '%s (%r)' % (self.__class__, self._head)

    def is_empty(self):
        """Return True is the stack is empty."""
        return self._size == 0

    def push(self, e):
        """Push element e to the top of the stack."""
        self._head = self._Node(e, self._head)
        self._size += 1

    def pop(self):
        """Return and remove the element at the top of the stack."""
        if self.is_empty():
            raise EmptyStackError
        answer = self._head._element
        self._head = self._head._next       # bypass the former top node
        self._size -= 1
        return answer

    def top(self):
        """Return (do not remove) the element at the top of the stack."""
        if self.is_empty():
            raise EmptyStackError
        return self._head._element


if __name__ == '__main__':
    s = LinkedStack()                      # contents: [ ]
    s.push(5)                        # contents: [5]
    s.push(3)                        # contents: [5, 3]
    print(len(s))                    # contents: [5, 3];    outputs 2
    print(s.pop())                   # contents: [5];       outputs 3
    print(s.is_empty())              # contents: [5];       outputs False
    print(s.pop())                   # contents: [ ];       outputs 5
    print(s.is_empty())              # contents: [ ];       outputs True
    s.push(7)                        # contents: [7]
    s.push(9)                        # contents: [7, 9]
    print(s.top())                   # contents: [7, 9];    outputs 9
    s.push(4)                        # contents: [7, 9, 4]
    print(len(s))                    # contents: [7, 9, 4]; outputs 3
    print(s.pop())                   # contents: [7, 9];    outputs 4
    s.push(6)                        # contents: [7, 9, 6]
    s.push(8)                        # contents: [7, 9, 6, 8]
    print(s.pop())                   # contents: [7, 9, 6]; outputs 8
    s.pop()                          # contents: [7, 9];
    s.pop()                          # contents: [7];
    s.pop()                          # contents: [ ];
    #s.pop()                          # EmptyStackError
