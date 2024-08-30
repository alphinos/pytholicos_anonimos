'''
A, B, C, D = map(int, input().split())




n % A == 0
n % B != 0
C % n == 0
D % n != 0

n = A
depois_da_metade = []
encontrou_antes_da_metade = False
encontrou_depois_da_metade = False


while n*n < C - A:

    complemento = C//n

    if n % A == 0 and n % B != 0 and C % n == 0 and D % n != 0:
        encontrou_antes_da_metade = True
        print(n)
        break

    if complemento % A == 0 and complemento % B != 0 and C % complemento == 0 and D % complemento != 0:
        encontrou_depois_da_metade = True
        depois_da_metade.append(complemento)

    n += A


if not(encontrou_antes_da_metade) and not(encontrou_depois_da_metade):
    print(-1)
elif not(encontrou_antes_da_metade) and encontrou_depois_da_metade:
    print(min(depois_da_metade))
'''

A, B, C, D = map(int, input().split())

n = 1

encontrou_antes_da_metade = False
encontrou_depois_da_metade = False
depois_da_metade = []

while n * n < C:

    if C % n == 0:

        complemento = C//n

        if n % A == 0 and n % B != 0 and C % n == 0 and D % n != 0:
            encontrou_antes_da_metade = True
            print(n)
            break

        if complemento % A == 0 and complemento % B != 0 and C % complemento == 0 and D % complemento != 0:
            encontrou_depois_da_metade = True
            depois_da_metade.append(complemento)
        
    n += 1
if not(encontrou_depois_da_metade) and not(encontrou_antes_da_metade):
    print(-1)

elif not(encontrou_antes_da_metade) and encontrou_depois_da_metade:
    print(min(depois_da_metade))
    
