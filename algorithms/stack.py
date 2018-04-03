class EmptyStackError(Exception):
    """EmptyStackError is raised while accessing an empty stack."""
    def __str__(self):
        return 'an empty stack'


class Stack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self._data = []

    def __len__(self):
        """Return the size of the stack."""
        return len(self._data)

    def __str__(self):
        """Return information for users."""
        return str(self._data)

    def __repr__(self):
        """Return information for developers."""
        return '%s (%r)' % (self.__class__, self._data)

    def is_empty(self):
        """Return True is the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Push element e to the top of the stack."""
        self._data.append(e)

    def pop(self):
        """Return and remove the element at the top of the stack."""
        if self.is_empty():
            raise EmptyStackError
        return self._data.pop()

    def top(self):
        """Return (do not remove) the element at the top of the stack."""
        if self.is_empty():
            raise EmptyStackError
        return self._data[-1]


if __name__ == '__main__':
    s = Stack()                      # contents: [ ]
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
