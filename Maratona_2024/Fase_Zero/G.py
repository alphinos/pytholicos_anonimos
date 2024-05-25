

N, Energia = map(int, input().split())

distancias = list(map(int, input().split()))
tabacos = list(map(int, input().split()))

paradas = 0

ponteiro = 0
distancia_primeira = 0

soma_maior = (0, 0)

soma_maior = (distancias[ponteiro] + tabacos[ponteiro], 0)

while ponteiro < N:

    if distancias[ponteiro] - distancia_primeira > Energia:

        Energia = tabacos[soma_maior[1]]
        distancia_primeira = distancias[soma_maior[1]]
        paradas += 1
        ponteiro -= 1
        soma_maior = (0, 0)
        
    elif distancias[ponteiro] + tabacos[ponteiro] >= soma_maior[0]:
        soma_maior = (distancias[ponteiro] + tabacos[ponteiro], ponteiro)

    ponteiro += 1


if ponteiro == N:
    print(paradas)

else:
    print(-1)
