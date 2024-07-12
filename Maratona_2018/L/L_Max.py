N, Q = map(int, input().split())

class Vertice:
    def __init__(self, id) -> None:
        self.id = id
        self.adj = []

class Grafo:
    def __init__(self, vertices) -> None:
        self.vertices = []

        for i in range(vertices):
            w = Vertice(i)
            self.vertices.append(w)

g = Grafo(N)

for i in range(N-1):
    E, S = map(int, input().split())
    g.vertices[E-1].adj.append(S)
    g.vertices[S-1].adj.append(E)


def pontos_comuns(g: Grafo, A, B, C, D):
    pass


\











for i in range(Q):
    A, B, C, D = map(int, input().split())
    print(pontos_comuns(g, A, B, C, D))



    
