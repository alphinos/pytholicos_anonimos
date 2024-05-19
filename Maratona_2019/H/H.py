Voltas, N = map(int, input().split())
Total= Voltas*N
precisao=0.0000000001
for i in range(1,10):
    A=int(Total*i/10)
    if(Total*i/10 -A < precisao):
        if i == 9:
            print( A )
            break
        print(A, end = " ")
    else:
        if i == 9:
            print( A + 1 )
            break
        print(A+1, end = " ")



