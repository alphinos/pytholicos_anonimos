def naoehPrimo(n):
    if(n==1): return True
    if(n%2==0 and n!=2):
        return True
    i=3
    while i*i<=n:
        if n%i==0:
            return True
        i+=2
    return False
T=int(input())
resposta=[]
X,Y=0,0
for i in range(T):
    N=int(input())
    if N%2==1:
        X=N//2
    else:
        X=N//2-1
    stat=True
    while(X>=1):
        Y=N-X
        if(naoehPrimo(X) and naoehPrimo(Y) ):
            resposta.append((X,Y))
            stat=False
            break
        X-=1
        
    if(stat):
        resposta.append(-1)
for i in range(T):
    if(resposta[i]!=-1):
        print(f'{resposta[i][0]} {resposta[i][1]}')
    else:
        print('-1')



