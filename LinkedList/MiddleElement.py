class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,data):
        temp=Node(data)
        temp.next=self.head
        self.head=temp
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    def findMiddle(self):
        one=self.head
        two=self.head
        while(two.next is not None):
            one=one.next
            two=two.next.next
        print(one.data)


li=Linkedlist()
li.insert(1)
li.insert(2)

li.printList()
print("The middle number is")
li.findMiddle()
