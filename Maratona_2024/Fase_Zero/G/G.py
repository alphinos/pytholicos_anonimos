
'''
N, Energia = map(int, input().split())

distancias = list(map(int, input().split()))
tabacos = list(map(int, input().split()))

paradas = 0

ponteiro = 0
distancia_primeira = 0

soma_maior = (0, 0)

soma_maior = (distancias[ponteiro] + tabacos[ponteiro], 0)

while ponteiro < N:

    if distancias[ponteiro] - distancia_primeira > Energia:

        Energia = tabacos[soma_maior[1]]
        distancia_primeira = distancias[soma_maior[1]]
        paradas += 1
        ponteiro -= 1
        soma_maior = (0, 0)
        
    elif distancias[ponteiro] + tabacos[ponteiro] >= soma_maior[0]:
        soma_maior = (distancias[ponteiro] + tabacos[ponteiro], ponteiro)

    ponteiro += 1


if ponteiro == N:
    print(paradas)

else:
    print(-1)

'''

from collections import deque

class Vertice:
    def __init__(self, x, y):
        self.coord = x
        self.energy = y
        self.adj = []
        self.paradas = -1
    
    def imprime(self):
        print(f"X: {self.coord}, E: {self.energy}, ADJ:{self.adj}")
    
points = []
N, Energia = map(int, input().split())

vertice_zero = Vertice(0,Energia)
for i in range(N):
    vertice_zero.adj.append(i+1)

points.append(vertice_zero)
distancias = list(map(int, input().split()))
tabacos = list(map(int, input().split()))


for i in range(N):
    v = Vertice(distancias[i], tabacos[i])
    for i in range(i+2, N+1):
        v.adj.append(i)

    points.append(v)

# for k in range(N+1):
#     points[k].imprime()


def bfs(grafo, vertice):

    fila= deque()
    fila.append(grafo[vertice])
    grafo[0].paradas = 0
    Energia = 0
    while fila:
        w = fila.popleft()
        Energia = w.energy
        tam = len(w.adj)
        if Energia - (grafo[N].coord-w.coord) >= 0:
            return w.paradas
        
        for i in range(tam): 
            if Energia - (grafo[w.adj[i]].coord-w.coord) >= 0:
                if w.paradas != grafo[w.adj[i]].paradas:
                    fila.append(grafo[w.adj[i]])
                    grafo[w.adj[i]].paradas = w.paradas + 1
    
    return -1
print(bfs(points, 0))
'''
6 11
3 8 15 25 30 45
12 5 15 20 15 12

Deveria retornar 3
Atualmente retorna 1
'''    

            




