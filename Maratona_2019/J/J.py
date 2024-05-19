CARTAS ={'A':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        'D':10,
        'Q':11,
        'J':12,
        'K':13}

def QuemVenceu(Jogadores): 
    for indice,Jogador in enumerate(Jogadores):
        if(len(Jogador)==4):
            control=True
            for j in range(3):
                if Jogador[j]!=Jogador[j+1]:
                    control=False
                    break
            if(control==True):
                return indice+1
    return 0    
    

def frequencia(vetor):
    VetorFreq=[0 for i in range(13)]
    for i in vetor:
        if i != -1:
            VetorFreq[i-1]+=1
    min=10
    i=0
    for indice,valor in enumerate(VetorFreq):
        if(valor<min and valor!=0):
            min=valor
            i=indice   
    return i+1

            
N, C = map(int,input().split())
Jogadores = [[] for i in range(N)]
for i in range(N):
    cartas = input()
    for j in range(4):
        Jogadores[i].append(CARTAS[cartas[j]])
   
Jogadores[C-1].append(-1)
Existe_vencedor = False
comeco = C-1
acabou_de_receber = True

while not Existe_vencedor:
    if(-1 in Jogadores[comeco] and acabou_de_receber == False):
        Jogadores[comeco].remove(-1)
        comeco=(comeco+1)%N
        Jogadores[comeco].append(-1)
        acabou_de_receber = True

    else:
        f = frequencia(Jogadores[comeco])
        Jogadores[comeco].remove(f)
        comeco=(comeco+1)%N
        Jogadores[comeco].append(f)
        acabou_de_receber = False

    Existe_vencedor=QuemVenceu(Jogadores)

print(Existe_vencedor)
    


    
