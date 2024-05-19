N = int(input())
max=0
indice=0
for i in range(N):
    A= int(input())
    if(A>max):
        max=A
        indice=i
if(indice==0):
    print("S")
else:
    print("N")