class Node():
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

def inOrder(root):
    if (root):
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)

def insertElement(temp,key):
    a=[]
    a.append(temp)

    while(len(a)):
        temp=a[0]
        a.pop(0)

        if(temp.left):
            a.append(temp.left)
        else:
            temp.left=Node(key)
        if(temp.right):
            a.append(temp.right)
        else:
            temp.left=Node(key)




root=Node(10)
root.left=Node(11)

root.left.left=Node(7)
root.right=Node(9)
root.right.left=Node(15)
root.right.right=Node(8)
print("Before Insertion")
inOrder(root)
print("Inserting the element 12")
key=12
insertElement(root,key)
print("after Insertion")
inOrder(root)

