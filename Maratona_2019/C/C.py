N, M, C = map(int, input().split())

veiculos_seguros = C

# Conjunto para rastrear posições inseguras
inseguro = set()

for c in range(C):
    A, B, D = input().split()
    A = int(A) - 1
    B = int(B) - 1

    # Marcar a posição atual como insegura
    if (A, B) not in inseguro:
        inseguro.add((A, B))
        veiculos_seguros -= 1

    if D == 'N':
        for i in range(A - 1, -1, -1):
            if (i, B) not in inseguro:
                inseguro.add((i, B))
                continue
            break
    elif D == 'S':
        for i in range(A + 1, N):
            if (i, B) not in inseguro:
                inseguro.add((i, B))
                continue
            break
    elif D == 'L':
        for j in range(B + 1, M):
            if (A, j) not in inseguro:
                inseguro.add((A, j))
                continue
            break
    else:  # 'O'
        for j in range(B - 1, -1, -1):
            if (A, j) not in inseguro:
                inseguro.add((A, j))
                continue
            break

print(veiculos_seguros)

"""
N, M, C = map( int, input().split() )

mapa = dict()

veiculos_seguros = C

perigo = dict()

for c in range( C ):
    A, B, D = input().split()
    A = int( A ) - 1
    B = int( B ) - 1

    if mapa.get( A * M + B ) == -1:
       veiculos_seguros -= 1

    if D == 'N':
        for i in range( A - 1, -1, -1 ):
            idx = i * M + B
            if not mapa.get( idx ):
                mapa[ idx ] = A - i
                perigo[ idx ] = [ A - i ]
                continue
            if mapa[ idx ] == A - i:
                perigo[ idx ].append( A - i )
                break
            if A - i > mapa[ idx ]:
                if not perigo.get( idx ):
                    perigo[ idx ] = [ A - i ]
                else:
                    perigo[ idx ].append( A - i )
    elif D == 'S':
        for i in range( A + 1, N ):
            idx = i * M + B
            if not mapa.get( idx ):
                mapa[ idx ] = A - i
                perigo[ idx ] = [ A - i ]
                continue
            if mapa[ idx ] == A - i:
                perigo[ idx ].append( A - i )
                break
            if A - i > mapa[ idx ]:
                if not perigo.get( idx ):
                    perigo[ idx ] = [ A - i ]
                else:
                    perigo[ idx ].append( A - i )
    elif D == 'L':
        for j in range( B + 1, M ):
            idx = A * M + j
            if not mapa.get( idx ):
                mapa[ idx ] = B - j
                perigo[ idx ] = [ B - j ]
                continue
            if mapa[ idx ] == B - j:
                perigo[ idx ].append( B - j )
                break
            if B - j > mapa[ idx ]:
                if not perigo.get( idx ):
                    perigo[ idx ] = [ B - j ]
                else:
                    perigo[ idx ].append( B - j )
    else: # O
        for j in range( B - 1, -1, -1 ):
            idx = A * M + j
            if not mapa.get( idx ):
                mapa[ idx ] = B - j
                perigo[ idx ] = [ B - j ]
                continue
            if mapa[ idx ] == B - j:
                perigo[ idx ].append( B - j )
                break
            if B - j > mapa[ idx ]:
                if not perigo.get( idx ):
                    perigo[ idx ] = [ B - j ]
                else:
                    perigo[ idx ].append( B - j )

for v in perigo.values():
    v.sort()
    bateu = False
    for i in range( len( v ) - 1 ):
        if v[ i ] == -1 or v[ i ] == v[ i + 1 ]:
            bateu = True
        if bateu:
            veiculos_seguros -= 1
    if bateu:
        veiculos_seguros -= 1

print( veiculos_seguros )
"""