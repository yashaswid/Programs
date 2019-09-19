#  Write a function that counts the number of times a given int occurs in a Linked List
# Given a singly linked list and a key, count number of occurrences of given key in linked list.
# For example, if given linked list is 1->2->1->2->1->3->1 and given key is 1, then output should be 4.




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
    def countElement(self,key):
        temp=self.head
        count=0
        while(temp is not None):
            if temp.data==key:
                count+=1
            temp=temp.next
        return count

li=Linkedlist()
li.insert(1)
li.insert(2)
li.insert(1)
li.insert(22)
li.insert(23)
li.printList()
key=1
print("The occurance of the key is")
print(li.countElement(key))

