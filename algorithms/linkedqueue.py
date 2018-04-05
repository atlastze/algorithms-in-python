from dlist import DoublyLinkedList


class EmptyQueueError(Exception):
    """EmptyQueueError is raised while accessing an empty queue."""
    def __str__(self):
        return 'an empty queue'


class LinkedQueue:
    """FIFO Queue implementation using a doubly linked list for storage."""

    def __init__(self):
        """Create an empty queue."""
        self._queue = DoublyLinkedList()

    def __len__(self):
        """Return the size of the queue."""
        return len(self._queue)

    def __str__(self):
        """Return information for users."""
        return str(self._queue)

    def __repr__(self):
        """Return information for developers."""
        return '< %s object at %s >' % (self.__class__,
                                   hex(id(self)))

    def is_empty(self):
        """Return True is the queue is empty."""
        return self._queue.is_empty()

    def enqueue(self, e):
        """Add element e to the back of the queue."""
        return self._queue.push_back(e)

    def dequeue(self):
        """Return and remove the element at the front of the queue."""
        if self.is_empty():
            raise EmptyQueueError
        return self._queue.pop_front()

    def first(self):
        """Return (do not remove) the element at the top of the queue."""
        if self.is_empty():
            raise EmptyQueueError
        return self._queue.first()


if __name__ == '__main__':
    q = LinkedQueue()
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
