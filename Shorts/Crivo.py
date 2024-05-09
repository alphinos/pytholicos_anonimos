f=open("Primos.txt","w")
import time
N = 1_000_000_000

n = [0 for i in range(N)]

primos = []

inicio = time.time()
for i in range(2, N):
    if(n[i] == 0):
        primos.append(i)
    
    for p in primos:
        if(i*p >= N):
            break

        n[i*p] = 1

        if(i%p == 0):
            break
fim = time.time()

# print(primos[0:100])
print(f"Quantidade de primos entre 1 e {N}: {len(primos)}")
print(f"O tempo em segundos é: {fim-inicio}")

f.write(str(primos))
f.close()

#CArlkos ficou LOKO

# def marca_primos( i, j, N, tam_primos, mark, primos ):
#     if i * primos[ j ] >= N:
#         return

#     marca_primos( i, j + 1, tam_primos, mark, primos )

# def primo( i, N, mark, primos ):
#     if i == N:
#         return
#     if mark[ i ] == 0:
#         primos.append( i )
    
