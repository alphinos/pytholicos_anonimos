
N, minimo, tijelas = map(int, input().split())

N -= minimo*tijelas

def combination(n, p):

    numerador = 1
    denominador = 1
    for i in range(p):
        numerador*=n  
        n -= 1
    
    for i in range(1, p+1):
        denominador *= i

    return numerador//denominador

def permutation(n, p):

    for i in range(1, p):
        n *= n-1
    
    return n

print(permutation(36,2))

total = permutation(N, tijelas)

resposta = 0
N+= 1

while N > 0:
    resposta += N
    N -= 2

print(resposta)