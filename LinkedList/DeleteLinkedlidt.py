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
#delete a given list
    def deleteList(self):
        temp=self.head
        while(temp.next):
            prev=temp
            temp=temp.next
            prev=None

li=linkedList()
li.addNodefirst(40)
li.addNodefirst(30)
li.addNodefirst(50)
li.addNodefirst(60)
li.display()
print("After deletion of list")
li.deleteList()

