#Questão D
#Tamanho do lado do quadrado
N, x, y =  map(int, input().split())

pesos = [0 for i in range(N)]
number = N
last = 1

comparacoes = 0
iteracoes = 0
atribuicoes = 0

for i in range(N):
    pesos[i] = number
    number-=1;
    comparacoes += 2

if ((x,y) != (2**N-1, 2**N-1)):
    for i in range(N):
        if((x,y) >= (2**i-1, 2**i-1) and (x,y) < (2**(i+1)-1,2**(i+1)-1)):
            last = 0
            print(pesos[i])
            atribuicoes += 1
        comparacoes += 3
        iteracoes += 1
    comparacoes += 1

else:
    print(0)

if(last):
    comparacoes += 1
    print(1)

print( comparacoes, atribuicoes, iteracoes )



 