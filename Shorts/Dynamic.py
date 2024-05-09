'''

import time
#Teste Fibonnaci recursivo e Dinâmico


#Para perceber a diferença basta calcular para Fibonacci de 40 pra cima

N = int(input())


#PRIMEIRO CALCULANDO RECURSIVO ORIGINAL
def Fib_rec(n):
    
    if n == 1 or n == 0:
        return 1

    return Fib_rec(n-1) + Fib_rec(n-2)

inicio = time.time()
print(Fib_rec(N))
fim = time.time()
print(f"O tempo foi de: {fim-inicio} Recursivo")



#SEGUNDO CALCULANDO RECURSIVO DINÂMICO

memo = [-1 for i in range(N+1)]

memo[0] = 1
memo[1] = 1

def Fib_dyn(n):
    if memo[n] == -1:
        memo[n] = Fib_dyn(n-1) + Fib_dyn(n-2)
    return memo[n]


inicio = time.time()
print(Fib_dyn(N))
fim = time.time()
print(f"O tempo foi de: {fim-inicio} Dinamico")


'''

'''
#PROBLEMA DO TROCO

Tenho um valor V que desejo trocar em valores do conjunto S

V
S {a1, a2, a3, a4, ..., an}

Problema: Determinar a menor quantidade de valores de S que devem ser usados para trocar V


Valor = int(input())
Moedas = list(map(int, input().split()))

memo = [[-1 for j in range(Valor+1)] for i in range(len(Moedas)+1)]

memo[len(Moedas)][0] = 0


INFINITO = 10000000

for i in range(1, Valor+1):
    memo[len(Moedas)][i] = INFINITO

for i in range(len(Moedas)):
    memo[i][0] = 0


    
def escolhe_moedas(moeda, valor):
    if(valor < 0):
        return INFINITO

    else:
        if memo[moeda][valor] == -1:
        
            memo[moeda][valor] = min(1+escolhe_moedas(moeda, valor-Moedas[moeda]), escolhe_moedas(moeda+1, valor))
    
    return memo[moeda][valor]

print(escolhe_moedas(0, Valor))


'''



'''
Problema da Mochila

Um ladrão entra em um museu e desejar roubar um quantidade entre N peças

Cada peça tem um valor V e um peso P

A mochila do ladrão suporta até um peso M

Calcule o maior valor que o ladrão pode roubar sem que ultrapasse o peso permitido


INFINITO = 1000000

M, n = map(int, input().split())

pecas = [[0,0] for i in range(n+1)]

for i in range(n):
    p, v = map(int, input().split())
    pecas[i][0] = p
    pecas[i][1] = v

pecas[n][0] = 0
pecas[n][1] = 0

memo = [[-1 for i in range(M+1)] for j in range(n+1)]

for i in range(M):
    memo[n][i] = 0

for i in range(n):
    memo[n][0] = 0

def calcula_valor(idx, peso_mochila):

    if peso_mochila < pecas[idx][0] or pecas[idx][0] == 0 or pecas[idx][0] == 0:
        return 0
    
    if memo[idx][peso_mochila] == -1:

        memo[idx][peso_mochila] = max( pecas[idx][1] + calcula_valor(idx+1, peso_mochila-pecas[idx][0]), calcula_valor(idx+1, peso_mochila))

    return memo[idx][peso_mochila]

print(calcula_valor(0, M))

'''

