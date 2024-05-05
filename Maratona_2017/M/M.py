def modulo( n ):
    return n if n > 0 else - n

Andares = [ int( input() ) for _ in range( 3 ) ]

menor = 1000 * 4

for i, a in enumerate(Andares):
    atual = 0
    for j, b in enumerate(Andares):
        if modulo( j - i ) == 1:
            atual += b * 2
        elif modulo( j - i ) == 2:
            atual += b * 4

    if atual < menor:
        menor = atual

print( menor )