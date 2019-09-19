# Remove duplicates from a sorted linked list
# Write a function which takes a list sorted in non-decreasing order and deletes any duplicate nodes from the list. The list should only be traversed once.
# For example if the linked list is 11->11->11->21->43->43->60 then removeDuplicates() should convert the list to 11->21->43->60



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
    def removeDuplicate(self):
        temp=self.head
        if temp is None:
            return
        while(temp.next is not None):
            if (temp.data==temp.next.data):
                new=temp.next.next
                temp.next=None
                temp.next=new
            else:
                temp=temp.next
        return self.head


li =Linkedlist()
li.insert(12)
li.insert(11)
li.insert(11)
li.insert(10)
li.insert(10)
li.insert(10)
li.print()
print("Removing the duplicate values")
li.removeDuplicate()
li.print()
