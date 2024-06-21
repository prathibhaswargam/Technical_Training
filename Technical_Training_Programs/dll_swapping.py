class Node:
    def __init__(self,x):
        self.prev=None
        self.data=x
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
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
                    #print(temp.prev,end=' ')
                    print(temp.data,end=" <-> ")
                    #print(temp.next,end=" ")
                else:
                    #print(temp.prev,end=' ')
                    print(temp.data,end="\n")
                    #print(temp.next,end=" ")
                temp=temp.next
    def swap(self):
        t=self.head
        h=self.head
        t3=None
        t1=t.next
        while t and t.next:
            if t==self.head:
                h=t1
                t1.next=t1.prev
                t1.prev=None
                t.prev=t1
                t.data,t1.data=t1.data,t.data
            else:
                t3=t.prev
                t.next,t1.next,t1.prev,t.prev=t1.next,t,t.prev,t1
                t3.next=t1
                t.data, t1.data = t1.data, t.data
                t = t.next.next
                t1=t.next
                h=t1
        print("Swapped Elements:")
        self.display()
    #Paranthesis is Balanced or Not
    def isValid(self):
        stack = []
        opening_brackets = ['(', '[', '{']
        closing_brackets = [')', ']', '}']
        bracket_mapping = {')': '(', ']': '[', '}': '{'}
        char=self.head
        while char is not None:
            if char.data in opening_brackets:
                stack.append(char.data)
            elif char.data in closing_brackets:
                if not stack or bracket_mapping[char.data] != stack.pop():
                    print(False)
                    return
            char=char.next
        if len(stack) == 0:
            print(True)
        else:
            print(False)
    # Absolute Difference Between even and odd sum
    def Absolute_diff(self, t, s1=0, s2=0):
        if t is None:
            return abs(s1 - s2)
        if t.data % 2 == 0:
            s1 += t.data
        else:
            s2 += t.data
        return self.Absolute_diff(t.next, s1, s2)
    #How Many prime numbers are there in the List
    def isprime(self, x, i=2):
        if x <= 1:
            return False
        if i > x // 2:
            return True
        if x % i == 0:
            return False
        return self.isprime(x, i + 1)
    def Prime_count(self, t, c=0):
        if t is None:
            return c
        if self.isprime(t.data):
            c += 1
        return self.Prime_count(t.next, c)
        
        
obj=DLL()
s=input("Enter sequence:").split()
n=len(s)
for i in s:
    obj.insert_ending(int(i))
#obj.isValid()
print(obj.Prime_count(obj.head))