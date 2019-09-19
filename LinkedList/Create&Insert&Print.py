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


li=linkedList()
li.head=Node(1)
second=Node(20)
third=Node(30)
li.head.next=second
second.next=third
li.display()