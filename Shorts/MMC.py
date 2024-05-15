#Algoritmo para Calcular o MMC entre dois numeros

A, B = map(int, input().split())

factor = 2

mmc = 1

while A > 1 or B > 1:

    while A % factor == 0 or B % factor == 0:
        if A % factor == 0:
            A = A//factor
        if B % factor == 0:
            B = B//factor
        mmc *= factor

    factor += 1

    
print(mmc)