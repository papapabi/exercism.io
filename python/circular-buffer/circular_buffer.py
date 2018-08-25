from collections import deque


class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self._store = deque(maxlen=capacity)

    def __repr__(self):
        return '{classname}(capacity={capacity}, {elements})'.format(
            classname=self.__class__.__name__,
            capacity=self.capacity,
            elements=list(self._store))

    def __bool__(self):
        return bool(self._store)

    def read(self):
        if not self._store:
            raise BufferEmptyException('buffer empty')
        return self._store.popleft()

    def write(self, data):
        if len(self._store) == self.capacity:
            raise BufferFullException('buffer full')
        self._store.append(data)

    def overwrite(self, data):
        self._store.append(data)

    def clear(self):
        self._store.clear()
