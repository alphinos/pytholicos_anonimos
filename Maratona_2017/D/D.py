from math import sqrt

PRIMOS = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
          41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 ]

despojados = set()

N = int( input() )

N_sqrt = int( sqrt( N ) )



for i, pi in enumerate( PRIMOS ):
    curr = pi
    despojados.add( curr )
    for pj in PRIMOS[ i : ]:
        curr *= pj
        if not ( curr * pj > N_sqrt ):
            despojados.add( curr )
        for pk in PRIMOS[ i + 1 : ]:
            if not ( curr * pk > N_sqrt ):
                despojados.add( curr * pk )

print( len( despojados ) )

divs = set()
for i in range( 1, N_sqrt ):
    if N % i == 0:
        divs.add( i )
        divs.add( N % i )

res = despojados.intersection( divs )

print( len( res ) )