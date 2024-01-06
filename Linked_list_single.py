class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self) :
        self.head=None
    def display(self) :
        t=self.head
        while t:
            print(t.data, end='-->')   
            t=t.next
        print(None)   
    def add_in_first(self,d) : 
        n=node(d)     
        n.next=self.head
        self.head=n
    def add_in_last(self,d)  :
        n=node(d)  
        t=self.head
        if t:
            while (t.next!=None):
                t=t.next
            t.next=n
        else:
          self.head=n
    def add_after(self,d,m) :
        n=node(d)     
        t=self.head
        if t:
            while(t!=None) :
                if (t.data==m) :
                    n.next=t.next
                    t.next=n
                else:
                    print('m doesn\'t exist')   
        else:
            print('The list is empty')     
    def del_first(self) :
        t=self.head
        if t:
            t=t.next
        else:
            return False
    def del_last(self) :
        t=self.head
        if t:
         while t.next:
            t=t.next
         t.next=None
        else:
            return False
    def del_after(self,m) :
        t=self.head
        if t:
            while(t.data!=m) :
                t=t.next
            t.next=t.next.next
        else:
            return False     
              
        
            
                   
                           
                    
                
                
                 
         
    
                  
        
        