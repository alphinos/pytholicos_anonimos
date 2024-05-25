


N,M= map(int,input().split())
L,K = map(int,input().split())
L=L-1
K=K-1
def qtd_peoes(x,y):
    qtd=0
    if(x+L<=N and y+K<=M and Mapa[x+L][y+K]=='*'):
        qtd+=1
    if(x+K<=N and y+L<=M and Mapa[x+K][y+L]=='*'):
        qtd+=1
    if(x+L<=N and y-K>=0 and Mapa[x+L][y-K]=='*'):
        qtd+=1
    if(x+K<=N and y-L>=0 and Mapa[x+K][y-L]=='*'):
        qtd+=1
    if(x-L>=0 and y+K<=M and Mapa[x-L][y+K]=='*'):
        qtd+=1
    if(x-K>=0 and y+L<=M and Mapa[x-K][y+L]=='*'):
        qtd+=1
    if(x-L>=0 and y-K>=0 and Mapa[x-L][y-K]=='*'):
        qtd+=1
    if(x-K>=0 and y-L>=0 and Mapa[x-K][y-L]=='*'):
        qtd+=1
Mapa=[[]for i in range(N)]
for i in range(N):
    s=input()
    for c in s:
        Mapa[i].append(c)
Maior_qtd=0
posicao=(0,0)
peoes=0
qtd=0
x=0
y=0
for i in range(N):
    
    for j in range(M):
        qtd=0
        x=int(i)
        y=int(j)
    

        if(x+L<N and y+K<M):
            if Mapa[x+L][y+K]=='*':
                qtd+=1
        
        if(x+K<N and y+L<M and Mapa[x+K][y+L]=='*'):
            qtd+=1
        if(x+L<N and y-K>=0 and Mapa[x+L][y-K]=='*'):
            qtd+=1
        if(x+K<N and y-L>=0 and Mapa[x+K][y-L]=='*'):
            qtd+=1
        if(x-L>=0 and y+K<M and Mapa[x-L][y+K]=='*'):
            qtd+=1
        if(x-K>=0 and y+L<M and Mapa[x-K][y+L]=='*'):
            qtd+=1
        if(x-L>=0 and y-K>=0 and Mapa[x-L][y-K]=='*'):
            qtd+=1
        if(x-K>=0 and y-L>=0 and Mapa[x-K][y-L]=='*'):
            qtd+=1


        if(qtd>Maior_qtd):
            Maior_qtd=qtd
            posicao=(i,j)   
            
        
print(posicao)
   

    

