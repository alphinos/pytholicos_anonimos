
n, A, B = map(int, input().split())

coords = [[0,0] for i in range(n)]
freqs = [1 for i in  range(n)]

for i in range(n):
    a, b = map(int, input().split())
    coords[i][0] = a
    coords[i][1] = b

for i in range(n):
    mA = coords[i][1]/(coords[i][0]-A)
    mB = coords[i][1]/(coords[i][0]-B)

    bA = -mA*A
    bB = -mB*B

    print(f"A equacao de A eh: y = {mA}x + {bA}")
    print(f"A equacao de B eh: y = {mB}x + {bB}")

    for j in range(n):
        if(coords[j][1] < mB*coords[j][0]+bB and coords[j][1] > mA*coords[j][0] + bA and coords[j][0] != coords[i][0] and coords[j][1] != coords[i][1]):
            freqs[i] += 1
    



maior_freqs = freqs[0]

# print(freqs)

# for i in range(1, n):
#     if freqs[i] > maior_freqs:
#         maior_freqs = freqs[i]
    
