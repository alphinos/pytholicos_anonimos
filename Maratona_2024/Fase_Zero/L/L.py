
N = int(input())

criancas = list(input().split())

ordem_idade = list(input().split())

mintaka = { ordem_idade[i]: 0 for i in range(N)}



mais_chorao = 0

for i in range(N):

    if i == N-1:
        print(ordem_idade[mais_chorao])
    else:
        print(ordem_idade[mais_chorao], end=" ")

    mintaka[criancas[i]] = 1

    if i != N-1:
        if criancas[i] == ordem_idade[mais_chorao]:
            mintaka[ordem_idade[mais_chorao]] = 1
            mais_chorao += 1
            escolhido = mintaka[ordem_idade[mais_chorao]]
            while escolhido != 0:
                mais_chorao += 1
                escolhido = mintaka[ordem_idade[mais_chorao]]

    
    
    
