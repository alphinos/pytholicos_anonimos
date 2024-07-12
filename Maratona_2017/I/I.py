#IMPOSTO REAL

from collections import deque
class Vertice:
    def __init__(self, id) -> None:
        self.id = id
        self.adj = {}
        self.gold = 0
        self.pai = None
        self.terminado = False
        self.visto = False
    
    def mostrar_vertice(self):
        print(f"ID: {self.id}")
        print(f"ADJ : {self.adj}")
        print(f"GOLD: {self.gold}")
        if self.pai != None:
            print(f"PAI: {self.pai.id}")
        else:
            print(f"PAI: SENPAI")


class Grafo:
    def __init__(self, vt) -> None:
        self.vertices: list[Vertice] = []
        for i in range(vt):
            v = Vertice(i+1)
            self.vertices.append(v)


N, G = map(int, input().split())
Gold = list(map(int, input().split()))

g = Grafo(N)

for i in range(N):
    g.vertices[i].gold = Gold[i]

for i in range(N-1):
    E, S, D = map(int, input().split())
    g.vertices[E-1].adj[S] = D
    g.vertices[S-1].adj[E] = D

for i in range(N):
    #print(g.vertices[i].mostrar_vertice())
    pass

stack = deque()
g.vertices[0].visto = True
stack.append(g.vertices[0])

distancia = 0
#print()
#print(f"TAMANHO {len(stack)}")
#print()

while stack:
    w = stack.pop()
    stack.append(w)

    #print(f"TAMANHO {len(stack)}")

    symx = True
    for k in w.adj:
        #print(f"Chave {k}")
        vtc = g.vertices[k-1]
        if vtc.visto == False:
            stack.append(vtc)
            vtc.pai = w
            vtc.visto = True
            symx = False

    #w.mostrar_vertice()
    if symx:
        w = stack.pop()
        if w.pai != None:
            d_pai = w.adj[w.pai.id]
            #print(f"{w.id} -> Distancia PAI: {d_pai}")
        
            if w.gold%G != 0:
                idas = (w.gold//G) + 1
            else:
                idas = w.gold//G
            
            w.pai.gold += w.gold
            distancia += 2*idas*d_pai
        

print(distancia)