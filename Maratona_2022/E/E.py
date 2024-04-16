#Questão E
import time
import random
N=10**7+1
v=[0 for i in range(N)] #Esse vetor guarda as alturas já visitadas e decrementa com o tempo
#num=int(input())
ans=0
#n=map(int,input().split())
n = [random.randint(0, 10**7) for _ in range(10**7)] #inicializando o vetor de entrada com numeros aleatórios
inicio=time.time()
for i in n:
    if v[i]>0: #Caso seja 1 nessa posição, na proxima iteração o 1 vai para posição i-1 e a posição i vira 0
        v[i]-=1
    else: #Caso contrário, coloca uma flecha nessa posição
        ans+=1
    v[i-1]+=1 #Incrementa a posição i-1 em 1(pois a cada passo a flecha desce 1 posição)

print(ans)
fim=time.time()
diferenca_tempo = fim - inicio

#Mostrando a diferença de tempo com precisão de 2 casas decimais
print("Tempo decorrido: {:.20f} segundos".format(diferenca_tempo))
    
