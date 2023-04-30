from os import *
from sys import *
from collections import *
from math import *

class Deque:
    def __init__(self, size):
        self.q=[0]*size
        self.f=-1
        self.r=-1
        self.size=size
        # Write your code here
        pass

    # Pushes 'X' in the front of the deque. Returns true if it gets pushed into the deque, and false otherwise.
    def pushFront(self, x):
        if self.isFull():
            return False
        if self.isEmpty():
            self.f=0
            self.r=0
        else:
            self.f=(self.f-1)%self.size
        self.q[self.f]=x
        return True


    # Pushes 'X' in the back of the deque. Returns true if it gets pushed into the deque, and false otherwise.
    def pushRear(self, x):
        if self.isFull():
            return False
        if self.isEmpty():
            self.f=0
        self.r=(self.r+1)%self.size
        self.q[self.r]=x
        return True


    # Pops an element from the front of the deque. Returns -1 if the deque is empty, otherwise returns the popped element.
    def popFront(self):
        if self.isEmpty():
            return -1
        x=self.q[self.f]
        if self.f==self.r:
            self.f=-1
            self.r=-1
        else:
            self.f=(self.f+1)%self.size
        return x


    # Pops an element from the back of the deque. Returns -1 if the deque is empty, otherwise returns the popped element.
    def popRear(self):
        if self.isEmpty():
            return -1
        x=self.q[self.r]
        if self.f ==self.r:
            self.f=-1
            self.r=-1
        else:
            self.r=(self.r-1)%self.size
        return x

    # Returns the first element of the deque. If the deque is empty, it returns -1.
    def getFront(self):
        if self.isEmpty():
            return -1
        return self.q[self.f]

    # Returns the last element of the deque. If the deque is empty, it returns -1.
    def getRear(self):
        if self.isEmpty():
            return -1
        return self.q[self.r]

    # Returns true if the deque is empty. Otherwise returns false.
    def isEmpty(self):
        if self.f==-1:
            return True
        return False

    # Returns true if the deque is full. Otherwise returns false.
    def isFull(self):
        if(self.r+1)%self.size==self.f:
            return True
        return False
