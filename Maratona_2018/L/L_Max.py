from collections import deque
N, Q = map(int, input().split())

class Vertice:
    def __init__(self, id) -> None:
        self.id = id
        self.pai = None
        self.visto = False
        self.adj = []
    
    def mostrar_vertice(self):
        print(f"ID: {self.id}")
        print(f"ADJ: {self.adj}")
        if self.pai != None:
            print(f"PAI: {self.pai.id}")
        else:
            print("RAIZ - PAI DE TODOS")


class Grafo:
    def __init__(self, vertices_n) -> None:
        self.vertices = []
        self.tam = vertices_n
        for i in range(vertices_n):
            w = Vertice(i+1)
            self.vertices.append(w)
    def mostrar_grafo(self):
        print("__________________")
        for i in range(self.tam):
            self.vertices[i].mostrar_vertice()
            print()
        print("__________________")
    
    def restart(self):
        for i in range(self.tam):
            self.vertices[i].visto = False
    
    
    

g = Grafo(N)

for i in range(N-1):
    E, S = map(int, input().split())
    g.vertices[E-1].adj.append(S)
    g.vertices[S-1].adj.append(E)

def DFS(g: Grafo, A, B):
    encontrado = False

    stack = deque()
    stack.append(g.vertices[A-1])
    g.vertices[A-1].visto = True
    g.vertices[A-1].pai = None

    while stack and not encontrado:
        w = stack.pop()
        #   print(f"Saiu da pilha {w.id}")
        for k in w.adj:
            v = g.vertices[k-1]
            if v.visto == False:
                v.visto = True
                v.pai = w
                stack.append(v)
     
            if v.id == B:
                encontrado = True
                break
    
    pontos = []
    v = g.vertices[B-1]
    while v.pai != None:
        pontos.append(v.id)
        v = v.pai

    pontos.append(A) 
    g.restart()   
    return pontos



def pontos_comuns(g: Grafo, A, B, C, D):
    linha_um = DFS(g, A, B)
    linha_dois = DFS(g, C, D)  
    #print(linha_um)
    #print(linha_dois)
    linha_um.sort() 
    linha_dois.sort()

    tam_um = len(linha_um)
    tam_dois = len(linha_dois)

    one = 0
    two = 0

    contador = 0

    while one < tam_um and two < tam_dois:

        if linha_um[one] == linha_dois[two]:
            contador += 1
            one += 1
            two += 1

        elif linha_um[one] < linha_dois[two]:
            one += 1
        else:
            two += 1
    
    return contador

for i in range(Q):
    A, B, C, D = map(int, input().split())
    print(pontos_comuns(g, A, B, C, D))



    
