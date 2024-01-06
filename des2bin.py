class stack():
    def __init__(self , limit = 10):
        self.stack = []
        self.limit = limit
    
    def peek (self):
        if (len(self.stack) <= 0):
            return -1
        else:
            return self.stack[len(self.stack) - 1]
    

    def pop(self):
        if (len(self.stack) <= 0):
            return -1
        else:
            return self.stack.pop()
        

    def push(self , data):
        if (len(self.stack) >= self.limit):
            return -1
        else:
            self.stack.append(data)


    def display(self):
        if (len(self.stack) <= 0):
            return -1
        else:
            for i in range (len(self.stack)):
                print (self.stack[i])


    def is_empty(self):
        if (len(self.stack) <= 0):
            return True
        else:
            return False
        
def des2bin(n):
    s = stack()
    while (n > 0):
        r = n % 2
        stack.push(r)
        n = n // 2
    b = " "
    while (not s.is_empty()):
        b = b + str(s.pop())
    return b