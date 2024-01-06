class dnode:

    def __init__(self , data):
        self.data = data
        self.next = None
        self.prev = None


class dlinkedlist:

    def __init__(self):
        self.head = None

    def display(self):
        t = self.head
        while (t != None):
            print (t.data , end="<-->")
            t = t.next
        print ('None')
    
    def addinstart(self , data):
        n = dnode(data)
        n.next = self.head
        self.head.prev = n
        self.head = n

    def addinend(self , data):
        n = dnode(data)
        if self.head != None :
            t = self.head
            while (t.next != None):
                t = t.next
            t.next = n
            n.prev = t
        else:
            self.head = n

    def addafter(self , m , data):
        n = dnode(data)
        t = self.head
        while (t.data != m):
            t = t.next
        n.next = t.next
        n.prev = t
        t.next = n
        n.next.prev = n


    def delfirst(self):
        if (self.head == None):
            return False
        self.head = self.head.next
        self.head.prev = None

    def dellast(self):
        if (self.head == None):
            return -1
        t = self.head
        while (t.next != None):
            t = t.next
        t.prev.next = None
        t.prev = None

    def delafter(self , d):
        t = self.head
        while (t.data != d):
            t = t.next
        t.next.prev = t.prev
        t.prev.next = t.next
        t.next = None
        t.prev = None
