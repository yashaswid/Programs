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
maxnumber=0
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)
def max(root):
    global maxnumber
    if root==None:
        return maxnumber
    if root.data>maxnumber:
        maxnumber=root.data
    max(root.left)
    max(root.right)
    return maxnumber



r = Node(500)
insert(r,Node(30))
insert(r,Node(80))

print(max(r))
