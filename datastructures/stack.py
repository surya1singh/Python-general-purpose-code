class Stack(object):
    def __init__(self,size=-1):
        self.__max_size = size
        self.__items = []

    def push(self,item):
        """ push element into Stack """
        if not self.isFull():
            self.__items.append(item)
        else:
            raise ValueError("Stack is Full.Unable to add more values")

    def top(self):
        """ Return top element of stack"""
        if not self.isEmpty():
            return self.__items[-1]
        else:
            raise ValueError("Stack is Empty")

    def pop(self):
        """ Pop top element from stack """
        if not self.isempty():
            return self.__items.pop()
        else:
            raise ValueError("Stack is Empty")

    def isEmpty(self):
        """ Return True if Stack is empty"""
        return self.__items == []

    def isFull(self):
        """ Return True if Stack is full """
        return len(self.__items) == self.__max_size

    def size(self):
        """ Return number of elements in stack """
        return len(self.__items)

    def __iter__(self):
        """ Make Stack as Iterator """
        i = self.size()
        while i>0:
            yield self.__items[i-1]
            i-=1
