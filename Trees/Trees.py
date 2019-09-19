class Trees():
    def __init__(self,val):
        self.data=val
        self.right=None
        self.left=None
    def printPre(self,root):
        if (root):
            print(root.data)
            root.printPre(root.left)
            root.printPre(root.right)
    def printPost(self,root):
        if (root):
            root.printPost(root.left)
            root.printPost(root.right)
            print(root.data)
    def printIn(self, root):
        if (root):
            root.printIn(root.left)
            root.printIn(root.data)
            root.printIn(root.r)







root=Trees(1)
root.left=Trees(2)
root.right=Trees(3)
root.left.left=Trees(4)
root.left.right=Trees(5)

print("The Preorder Traversal is")
root.printPre(root)
print("The Postorder Traversal is")
root.printPost(root)
print("The Inorder Traversal is")
root.printIn(root)