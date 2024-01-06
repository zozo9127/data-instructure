class Queue_c:

    def __init__(self , k):
        self.k = k
        self.queue =[None] * k
        self.front = -1
        self.rear = -1

    def insqueue_c(self , data , k):
        if ((self.rear + 1) % k == self.front):
            print ("full")
        elif (self.front == -1):
            self.front == 0
            self.rear == 0
            self.queue[self.rear] = data
        else:
            self.rear += -1
            self.queue[self.rear] = data

    def delqueue_c(self , k):
        if (self.front == -1):
            print ("empty")
        elif (self.front == self.rear):
            t = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return 1
        else:
            t = self.queue[self.front]
            self.front = (self.front + 1) % k
            return t

    def disqueue_c(self):
        if self.front == -1:
            print ("empty")
        elif (self.front < self.rear):
            for i in range (self.front , self.rear + 1):
                print (self.queue[i])
        else:
            for i in range (self.front , self.k):
                print(self.queue[i])
            for j in range (self.rear + 1):
                print (self.queue[j])     
