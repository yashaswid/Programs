class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None


def find(root,num):
    if root==None or root.data==num:
        return root
    elif num >root.data:
        return find(root.right,num)
    return find(root.left,num)


root=Node(1)
root.left=Node(2)
root.right=Node(3)
key=3
print(find(root,key))