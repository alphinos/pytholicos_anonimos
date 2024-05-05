string = input()

tamanho = 0
alfabeto = set()

for c in string:
    tamanho += 1
    alfabeto.add( c )

diferentes = tamanho
tam_alfabeto = len( alfabeto )

for sub_tam in range( 2, tam_alfabeto + 1 ):
    diff_atual = diferentes

    for i in range( 0, tamanho - sub_tam + 1 ):
        diff = True
        letras_diff = set()

        for j in range( i, i + sub_tam ):
            if string[ j ] in letras_diff:
                diff = False
                break
            else:
                letras_diff.add( string[ j ] )

        if diff is True and len( letras_diff ) == sub_tam:
            diferentes += 1
    
    sub_tam += 1

print( diferentes )