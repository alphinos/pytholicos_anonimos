N = int(input())
vetor = list(map(int, input().split()))

inicio = 0
fim = 0
has_zero = False
print(vetor)
while(fim < N-1):
    if(vetor[fim] == 0):
        has_zero = True

    if( has_zero == True):
        if(vetor[fim+1] == 0):
            fim += 1
        else:
            aux = vetor[fim+1]
            vetor[inicio] = aux
            vetor[fim+1] = 0
            fim += 1
            inicio += 1
    else:
        inicio += 1
        fim += 1
    print(vetor)


max = 0
tam = len(vetor)
for i in range(tam):
    max += 1




