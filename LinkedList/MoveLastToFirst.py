# Write a function that moves the last element to the front in a given Singly Linked List.
# For example, if the given Linked List is 1->2->3->4->5, then the function should change the list to 5->1->2->3->4



class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head = None


    def insert(self,val):
        temp=Node(val)
        temp.next=self.head
        self.head=temp
    def print(self):
        temp=self.head
        while (temp):
            print(temp.data)
            temp=temp.next
    def move(self):
        temp=self.head
        pre=self.head
        # can be done in two ways
        # while(temp.next is not None): first method
        #     pre=temp
        #     temp=temp.next
        # value=temp.data
        # pre.next=None
        # li.insert(value)
        while(temp.next is not None):
            # second method
            pre=temp
            temp=temp.next
        pre.next = None
        temp.next=self.head
        self.head=temp


https://33souththird.activebuilding.com/


li =Linkedlist()
li.insert(6)
li.insert(5)
li.insert(4)
li.insert(3)
li.insert(2)
li.insert(1)
li.print()
print("Removing the duplicate values")
li.move()
li.print()
