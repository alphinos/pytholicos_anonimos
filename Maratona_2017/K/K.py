from math import sqrt, pow

A, B, N, K = map( int, input().split() )

X = A + sqrt( B )
X = int( pow( X, N ) )

tam = 0
digitos = []

while X // 10 != X:
    digitos.append( X % 10 )
    tam += 1

    X = X // 10

digitos.append( X )

print( digitos[ K - 1 ] )