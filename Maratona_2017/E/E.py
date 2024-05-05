escalas = {
    "do" : [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    "do#" : [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0],
    "re" : [0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    "re#" : [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    "mi" : [0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    "fa" : [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0],
    "fa#" : [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
    "sol" : [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    "sol#" : [1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    "la" : [0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    "la#" : [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    "si" : [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1]
}
chaves = list( escalas.keys() )

N = int( input() )

contador = 0
for i in range( N ):
    nota = int( input() ) % 12
    tirar = []
    for j in escalas:
        if escalas[ j ][ nota - 1 ] == 0:
            tirar.append( j )
    for t in tirar:
        escalas.pop( t )    

if len( escalas ) == 0:
    print( "desafinado" )
else:
    for chave in escalas:
        print( chave )
        break