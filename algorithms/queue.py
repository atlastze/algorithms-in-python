class EmptyQueueError(Exception):
    """EmptyQueueError is raised while accessing an empty queue."""
    def __str__(self):
        return 'an empty queue'


class Queue:
    """FIFO Queue implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty queue."""
        self._data = []

    def __len__(self):
        """Return the size of the queue."""
        return len(self._data)

    def __str__(self):
        """Return information for users."""
        return str(self._data)

    def __repr__(self):
        """Return information for developers."""
        return '< %s.%s at %s>' % (self.__module__,
                                   self.__class__,
                                   hex(id(self)))

    def is_empty(self):
        """Return True is the queue is empty."""
        return len(self._data) == 0

    def enqueue(self, e):
        """Add element e to the back of the queue."""
        self._data.append(e)

    def dequeue(self):
        """Return and remove the element at the top of the queue."""
        if self.is_empty():
            raise EmptyQueueError
        return self._data.pop(0)

    def first(self):
        """Return (do not remove) the element at the front of the queue."""
        if self.is_empty():
            raise EmptyQueueError
        return self._data[0]


if __name__ == '__main__':
    q = Queue()
    q.enqueue(5)
    print(q)
    q.enqueue(3)
    print(q)
    print(len(q))
    q.dequeue()
    print(q)
    print(q.is_empty())
    q.dequeue()
    print(q)
    print(q.is_empty())
    #q.dequeue()
    q.enqueue(7)
    print(q)
    q.enqueue(9)
    print(q)
    print(q.first())
    q.enqueue(4)
    print(q)
    print(len(q))
    q.dequeue()
    print(q)
