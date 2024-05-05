N, Q = map( int, input().split() )

notas = [ 1 for _ in range( N ) ]

for _ in range( Q ):
    a, b = map( int, input().split() )

    freq = 0
    acum =  [ 0 ] * 9
    for n in notas[ a : b + 1 ]:
        acum[ n ] += 1
        
        if acum[ n ] < acum[ freq ]:
            continue
        
        freq = n
    
    for i in range( a, b + 1 ):
        notas[ i ] = ( notas[ i ] + freq ) % 9
    
print( *notas, sep = "\n" )
# print( *acum.values() )


# N, Q = map(int, input().split())

# notas = [1] * N

# # Calcular a frequência de cada número em notas
# freq = [0] * 10
# for n in notas:
#     freq[n] += 1

# for _ in range(Q):
#     a, b = map(int, input().split())

#     most_freq = max( range(10), key = lambda x: freq[x] )
#     for i in range(a, b + 1):
#         notas[i] = (notas[i] + most_freq) % 9
#         freq[notas[i]] += 1
#         freq[notas[i] - most_freq] -= 1

# print(*notas, sep="\n")

"""
N, Q = map( int, input().split() )

notas = [ 1 for _ in range( N ) ]

for _ in range( Q ):
    a, b = map( int, input().split() )

    freq = 0
    acum = { 0 : 0 }
    for n in notas[ a : b + 1 ]:
        if acum.get( n ):
            acum[ n ] += 1
        else:
            acum[ n ] = 1
        
        if acum[ n ] < acum[ freq ]:
            continue
        
        freq = n
    
    for i in range( a, b + 1 ):
        notas[ i ] = ( notas[ i ] + freq ) % 9
    
print( *notas, sep = "\n" )
"""

"""N, Q = map( int, input().split() )

notas = [ 1 for _ in range( N ) ]

m_freq = 1

for _ in range( Q ):
    a, b = map( int, input().split() )

    freq = 0
    acum = { 0 : 0 }
    for i, n in enumerate( notas[ a : b + 1 ] ):
        if acum.get( n ):
            acum[ n ] += 1
        else:
            acum[ n ] = 1
        
        notas[ i ] = ( notas[ i ] + m_freq ) % 9
        
        if acum[ n ] > acum[ freq ]:
            for j in range(a, i + 1 ):
                notas[ j ] = ( notas[ j ] + 1 ) % 9
        
        if acum[ n ] < acum[ freq ]:
            continue
        
        freq = n



    
    print( *notas, sep = " " )
    
    m_freq += freq
    
    # for i in range( a, b + 1 ):
    #     notas[ i ] = ( notas[ i ] + freq ) % 9
    
print( *notas, sep = "\n" )"""
