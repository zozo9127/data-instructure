class Stack:
    def __init__(self, limit=10) :
        self.stack=[]
        self.limit=limit
    def peek(self):
        if len(self.stack) ==0:
            return
        else:
            return self.stack[len(self.stack)-1]
    def pop(self)  :
        if len(self.stack) ==0:
            return
        else:
            return self.stack.pop()
    def push(self,data) :  
        if len(self.stack) >= self.limit:
            return False
        else:
            self.stack.append(data)
    def display(self):
            if len(self.stack) ==0:
             return False
            else:
                for i in self.stack:
                    print(i)
    def is_empty(self) :
          if len(self.stack) ==0:
             print('Is empty')    
def reverse(x) :
    s=Stack() 
    for i in range(len(x)):
        s.push(x[i])   
    for i in range(len(x)):
        x[i]=s.pop()        
    for i in range(len(x)):
        print(x[i])
reverse([1,2,3]) 

     
