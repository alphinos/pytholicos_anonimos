
n, A, B = map(int, input().split())

x = [0 for i in range(n+2)]
y = [0 for i in range(n+2)]


x[0] = A
x[1] = B



def coeficiente_angular(Ancora, pma, pme):
    return (y[pme] - y[Ancora]) * (x[pma] - x[Ancora]) < (y[pma] - y[Ancora]) * (x[pme] - x[Ancora]) 


def inside(pma, pme) -> bool:
    return coeficiente_angular(0, pma, pme) and coeficiente_angular(1, pma, pme) and y[pma] != y[pme] and coeficiente_angular(1,0,pme)

for i in range(2, n+2):
    x_p, y_p = map(int, input().split())

    x[i] = x_p
    y[i] = y_p


freqs = [1 for i in range(n+2)]

for i in range(2, n+2):
    for j in range(2, n+2):
        if i != j:
            if( inside(i, j) == True):
                freqs[i] += 1


maior = freqs[2]

for i in range(2, n+2):
    if freqs[i] > maior:
        maior = freqs[i]
    
print(maior)


