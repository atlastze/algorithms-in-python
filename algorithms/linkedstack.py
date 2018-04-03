from slist import SinglyLinkedList


class EmptyStackError(Exception):
    """EmptyStackError is raised while accessing an empty stack."""
    def __str__(self):
        return 'an empty stack'


class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""

    def __init__(self):
        """Create an empty stack."""
        self._stack = SinglyLinkedList()

    def __len__(self):
        """Return the size of the stack."""
        return len(self._stack)

    def __str__(self):
        """Return information for users."""
        return str(self._stack)

    def __repr__(self):
        """Return information for developers."""
        return '%s (%r)' % (self.__class__, self._stack)

    def is_empty(self):
        """Return True is the stack is empty."""
        return self._stack.is_empty()

    def push(self, e):
        """Push element e to the top of the stack."""
        return self._stack.push_front(e)

    def pop(self):
        """Return and remove the element at the top of the stack."""
        if self.is_empty():
            raise EmptyStackError
        return self._stack.pop_front()

    def top(self):
        """Return (do not remove) the element at the top of the stack."""
        if self.is_empty():
            raise EmptyStackError
        return self._stack.first_element()


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
