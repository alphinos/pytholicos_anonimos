def get_tokens( tokens : list, cl : str ):
    state = 0
    token = ''

    for c in cl:
        if state == 0:
            if c =='x':
                state = 1
            elif c == 'n':
                token += c
                state = 2
        elif state == 1:
            if c.isdigit ():
                token += c
            else:
                state = 3
        elif state == 2:
            if c == 'o' or c == 't':
                token += c
            else:
                state = 3
        else:
            tokens.append( token )
            token = ''

M, N = map( int, input().split() )

cls = [ [ 0 ] ]
literais = [ None ] * ( N + 1 )
literais[ 0 ] = False

for m in range( M ):
    tokens = []
    cl = input()

    get_tokens( tokens, cl )

    flag_not = False

    prev_literal = cls[ m ][ 0 ]
    prev_not = False
    if prev_literal == 'not':
        prev_not = True
        prev_literal = cls[ m ][ 1 ]

    prev = literais[ prev_literal ]

    for t in tokens:
        if t == prev_literal:
            continue
        if t == 'not':
            flag_not = True
            continue

        if prev_not:
            if flag_not:
                literais[ t ] = prev
            else:
                literais[ t ] = not prev
        else:
            if flag_not:
                literais[ t ] = False
            else:
                literais[ t ] = True

        if prev and not literais[ t ]:
            pass