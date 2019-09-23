from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addEdge(self,src,des):
        self.graph[src].append(des)

    def seeEdge(self,visited,v):
        print(v)
        visited[v]=True
        for i in self.graph[v]:
            if visited[i]==False:
                self.seeEdge(visited,i)
    def DFS(self,ver):
        visited=[False]*(len(self.graph))
        self.seeEdge(visited,ver)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.DFS(2)