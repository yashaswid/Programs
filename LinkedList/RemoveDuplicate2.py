# Remove duplicates from an unsorted linked list
# Write a removeDuplicates() function which takes a list and deletes any duplicate nodes from the list. The list is not sorted.
# For example if the linked list is 12->11->12->21->41->43->21 then removeDuplicates() should convert the list to 12->11->21->41->43.


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
        s=set()
        while(temp.next is not None):
            if temp in s:
                temp=None
            else:
                s.add(temp)
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
