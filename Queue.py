class Queue:

    def __init__(self , k):
        self.k = k
        self.queue = [None] * k
        self.front = -1
        self.rear = -1

    def disqueue(self):
        if self.front == -1:
            print("empty")
        for i in range (self.front , self.rear + 1):
            print(self.queue[i])

    def insqueue(self , data):
        if (self.rear == -1):
            self.front = 0
            self.rear = 0
        elif (self.rear + 1 == self.k):
            print ("is full")
        else:
            self.queue[self.rear] = data
            self.rear += 1

    def delqueue(self):
        if self.front == -1:
            print ("empty")
        elif (self.front == self.rear):
            t = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return t
        else:
            t = self.queue[self.front]
            self.front += 1
            return t