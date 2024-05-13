
class Grafos_Matriz():
    def __init__(self, nos, direct = "Nao Direcionado"):
        self.grafo: list = [[0 for i in range(nos)]for i in range(nos)]
        self.directionated = direct
       
    def make_conection(self, u, v) -> bool:
        try:
            self.grafo[u][v] = 1
            if (self.directionated == "Nao Direcionado"):
                self.grafo[v][u] = 1
            return True
        except:
            return False
        
    def has_conection(self, u, v) -> bool:
        if (self.grafo[u][v] == 1):
            return True
        return False


    def show_grafo(self) -> bool:
        try:
            for i in range(len(self.grafo)):
                for j in range(len(self.grafo)):
                    print(f"{self.grafo[i][j]} ", end="")
                print()
            print()
            return True
        except:
            return False


class Grafos_Lista():
    def __init__(self, nos, direct = "Nao Direcionado"):
        self.grafo: list = [[] for i in range(nos)]
        self.directionated = direct
    
    def make_conection(self, u, v) -> bool:
        try:
            self.grafo[u].append(v)
            if (self.directionated == "Nao Direcionado"):
                self.grafo[v].append(u)
            return True
        except: 
            return False

    def has_conetion(self, u, v) -> bool:
        for i in range(self.grafos[u]):
            if self.grafos[i] == v:
                return True
        return False
    
    def show_grafo(self) -> bool:
        try:
            for i in range(len(self.grafo)):
                print(f"Lista {i} = {self.grafo[i]}")
            print()
            return True
        except:
            return False

    def BFS(self, no: int) -> list:
        queue: list = []
        dist: list = [-1 for i in range(len(self.grafo))]
        fathers: list =  [-1 for i in range(len(self.grafo))]
        visited: list = [False for i in range(len(self.grafo))]

        for i in range(len(visited)):
            visited[i] =  False
        visited[no] = True

        queue.append(no)
        dist[no] = 0
        fathers[no] = 0

        while(len(queue) != 0):
            aux_node = queue.pop(0)
        
            if (len(self.grafo[aux_node]) != 0):
                for i in range(len(self.grafo[aux_node])):
                    if visited[self.grafo[aux_node][i]] == False:
                        visited[self.grafo[aux_node][i]] = True
                        fathers[self.grafo[aux_node][i]] = aux_node
                        dist[self.grafo[aux_node][i]] = dist[aux_node]+1
                        queue.append(self.grafo[aux_node][i])
        return dist

                
                
            

        
        
grafo = Grafos_Lista(6, "Direcionado")
grafo.show_grafo()
grafo.make_conection(2,3)
grafo.make_conection(2,0)
grafo.make_conection(0,1)
grafo.make_conection(0,4)
grafo.make_conection(0,5)

grafo.show_grafo()
tam = len(grafo.grafo)

print(grafo.BFS(0))
print(grafo.BFS(1))
print(grafo.BFS(2))
print(grafo.BFS(3))
print(grafo.BFS(4))
print(grafo.BFS(5))



# for i in range(tam):
#     enc = grafo.BFS(i)
#     flag = True
#     for j in range(len(enc)):
#         if enc[j] == -1:
#             flag = False

#     if flag == True:
#         print(i+1)
#         break


        