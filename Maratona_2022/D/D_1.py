#Questão D

#Tamanho do lado do quadrado e (Coordenadas do ponto de parada)
N, x, y =  map(int, input().split())

points = [[0,0]for i in range(N)]
square_center = [2**(N-1), 2**(N-1)]
points[0] = square_center
step = [(2**N//2)//2, (2**N//2)//2]


#Calculará a coordenada do ponto seguinte ao ponot atual, bom base no quadrante do destino.
def devolve_metadinha(point_a, quadrant, step) -> list:
    middle = [0,0]

    if(quadrant == 0):
        middle[0] = (point_a[0] - step[0])
        middle[1] = (point_a[1] - step[1])
    elif (quadrant == 1):
        middle[0] = (point_a[0] - step[0])
        middle[1] = (point_a[1] + step[1])
    elif (quadrant == 2):
        middle[0] = (point_a[0] + step[0])
        middle[1] = (point_a[1] + step[1])
    elif (quadrant == 3):
        middle[0] = (point_a[0] + step[0])
        middle[1] = (point_a[1] - step[1])
    
    return middle

#Calcula em qual quadrante está o ponto de destino com base no ponto atual, começando do ponto autal sendo o centro
def find_quadrant(point_a, point_b) -> int:

    if(point_a[0] < point_b[0] and point_a[1] < point_b[1]):
        return 0
    elif (point_a[0] < point_b[0] and point_a[1] > point_b[1]):
        return 1
    elif (point_a[0] > point_b[0] and point_a[1] > point_b[1]):
        return 2
    elif (point_a[0] > point_b[0] and point_a[1] < point_b[1]):
        return 3
    else:
        return -1


#Interamos sobre N-1 vezes, suficiente para decidir se o ponto é atingido em 1, 2, 3 ... N-1 ativações dos atratores
for i in range(N-1):
    #Testando sempre se o ponto que eu estou é o ponto colocado no problema
    if(points[i][0] == x and points[i][1] == y):
        print(i)
        break

    #Calculamos o quadrante do ponto alvo em relação ao ponto atual
    quadrant = find_quadrant([x,y], points[i])
    if(quadrant == -1):
        print(N)
        break

    #O ponto atual é atualizado com o devolve_metadinha, colocando ele no proximo indice e assim por diante. 
    #Cada ponto proximo será calculado com base no ponto anterior
    points[i+1] = devolve_metadinha(points[i], quadrant, step)

    #O passo de calcular o próximo ponto vai diminuindo a cada iteração, como observado empiricamente
    if(step[0] != 1 and step[1] != 1):
        step = [step[0]//2, step[1]//2]

#Como não chegamos a testar na ultima iteração, aqui está ela
if(points[N-1][0] == x and points[N-1][1] == y):
    print(N-1)







































'''Essa parte aqui foi com Deus
    Entendemos a Questão Errada kekw'''

# pesos = [0 for i in range(N)]
# number = N
# for i in range(N):
#     pesos[i] = i+1

# square_superior = [2**N//2,2**N//2]
# square_inferior = [2**N//2,2**N//2]


# if( x != 2**N//2 and y != 2**N//2):
#     for i in range(N):
#         square_superior[0] -= (2**N)//(2**(i+2))
#         square_superior[1] += (2**N)//(2**(i+2))
#         square_inferior[0] += (2**N)//(2**(i+2))
#         square_inferior[1] -= (2**N)//(2**(i+2))
#         print(square_inferior)
#         print(square_superior)
#         if( x >= square_superior[0] and x <= square_inferior[0] and y >= square_inferior[1] and y <= square_superior[1]):
#             print(pesos[i])
#             break
# else:
#     print(0)
