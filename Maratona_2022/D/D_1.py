#Questão D

#Tamanho do lado do quadrado e (Coordenadas do ponto de parada)
N, x, y =  map(int, input().split())

pesos = [0 for i in range(N)]
number = N
last = 1
for i in range(N):
    pesos[i] = i+1

square_superior = [2**N//2,2**N//2]
square_inferior = [2**N//2,2**N//2]


if( x != 2**N//2 and y != 2**N//2):
    for i in range(N):
        square_superior[0] -= (2**N)//(2**(i+2))
        square_superior[1] += (2**N)//(2**(i+2))
        square_inferior[0] += (2**N)//(2**(i+2))
        square_inferior[1] -= (2**N)//(2**(i+2))
        if( x >= square_superior[0] and x <= square_inferior[0] and y >= square_inferior[1] and y <= square_superior[1]):
            print(pesos[i])
            last = 0
            break
else:
    last = 0
    print(0)

if(last):
    print(N)




