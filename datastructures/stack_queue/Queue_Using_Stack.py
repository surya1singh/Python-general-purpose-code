from stack import Stack

class Queue_Using_Stack(object):
    def __init__(self,size=-1):
        self.__max_size = size
        self.s1 = Stack(size=self.__max_size)
        self.s2 = Stack(size=self.__max_size)
        
    def isEmpty(self):
        """ Return True is Queue is empty, else False """
        return (self.s1.isEmpty() and self.s2.isEmpty())

    def isFull(self):
        """ return True is Queue is Full"""
        return self.size()==self.__max_size
    
    def enqueue(self, item):
        """ Insert item in the Queue at the end """
        if not self.isFull():
            self.s1.push(item)
        else:
            raise ValueError("Queue is Full.Unable to add more values")
    def dequeue(self):
        """ Return First item of Queue """
        if self.isEmpty():
            raise ValueError("Queue is Empty")
        elif self.s2.isEmpty():
            while not self.s1.isEmpty():
                self.s2.push(self.s1.pop())
        return self.s2.pop()

    def size(self):
        """ Return size of Queue """
        return self.s1.size() + self.s2.size()
