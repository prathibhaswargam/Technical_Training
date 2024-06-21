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
    def printInorder(self, node):
        if node:
            self.printInorder(node.left)
            print(node.data, end=" ")
            self.printInorder(node.right)
    def printpreorder(self, node):
        if node:
            print(node.data, end=" ")
            self.printpreorder(node.left)
            self.printpreorder(node.right)
    def printpostorder(self, node):
        if node:
            self.printpostorder(node.left)
            self.printpostorder(node.right)
            print(node.data, end=" ")
    def tree_sum(self,node,s=0):
        if node:
            s += node.data
            s=self.tree_sum(node.left,s)
            s=self.tree_sum(node.right,s)
        return s
    def tree_even_sum(self,node,s1=0):
        if node is None:
            return s1
        if node.data % 2 == 0 :
            s1 += node.data
        s1=self.tree_even_sum(node.left,s1)
        s1=self.tree_even_sum(node.right,s1)
        return s1
    def Absolute_diff(self, node,s=0):
        if node is None:
            return s
        if node.data % 2 == 0:
            s += node.data
        else:
            s -= node.data
        s = self.Absolute_diff(node.left, s)
        s = self.Absolute_diff(node.right, s)
        return abs(s)
    '''def height(self, node,c=-1):
        if node is None:
            return c
        left = self.height(node.left,c+1)
        right = self.height(node.right,c+1)
        return max(left,right)'''
    def height(self, node):
        if node is None:
            return -1
        return max(self.height(node.left),self.height(node.right))+1
    def Balance(self, node):
        return abs(self.height(node.left)-self.height(node.right)) <=1
    def leaf_node(self, node,c=0):
        if node is None:
            return c
        if node.left is None and node.right is None:
            c+=1
        c=self.leaf_node(node.left,c)
        c=self.leaf_node(node.right,c)
        return c
    def leaf_nodes_sum(self, node,s=0):
        if node is None:
            return s
        if node.left is None and node.right is None:
            s+=node.data
        s= self.leaf_nodes_sum(node.left,s)
        s= self.leaf_nodes_sum(node.right,s)
        return s
    def search_depth(self, node,search,depth=0):
        if node is None:
            return 'Element is not found'
        if node.data == search:
            return depth
        left_depth = self.search_depth(node.left, search, depth + 1)
        right_depth=self.search_depth(node.right, search, depth + 1)
        return left_depth if left_depth else right_depth

    def fun(self, node, a=0, s=''):
        if node is None:
            return a
        s += str(node.data)
        if node.left is None and node.right is None:
            a += int(s)
            s=''
            return a
        a_left = self.fun(node.left, a, s)
        a_right = self.fun(node.right, a, s)
        return a_left + a_right - a
obj = Binary_tree()
s = input("Enter the sequence: ").split()
for i in s:
    obj.insert(int(i))
obj.printInorder(obj.root)
'''print('\nAbsolute difference:',obj.Absolute_diff(obj.root))
#obj.printpreorder(obj.root)
#obj.printpostorder(obj.root)
print("\nSum of tree:",obj.tree_sum(obj.root))
print("\nEven sum of tree:",obj.tree_even_sum(obj.root))
print("\nHeight:",obj.height(obj.root))
if obj.Balance(obj.root):
    print("Balanced")
else:
    print("Not Balance ")
print("\nLeaf Node:",obj.leaf_node(obj.root))
print("\nLeaf Nodes sum:",obj.leaf_nodes_sum(obj.root))
search=int(input("Enter the search element: "))
print("\nDepth:",obj.search_depth(obj.root,search))'''
print('\nsum:',obj.fun(obj.root))