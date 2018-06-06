class Queue(object):
    def __init__(self,size=-1):
        self.__items = []
        self.__max_size = size

    def isEmpty(self):
        """ Return True if Queue is empty, else False """
        return self.__items == []

    def isFull(self):
        """ Return True is Queue is Full"""
            return self.size() == self.__max_size

    def enqueue(self, item):
        """ Insert item in the Queue at the end """
        if not self.isFull():
            self.__items.insert(0,item)
        else:
            raise ValueError("Queue is Full.Unable to add more values")

    def dequeue(self):
        """ Return First item of Queue """
        return self.__items.pop()

    def size(self):
        """ Return size of Queue """
        return len(self.__items)

    def __iter__(self):
        """ This function making Queue an Iterator """
        i=self.size()
        while i>0:
            yield self.__items[i-1]
            i-=1

