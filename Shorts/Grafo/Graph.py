class Graph:
    def __init__(self, size):
        self.graph = { i : list() for i in range( size ) }
        self.size = size

    def add_directed_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def remove_directed_edge(self, u, v):
        if u in self.graph and v in self.graph:
            if v in self.graph[u]:
                self.graph[u].remove(v)

    def add_non_directed_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def remove_non_directed_edge(self, u, v):
        if u in self.graph and v in self.graph:
            if v in self.graph[u]:
                self.graph[u].remove(v)
            if u in self.graph[v]:
                self.graph[v].remove(u)

    def display(self):
        for node in self.graph:
            print(node, "->", " -> ".join(map(str, self.graph[node])))


    def bfs(self, no):
        distancia = [-1 for i in range( self.size )]

        visited = [False for i in range( self.size )]
        visited[no] = True

        distancia[no] = 0
        
        fila = []
        fila.append(no)
        
        while fila:
            no_tirado = fila.pop(0)
            for w in self.graph[no_tirado]:
                if visited[w] == False:
                    distancia[w] = distancia[no_tirado] + 1
                    visited[w] = True
                    fila.append(w)
            print(visited)


        return distancia

        
    def dfs(self, no):
        distancia = [-1 for i in range( self.size )]

        visited = [False for i in range( self.size )]
        visited[no] =  True

        distancia[no] = 0

        pilha = []
        pilha.append(no)

        while pilha:
            no_tirado = pilha.pop()

            for w in self.graph[no_tirado]:
                if visited[w] ==  False:
                    distancia[w] = distancia[no_tirado] + 1
                    pilha.append(w)
                    visited[w] = True
            print(visited)


        return distancia

G = Graph( 6 )
G.add_directed_edge(1,2)
G.add_directed_edge(0,4)
G.add_directed_edge(0,1)
G.add_directed_edge(4,3)

G.display()

print(G.dfs(0))
print()
print(G.bfs(0))


