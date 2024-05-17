
'''
Infelizmente, seu melhor amigo está preso em uma caverna que possui vazamentos de água pelo
solo. Mas, felizmente, você possui um mapa detalhado da caverna dizendo onde estão os salões e as
entradas de água.
Seu mapa é descrito em células, cada célula pode representar uma parede de rocha, um espaço vazio
do salão ou um ponto de vazamento de água.
Então, sua tarefa é determinar quais salões ficarão cheios de água a medida que o vazamento
aumenta, com essa informação você conseguirá salvá-lo.
ENTRADA
A entrada é composta por vários mapas, sendo que a descrição de cada mapa começa com uma linha
contendo dois inteiros N e M (1 ≤ N, M ≤ 50), correspondente ao número de linhas e de colunas do
mapa. As N linhas a seguir descrevem o mapa, cada linha contendo M caracteres. Os caracteres
possíveis são: ‘A’ que representa uma célula vazia; ‘X’ que representa uma célula com rocha; e; ‘T’
que representa uma célula com vazamento. A entrada termina com M=N=0.
SAÍDA
Para cada mapa, imprima a estimação da inundação futura. Esta estimação deverá corresponder ao
mapa original, porém trocando as células que serão inundados pelo caractere T. Deixe uma linha em
branco após cada mapa (incluindo o último mapa).

'''
from collections import deque

run = True

def imprime_certo(mapa, lin, col):

    for i in range(lin):
        for j in range(col):
            print(f"{maps[i][j]}", end='')
        print()

while run:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        run = False
        print()
        continue

    maps = [['X' for i in range(n)] for j in range(m)]
    pilha = deque()

    for i in range(m):
        linha = input()
        for j in range(n):
            if linha[j] == 'A':
                maps[i][j] = 'A'
            elif linha[j] == 'T':
                maps[i][j] = 'T'
                pilha.append([i, j])
    
    correction_lin = ['X' for i in range(n)]
    maps.append(correction_lin)

    for i in range(m):
        maps[i].append('X')
    
    if not(pilha):
        imprime_certo(maps, m, n)
    
    while pilha:
        point = pilha.pop()

        lin = point[0]
        col = point[1]

        moves = [(lin-1, col), (lin, col+1), (lin+1, col), (lin, col-1)]
        

        for move in moves:
            x = move[0]
            y = move[1]
            if maps[x][y] == 'A':
                maps[x][y] = 'T'
                pilha.append([x, y])
        
    
    imprime_certo(maps, m, n)
    print()


            