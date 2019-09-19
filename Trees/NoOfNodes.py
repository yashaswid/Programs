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

def NoOfNodes(root):
    if root==None:
        return 0
    else:
        return NoOfNodes(root.left)+NoOfNodes(root.right)+1

r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))
print(NoOfNodes(r))
