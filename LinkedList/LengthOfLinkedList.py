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
#length a given list
    def lengthList(self):
        count=0
        temp=self.head
        while(temp.next):
            temp=temp.next
            count+=1
        return count+1

li=linkedList()
li.addNodefirst(40)
li.addNodefirst(30)
li.addNodefirst(50)
li.addNodefirst(60)
li.display()
print("No of Elements")
print(li.lengthList())

