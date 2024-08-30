col = int(input())

alturas = list(map(int, input().split()))

tgl_esquerda = [0 for i in range(col)]
tgl_direita = [0 for i in range(col)]

alt = 1

tgl_esquerda[0] = alt
alt += 1

for i in range(1, col):

    if alturas[i] < alt:
        alt = alturas[i]

    if alturas[i-1] >= alt-1:
        tgl_esquerda[i] = alt
        
    alt += 1

alt = 1
tgl_direita[col-1] = alt
alt += 1

for i in range(col-2, -1, -1):

    if alturas[i] < alt:
        alt = alturas[i]

    if alturas[i+1] >= alt-1:
        tgl_direita[i] = alt
        
    alt += 1

maior = 1

mins = [0 for i in range(col)]

for i in range(col):
    mins[i]= min(tgl_direita[i], tgl_esquerda[i])
    if mins[i] > maior:
        maior = mins[i]
        
print(maior)

    




