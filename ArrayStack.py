# Stack - LIFO using List

class Empty(Exception):
    pass

class ArrayStack:

    def __int__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    # push to the top of the stack
    def push(self, e):
        self._data.append(e)

    # return the top of the stack
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    # Remove and return the top element of the stack & end of list
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

