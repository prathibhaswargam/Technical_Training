class Node:
    def __init__(self,u):
        self.data=u
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def insert_begining(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def insert_ending(self,data):
        nb=Node(data)
        if self.head is None:
            self.head=Node(data)
        else:
            nb=Node(data)
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=nb
            nb.next=None
    def search(self):
        s=int(input('\nEnter a num:'))
        temp=self.head
        while temp:
            if temp.data==s:
                print("Element is found")
                break
            else:
                temp=temp.next
        if temp==None:
            print("Element is not found")
    def middlenode(self,n):
        x=n//2
        temp=self.head
        for _ in range(0,x):
            temp=temp.next
        print("\nMiddle Node:",temp.data)
    def longestlength(self,n):
        temp=self.head
        long=0
        c=1
        while temp and temp.next and n >= 0:
            if temp.next.data== temp.data +1:
                c += 1
                if c > long:
                    long = c
            else:
                c = 1
            temp = temp.next
            n -= 1
        if c>long:
            long=c
        print("\nLongest sequence:", long)
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
    def bubblesort(self):
        t=self.head
        c=0
        while t.next!=None:
            f=0
            t1=t.next
            while t1!=None:
                if t.data>t1.data:
                    f=1
                    c+=1
                    t.data,t1.data=t1.data,t.data
                t1=t1.next
            t=t.next
            if f==0:
                break
        print(c)
        self.display()
    def subs(self):
        t = self.head
        while(t != None):
            t1 = t.next
            while(t1 != None):
                print(t.data,t1.data)
                t1= t1.next
            t = t.next
            
    def num(self,n):
        t=self.head
        while t.next!=None:
            t=t.next
        t1=self.head
        t2=t
        if n%2==0:
            while i<j:
                a[i],a[j]=a[j],a[i]
                i+=1
                j-=1
        else:
            while i!=j:
                a[i],a[j]=a[j],a[i]
                i+=1
                j-=1
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        self.display()

    
obj=SLL()
'''n=int(input("Enter no of nodes:"))
for i in range(1,n+1):
    if i==1:
        item=int(input("Enter item:"))
        node=Node(item)
        obj.head=node
    else:
        item=int(input("Enter item:"))
        newnode=Node(item)
        node.next=newnode
        node=newnode'''
s=input("Enter sequence:")
n=len(s)
for i in s:
    obj.insert_ending(i)
obj.display()
#obj.search()
#obj.middlenode(n)
#obj.longestlength(n)
#bj.bubblesort()
#obj.subs()
obj.reverse()