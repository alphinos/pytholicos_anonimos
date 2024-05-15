#Algoritmo para Fatoração em números primos
import math

N = 124
n = N

factor = 2

N_factor = []

print(len(N_factor))

while N > 1 or factor < int(math.sqrt(N)):

    while N % factor == 0:
        N_factor.append(factor)
        N /= factor

    factor += 1


print(f"{n} = ")
cont = 1
for i in range(len(N_factor)-1):
    if N_factor[i+1] == N_factor[i]:
           cont += 1
    else:
        print(f"{N_factor[i]}^{cont}")
        cont = 1

print(f"{N_factor[-1]}^{cont}")
