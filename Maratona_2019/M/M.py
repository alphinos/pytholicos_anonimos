import math
def gulosa(vetor, competidores, PipocaSegundos, segundos):
    qtd_pipocas=0
    pos=0
    Max=segundos*PipocaSegundos
    while(pos<len(vetor) and competidores>0):
        qtd_pipocas+=vetor[pos]
        if(qtd_pipocas>Max):
            qtd_pipocas=0
            competidores-=1
            pos-=1
        pos+=1
       
    if(competidores>0):
        return True
    return False
def BuscaBinaria(intervalo, vetor, competidores, PipocaSegundos):
    inicio=1
    fim=intervalo
    min=10**9
    while inicio<=fim:
        meio=(inicio+fim)//2
        if(gulosa(vetor,competidores,PipocaSegundos,meio)==True):
            
            if(min>meio):
                min=meio
           
            fim=meio-1
        else:
            inicio=meio+1
  
    print(min)
N,C,T=map(int,input().split())
V=list(map(int,input().split()))
BuscaBinaria(10**9,V,C,T)
