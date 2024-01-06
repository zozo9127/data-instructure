class BTNode:
    def __init__(self,data, left=None, right=None):
        self.left=left
        self.right=right
        self.data=data
class Btree:
    def __init__(self,root) :
        self.root=None
    def Inorder(self,root):
        if root is None:
            return False
        else:
            self.Inorder(root.left)    
            print(root.data)  
            self.Inorder(root.right)   
    def Preorder (self,root) :
        if root is None:
            return False
        else:
         print(root.data)  
         self.Preorder(root.left)  
         self.Preorder(root.right)  
    def Postorder(self, root) :
        if root is None:
            return False
        else:
         self.Postorder(root.left)  
         self.Postorder(root.right)   
         print(root.data)  
class NodeBST:
    def __init__(self,data):
       self.key=data
       self.left=None
       self.right=None
def secondBST(root,k)  :
     if root is None :
        return print('Not Found')
     if k is root.key:
        return print('True')
     if k< root.key:
        return secondBST(root.left, k)
     return secondBST(root.right, k)
r=NodeBST(5)    
r.left=NodeBST(3)   
r.left.left=NodeBST(2)     
r.left.right=NodeBST(4)
r.right=NodeBST(8)
secondBST(r,81)

   