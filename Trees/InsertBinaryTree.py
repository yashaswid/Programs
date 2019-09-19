class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

def insert(root,node):
    if root is None:
        return root
    else:
        if root.data<node.data:
            if root.right==None:
                root.right=node
            else:
                insert(root.right,node)
        else:
            if root.left==None:
                root.left=node

            else:
                insert(root.left,node)

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)

r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))
inOrder(r)
