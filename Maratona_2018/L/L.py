class Graph:
    def __init__(self, size):
        self.graph = { i : list() for i in range( size + 1 ) }
        self.size = size + 1

    def add_non_directed_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, no):
        distancia = [-1 for i in range( self.size )]
        distancia[no] = 0

        visited = [False for i in range( self.size )]
        visited[no] = True

        alfa = [ None for i in range( self.size ) ]
        alfa[ no ] = None

        
        fila = []
        fila.append(no)


        while fila:
            no_tirado = fila.pop(0)

            for w in self.graph[no_tirado]:
                if visited[w] == False:
                    distancia[w] = distancia[no_tirado] + 1
                    visited[w] = True
                    fila.append(w)
                    alfa[ w ] = no_tirado

        return alfa
    
    def path( self, alfa, u, v ):
        path = []
        while u != v:
            if alfa[ v ] is None:
                break
            path.append( v )
            v = alfa[v]

        path.append( u )

        return path

N, Q = map( int, input().split() )

graph = Graph( N )

for n in range( N - 1 ):
    u, v = map( int, input().split() )
    graph.add_non_directed_edge( u, v )

qtd_comuns = [  ]

for q in range( Q ):
    A, B, C, D = map( int, input().split() )

    com_a = graph.bfs( A )
    com_b = graph.bfs( C )

    com_a = graph.path( com_a, A, B )
    com_b = graph.path( com_b, C, D )
    
    comuns = set( com_a )
    qtd = 0
    for b in com_b:
        if b in comuns:
            qtd += 1

    qtd_comuns.append( qtd )

print( *qtd_comuns, sep = "\n" )