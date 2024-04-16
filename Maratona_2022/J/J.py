#Questão J
n = int(input())

cartas = [1,2,3,4,5,6,7,8,9,10,10,10,10] #Cartas e suas pontuações no respectivo índice
usadas = [0 for i in range(13)] #Armazenas quais cartas usadas. Só existem 4 cartas de cada
maria_vence = 0 

j = 0
m = 0

#Somamos pontos de João e marcamos a carta que foi usada
c1, c2 = map(int, (input().split()))
j += cartas[c1-1]
j += cartas[c2-1]
usadas[c1-1]+=1
usadas[c2-1]+=1

#Somamos pontos de Maria e marcamos a carta que foi usada
c1, c2 = map(int, (input().split()))
m += cartas[c1-1]
m += cartas[c2-1]
usadas[c1-1]+=1
usadas[c2-1]+=1

#Guardamos as proximas cartas, que são comuns
next_j = list(map(int, input().split()))

#Somamos os pontos comuns e marcamos como cartas usadas
for i in range(n):
    j += cartas[next_j[i]-1]
    m += cartas[next_j[i]-1]
    usadas[next_j[i]-1] += 1

#Verificamos da menor carta para a maior em pontuação qual faz Maria vencer
for i in range(len(usadas)):
    #Maria vence quando faz exatos 23 pontos indendente dos pontos de João, ou quando João estoura e ela não
    if ((usadas[i] < 4) and ((m + cartas[i] == 23) or ((j + cartas[i] > 23) and (m + cartas[i] < 23)))):
        print(i+1)
        maria_vence = 1 #Maria venceu
        break
#Se Maria não venceu imprimimos
if(not(maria_vence)):
   print(-1) 

