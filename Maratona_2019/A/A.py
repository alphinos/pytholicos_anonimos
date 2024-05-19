from collections import deque
M, N, K = map(int, input().split())
for i in range (K):
    x,y,dist=map(int, input().split())

Matriz=[[0 for j in range(N)]for i in range[M]]

def distancia(x,y ,i ,j):
    return (i-x)**2+(y-i)**2

def preencheMatriz(Matriz, x,y, dist):
    for i in range(M):
        for j in range(N):
            if distancia(x,y,i,j)>=dist:
                Matriz[i][j]=1
            

def dfs(Matriz, x, y):
    Q=deque()
