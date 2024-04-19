#Questão D

#Tamanho do lado do quadrado e (Coordenadas do ponto de parada)
N, x, y =  map(int, input().split())

points = [[] for i in range(N+1)]

square_center = [2**(N-1), 2**(N-1)]

points[0].append(square_center)

def devolve_metadinha(point_a, point_b) -> list:
    middle = [0,0]
    middle[0] = (point_a[0]+point_b[0])//2
    middle[1] = (point_a[1]+point_b[1])//2
    
    return middle

spaces = [0 for i in range(N+1)]

if(points[0][0][0] == x and points[0][0][1] == y):
    print(0)
else:
    points[1].append(devolve_metadinha(points[0][0], [0,0]))
    points[1].append(devolve_metadinha(points[0][0], [0,2**N]))
    points[1].append(devolve_metadinha(points[0][0], [2**N,0]))
    points[1].append(devolve_metadinha(points[0][0], [2**N, 2**N]))
    spaces[1] = 4

    for i in range(2, N+1):
        for j in range(spaces[i-1]):
            if(points[i-1][j][0] == x and points[i-1][j][1] == y):
                print(i-1)
                break
            else:
                points[i].append(devolve_metadinha(points[i-1][j], [0,0]))
                points[i].append(devolve_metadinha(points[i-1][j], [0,2**N]))
                points[i].append(devolve_metadinha(points[i-1][j], [2**N,0]))
                points[i].append(devolve_metadinha(points[i-1][j], [2**N, 2**N]))

                spaces[i] += 4
                
        


















































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





