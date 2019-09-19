class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def insert(root, node):
    if root is None:
        return root
    else:
        if root.data < node.data:
            if root.right == None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left == None:
                root.left = node

            else:
                insert(root.left, node)


# returns 1 if element found in the tree else 0
temp = 0


def foundElement(root, num):
    global temp
    if root == None:
        temp = 0
    if root.data==num:
        temp=1
    foundElement(root.left,num)
    foundElement(root.right,num)
    return temp


r = Node(50)
insert(r, Node(30))
insert(r, Node(80))
print(foundElement(r, 80))
