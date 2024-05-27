def MMC_NN2(numbers):
   
    mmc = 1

    
    tam_n = len(numbers)

 
    for i in range(tam_n):
        mmc = lcm(mmc, numbers[i])
    return mmc

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a // gcd(a, b)) * b



N,T = map(int, input().split())
lista=list(map(int, input().split()))

r=int(MMC_NN2(lista))
best_mmc=r
best=1
best_v=0
for i in range(2,T+1):
    best_v=lcm(r,i)
    if(best_v<=T and best_v>best_mmc):
        best_mmc=best_v
        best=i

print(best)




