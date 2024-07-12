def ehDespojado(N):
    i=2
    stat=True 
    while i*i<=N:  
        if(N%(i*i)==0):
            return False
        if(N%i==0):
            stat=False
        i+=1
    return not stat

N= int(input())


i=1
cont=0
while(i*i<=N):
    if(N%i==0):
        outro_divisor=N//i
        print(f'i{i} outro:{outro_divisor}')
        if(outro_divisor!=i and ehDespojado(outro_divisor)):
            cont+=1    
        if(ehDespojado(i)):
            cont+=1
    i+=1
print(cont)
     