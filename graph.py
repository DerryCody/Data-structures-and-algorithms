class Graph():
    def __init__(self,n):
        self.adlis = [[ ]for i in range(n)]
        self.n = n
    def createdge(self,V1,V2):
        self.adlis[V1].append(V2)
        self.adlis[V2].append(V1)
    def BFS(self,source):
        self.visited = [False]*self.n
        self.res = []
        self.queue = [source]
        self.visited[source] = True
        while len(self.queue) > 0:
            f = self.queue.pop(0)
            self.res.append(f)
            for node in self.adlis[f]:
                if self.visited[node] != True:
                    self.queue.append(node)
                    self.visited[node] = True
        return self.res 

        

graph = Graph(4)
graph.createdge(0,1)
graph.createdge(1,2)
graph.createdge(2,3)
graph.createdge(3,1)
try1 = graph.BFS(3)
print(try1)
