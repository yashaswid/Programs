class Node:
    def __init__(self,val):
        self.data=val
        self.next=None



class Linkedlist():
    def __init__(self):
        self.head=None


    def insertNode(self,ex):

        temp=Node(ex)
        temp.next=self.head
        self.head=temp

    def display(self):

        temp=self.head
        while(temp.next):
            print(temp.data)
            temp=temp.next

    def delindex(self,position):
        temp = self.head
        if position==0:
            self.head=temp.next
            temp=None

        if self.head is None:
            return


        for i in range(position-1):
            temp=temp.next

        next=temp.next.next

        temp.next=None
        temp.next = next
li =Linkedlist()
li.head=Node(8)
li.insertNode(7)
li.insertNode(6)
li.insertNode(5)
li.insertNode(4)
li.insertNode(3)
li.insertNode(2)
li.insertNode(1)
li.display()
li.delindex(3)
print("After deletion")
li.display()

