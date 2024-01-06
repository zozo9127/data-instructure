class stack:

    def init(self,limit):
        self.stack = []
        self.limit = limit

    def peek(self):
        if len(self.stack) == 0:
            return False
        else:
            return self.stack[len(self.stack) - 1]
        
    def pop(self):
        if len(self.stack) == 0:
            return False 
        else:
            return self.stack.stack.pop() 
        
    def push(self, data):
        if len(self.stack) >= self.limit:
            return False 
        else:
            self.stack.append(data)  

    def display(self):
        if len(self.stack) == 0:
            return False    
        for i in self.stack:
            print(i)

    def is_empty(self)   :
        if len(self.stack) == 0:
         print("is empty!")  



def to_check(phrase):
    s1 = stack()
    n = []
    for i in phrase:
        n.append(i)
    for i in phrase:
        if i is '(' or '[' :
            t=s1.push(i)
        else:
            pass
    for i in phrase:
        if   i is ')' or ']'  :
            t1 = s1.push(i)
        else:
            pass
    if len(t) != len(t1) :
        return False 
    else:
        t0 = t1[::-1]
    if t0 != t1:
        print('your phrase in not valid')