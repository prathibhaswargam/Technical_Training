class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

class Binary_tree:
    def __init__(self):
        self.root = None
    def insert(self, x):
        if self.root is None:
            self.root = Node(x)
        else:
            self.insert1(self.root, x)
    def insert1(self, node, x):
        if x < node.data:
            if node.left is None:
                node.left = Node(x)
            else:
                self.insert1(node.left, x)
        else:
            if node.right is None:
                node.right = Node(x)
            else:
                self.insert1(node.right, x)
    def topview(self,root):
        if root is None:
            return
        q = []
        d = dict()
        c = 0
        q.append((root, c))
        while len(q):
            node, c = q.pop(0)
            c = c
            if c not in d:
                d[c] = node.data
            if node.left:
                q.append((node.left, c - 1))
            if node.right:
                q.append((node.right, c + 1))
        for i in sorted(d):
            print(d[i], end=" ")
    def bottomview(self,root):
        if root is None:
            return
        q = []
        d = dict()
        c = 0
        q.append((root, c))
        while len(q):
            node, c = q.pop(0)
            c = c
            d[c]=node.data
            if node.left:
                q.append((node.left, c - 1))
            if node.right:
                q.append((node.right, c + 1))
        for i in sorted(d):
            print(d[i], end=" ")
    def leftview(self,root,c=0,d={}):
        if root is None:
            return
        if c not in d:
            d[c] = root.data
            print(root.data, end=" ")
        self.leftview(root.left,c+1,d)
        self.leftview(root.right,c+1,d)
        return d
    def rightview(self,root,c=0,d={}):
        if root is None:
            return
        if c not in d:
            d[c] = root.data
            print(root.data, end=" ")
        self.rightview(root.right,c+1,d)
        self.rightview(root.left,c+1,d)
        return d
    '''def topview1(self, root, c=0, d=None):
        if d is None:
            d = {}
        if root is None:
            return d
        if c not in d or d[c] < root.data:
            d[c] = root.data
        self.topview1(root.left, c - 1, d)
        self.topview1(root.right, c + 1, d)
        return d'''
obj = Binary_tree()
s = input("Enter the sequence: ").split()
for i in s:
    obj.insert(int(i))
#obj.topview(obj.root)
print("\nLeft View:")
obj.leftview(obj.root)
print("\nRight View:")
obj.rightview(obj.root)
print("\nTop View:")
obj.topview(obj.root)
print("\nBottom View:")
obj.bottomview(obj.root)
#7 2 1 4 5 6 8
#10 5 15 2 7 11 8 9