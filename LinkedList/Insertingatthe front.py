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
    #this function add the new node to the front of the list
    def addNodefirst(self,data):
        temp=Node(data)
        temp.next=self.head
        self.head=temp

    # this function add the new node after a given node of the list
    def addNodemiddle(self,pre,data):
        temp=Node(data)
        temp.next=pre.next
        pre.next=temp

    # this function add the new node to the end of the list
    def addNodeend(self,data):
        temp=Node(data)
        x=self.head
        while(x.next):
            x=x.next
        x.next=temp



li=linkedList()
li.head=Node(1)
second=Node(20)
third=Node(30)
li.head.next=second
second.next=third
print("Before Addition")
li.display()
print("Adding new Node 40 to the front of the list")
li.addNodefirst(40)
li.display()
print("Addition of new node in the middle")
li.addNodemiddle(li.head.next,50)
li.display()
print("Addition of new node in the end")
li.addNodeend(100)
li.display()