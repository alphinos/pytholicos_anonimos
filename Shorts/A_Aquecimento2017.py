
N = int(input())

'''Cacular o Fatorial'''
# f = open("Fatorial.txt", "w")

# fatzinho = 2
# fatorial = [1,1]
# while(fatorial[fatzinho-1] < N):
#     fatorial.append(fatorial[fatzinho-1]*fatzinho)
#     fatzinho += 1

# f.write(str(fatorial))


Fatorial = [5040, 720, 120, 24, 6, 2, 1, 1]

#Programação Dinâmica

memo = [[-1 for i in range(N+1)] for i in range(len(Fatorial)+1)]
INFINITO = 1_000_000

for i in range(len(Fatorial)):
    memo[i][0] = 0

for i in range(1, N+1):
    memo[len(Fatorial)][i] = INFINITO

def escolhe_numero_fat(choice_idx, N):

    if N < 0:
        return INFINITO
    
    if memo[choice_idx][N] == -1:
        memo[choice_idx][N] = min(1+escolhe_numero_fat(choice_idx, N-Fatorial[choice_idx]), escolhe_numero_fat(choice_idx+1, N))

    return memo[choice_idx][N]


    

print(escolhe_numero_fat(0, N))

