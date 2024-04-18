from time import sleep


def modulo( num : int ) -> int:
    return -num if num < 0 else num

def mover_atual( atual : tuple[ int, int ], alvo : tuple[ int, int ], N : int ) -> tuple[ int, int ]:
    dist_x = modulo( alvo[ 0 ] - atual[ 0 ] )
    dist_y = modulo( alvo[ 1 ] - atual[ 1 ] )

    dist_x = alvo[ 0 ] - atual[ 0 ]
    dist_y = alvo[ 1 ] - atual[ 1 ]

    novo_atual_x = 0
    novo_atual_y = 0

    # if ( alvo[ 0 ] - dist_x < 0 ):
    #     novo_atual_x = atual[ 0 ] // 2
    # elif ( alvo[ 0 ] + dist_x > 2**N ):
    #     novo_atual_x = int( atual[ 0 ] * 1.5 )
    # else:
    #     novo_atual_x = alvo[ 0 ]
    
    # if ( alvo[ 1 ] - dist_y < 1 ):
    #     novo_atual_y = atual[ 1 ] // 2
    # elif ( alvo[ 1 ] + dist_y > 2**N ):
    #     novo_atual_y = int( atual[ 1 ] * 1.5 )
    # else:
    #     novo_atual_y = alvo[ 1 ]

    if alvo[ 0 ] + dist_x < 0 or alvo[ 0 ] + dist_x > 2**N:
        if alvo[ 0 ] < 2**N // 2:
            novo_atual_x = atual[ 0 ] // 2
        else:
            novo_atual_x = int( atual[ 0 ] * 1.5 )
    else:
        novo_atual_x = atual[ 0 ]
    
    if alvo[ 1 ] + dist_y < 0 or alvo[ 1 ] + dist_y > 2**N:
        if alvo[ 1 ] < 2**N // 2:
            novo_atual_y = atual[ 1 ] // 2
        else:
            novo_atual_y = int( atual[ 1 ] * 1.5 )
    else:
        novo_atual_y = atual[ 1 ]
    
    return ( novo_atual_x, novo_atual_y )

N, x, y = map( int, input().split() )


atual = ( 2**N // 2, 2**N // 2 )
alvo = ( x, y )

contador = 0

while atual != alvo:
    print( atual )
    atual = mover_atual( atual, alvo, N )
    contador += 1
print( atual )
  
print( contador )

print(  )