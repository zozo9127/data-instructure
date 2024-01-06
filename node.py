class node:
    def __init__(self , d):
        self.data = d
        self.next = None

class linkedlist:

    def __init__(self):
        self.head = None

    def display(self):
        t = self.head
        while (t != None):
            print (t.data , end='-->')
            t = t.next
        print('None')

    def addfirst(self , newdata):
        n = node(newdata)
        n.next = self.head
        self.head = n
    
    def addlast(self , newdata):
        n = node(newdata)
        t = self.head
        if t == None:
            self.head = n
        else:
            while (t.next):
                t = t.next
            t.next = n

    def addafter(self , m , d):
        n = node(d)
        t = self.head
        if t == None:
            print ('list is empty')
            return -1
        while (t != None):
            if (t.data == m):
                n.next = t.next
                t.next = n
                return
        print ("doesn't exist")
        return -1

    def delfirst(self):
        if (self.head):
            self.head = self.head.next
        else:
            print ('list is empty')
            return -1
        
    def dellast(self):
        if (self.head == None):
            print ('list is empty')
            return -1
        else:
            t = self.head
            if (t.next == None):
                self.head = None
                return
            while (t.next.next != None):
                t = t.next
            t.next = None

    def delafter(self , m):
        t = self.head
        if (t == None):
            print ('list is empty')
            return -1
        while (t != m):
            t = t.next
            if (t == None):
                return -1
        t.next = t.next.next

    def reverse(self):
        