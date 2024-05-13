#Desvedando o Monty Hall

N = int(input())
Total = N
for i in range(N):
    a = int(input())
    if a == 1:
        Total -= 1

print(Total)