import math
N = int(input())

maxima_entrada = 10000
N_factor = [0 for i in range(maxima_entrada)]

def fatores_primos(n) -> None:
    factor = 2
    N_factor[5] = 0

    while n > 1 or factor < int(math.sqrt(n)):

        while n % factor == 0:
            N_factor[factor] += 1
            n = n//factor
        factor += 1


def calcula_zeros_leandro(N):

    quant_5 = 0

    fator_q_divide = 5

    while N//fator_q_divide > 0:
        quant_5 += N//fator_q_divide
        fator_q_divide*=5

    return quant_5

def calcula_zeros_maxwell(N):

    quant_5 = 0

    while N > 0:
        fatores_primos(N)
        quant_5 += N_factor[5]
        N -= 5

    return quant_5


print(calcula_zeros_leandro(N))
print(calcula_zeros_maxwell(N))