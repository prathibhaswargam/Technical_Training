class node:
    def __init__(self):
        self.d = {}
        self.flag = 0


class tries:
    def __init__(self):
        self.root = node()

    def insert(self, str):
        t= self.root
        for i in str:
            if i not in t.d:
                t.d[i] = node()
            t=t.d[i]
        t.flag = 1
    def  search(self, str):
        t = self.root
        for i in str:
            if i not in t.d:
                return False
            t = t.d[i]
        return t.flag == 1
    def prefix(self,str):
        t = self.root
        for i in str:
            if i not in t.d:
                return False
            t = t.d[i]
        return True
    def _dfs(self, node, prefix,l=[]):
        if node.flag == 1:
            l.append(prefix)
        for char, next_node in node.d.items():
            self._dfs(next_node, prefix + char,l)
        return l
    def print_prefix(self):
        prefix=input("Enter prefix: ")
        t = self.root
        for char in prefix:
            if char not in t.d:
                return
            t = t.d[char]
        return self._dfs(t, prefix)
t1 = tries()
n=int(input())
for i in range(n):
    s = input()
    t1.insert(s)
print(t1.search('word'))
#print(t1.prefix('wo'))
l=t1.print_prefix()
print(max(l))

