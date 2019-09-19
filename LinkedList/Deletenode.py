class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList():
    def __init__(self):
        self.head=None

    def display(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    #this function add the new node to teh front of the list
    def addNodefirst(self,data):
        temp=Node(data)
        temp.next=self.head
        self.head=temp
#delete a given node
    def deleteNode(self,key):
 #deletes if the first elemnt is only the key to be deleted
        temp=self.head
        if(temp.data==key):
            self.head=temp.next
            temp=None

        pre=self.head
        while(temp is not None):
            if (temp.data==key):
                break
            pre=temp
            temp=temp.next

        if (temp==None):
            return
        pre.next=temp.next
        temp=None






li=linkedList()
li.addNodefirst(40)
li.addNodefirst(30)
li.addNodefirst(50)
li.addNodefirst(60)
li.display()
print("After deletion, when found first")
li.deleteNode(60)
li.display()
print("Deletion by traversing")
li.deleteNode(30)
li.display()

