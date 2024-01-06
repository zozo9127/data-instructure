class dnode:
    def __init__(self, data) :
        self.data=data
        self.next=None
        self.prev=None
class linked_list :
        def __init__(self):
            self.head=None
        def display(self) :
            t=self.head
            while (t) :
                print(t.data, end='__>')  
                t=t.next
            print()   
        def add_in_first(self,d) :
            if self.head is None:
                return 
            else:
             n=dnode(d)   
             n.next=self.head
             self.head.prev=n
             self.head=n
        def add_in_the_end(self,d) :
            n1=dnode(d)   
            if (self.head==None): 
                self.head=n1
            else:
                while(self.head.next):
                    self.head.next=n1
                    n1.prev=self.head
                    n1=self.head
        def add_in_between(self,d,m) :
            n2=dnode(d)   
            t=self.head 
            while (t.data!=m):
                t=t.next
            n2.next=t.next
            n2.prev=t
            t.next=n2
            n2.next.prev=n2
            
        def del_first(self) :
            if (self.head==None)  :
                return False
            else:
                self.head=self.head.next
                self.head.prev=None
                
        def del_last(self)  :
            if (self.head==None) :
                return False
            else:
                t=self.head
                while (t.next!=None)  :
                    t=t.next
                t.next.prev=None
                t.prev=None
        def del_in_between(self,d) :
            n5=dnode(d)
            t=self.head
            while(t.data!=d)   :
                t=t.next
            t.next.prev=t.next
            t.prev=None
            t.next=None
            
            
            
                    
                
                       
                
            
            
            
                
                       
              
               
        