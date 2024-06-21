graph={
    '5':[('3',5),('7',6)],
    '7':[('3',4),('5',6),('4',8)],
    '4':[('8',9),('7',8),('2',11)],
    '8':[('4',9),('2',10),('3',7)],
    '3':[('5',5),('7',4),('8',7)],
    '2':[('4',11),('8',10)]
    }
def dfs(node,graph,l=[]):
    print(node,end=' ')
    l.append(node)
    for i,_ in graph[node]:
        print(i,end=' ')
        if i not in l:
            dfs(i,graph,l)
def dfs_paths(node,graph,l=[]):
    l.append(node)
    if node == '2':
        print('\n',l)
        l.pop()
        return
    for i,_ in graph[node]:
        if i not in l:
            dfs_paths(i, graph, l)
    l.pop()
def dfs_mincost(node, graph, l=[], c=0,m=9999999,l1=[]):
    l.append(node)
    if node == '2':
        if c<m:
            m=c
            l1=l.copy()
        l.pop()
        return m,l1
    for i, x in graph[node]:
        if i not in l:
            m,l1=dfs_mincost(i, graph, l, c + x, m,l1)
    l.pop()
    return m,l1
dfs('5',graph)
dfs_paths('5',graph)
print('\nMincost:',dfs_mincost('5',graph))
