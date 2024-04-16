#Questão J
n = int(input())

cartas = [1,2,3,4,5,6,7,8,9,10,10,10,10]
usadas = [0 for i in range(13)]
maria_vence = 0

j = 0
m = 0

c1, c2 = map(int, (input().split()))
j += c1 
j+=c2
usadas[c1]+=1
usadas[c2]+=1


c1, c2 = map(int, (input().split()))
m += c1 
m +=c2
usadas[c1]+=1
usadas[c2]+=1

next_j = list(map(int, input().split()))

for i in range(n):
    j += next_j[i]
    m += next_j[i]
    usadas[next_j[i]] += 1
    
for i in range(len(usadas)):
    if ((usadas[i] < 4) and ((m + i == 23) or ((j + i > 23) and (m + i <= 23)))):
        print(i)
        maria_vence = 1
        break

if(not(maria_vence)):
   print(-1) 

