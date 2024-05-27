musica = [ False, False, False ]

ouviu = map( int, input().split() )

for s in ouviu:
    if s != 0:
        musica[ s - 1 ] = True

for i, m in enumerate( musica ):
    if m is False:
        print( i + 1 )
        break