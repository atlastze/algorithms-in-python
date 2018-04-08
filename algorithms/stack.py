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
        return '< %s object at %s >' % (self.__class__,
                                   hex(id(self)))

    def __iter__(self):
        """Return iterator."""
        return iter(self._data)

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
