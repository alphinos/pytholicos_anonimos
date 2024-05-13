N = int( input() )

ganha = "N"

for i in range( N ):
    a, b = map( int, input().split() )

    if not (a == 1 and b == 2 or a == 2 and b == 1):
        ganha = "Y"

print( ganha )