N = int( input() )
K = int( input() )

participantes = [ int( input() ) for _ in range( N ) ]
participantes.sort(  )

pont = N - K
status = True

classifcs = K

while status and pont > 0:
    if participantes[ pont ] == participantes[ pont - 1 ]:
        pont -= 1
        classifcs += 1
    else:
        status = False

print( classifcs )