class Node:
    def __init__(self,x):
        self.prev=None
        self.data=x
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
    def insert_begining(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            nb=Node(data)
            nb.next=self.head
            nb.prev=None
            self.head=nb
    def insert_ending(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            nb=Node(data)
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=nb
            nb.next=None
            nb.prev=temp
    def display(self):
        if self.head is None:
            print("List is Empty")
        else:
            temp=self.head
            while temp:
                if temp.next!=None:
                    print(temp.data,end=" -> ")
                else:
                    print(temp.data,end="\n")
                temp=temp.next
            
obj=DLL()
s=input("Enter sequence:")
n=len(s)
for i in s:
    obj.insert_begining(int(i))
obj.display()
obj.insert_begining(10)
obj.display()