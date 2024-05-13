from math import pow

class Circle:
    def __init__( self, x, y, r ):
        self.x = x
        self.y = y
        self.r = r

def dist( a, b ):
    return pow( a.y - b.y, 2 ) + pow( a.x - b.x, 2 )

def mod( n ):
    return n**2

N = int( input() )

N_2 = 2*N

intersecs = 0

circles = [  ]

X, Y, R = map( float, input().split() )

circles.append( Circle( X, Y, R ) )

for _ in range( N - 1 ):
    X, Y, R = map( float, input().split() )
    
    if intersecs > N_2:
        continue

    circle = Circle( X, Y, R )

    for c in circles:
        D = dist( circle, c )
        if D > mod( circle.r - c.r ) or D < mod( circle.r + c.r ):
           intersecs += 2
        elif D == mod( circle.r - c.r ) or D == mod( circle.r + c.r ):
            intersecs += 1
    
    circles.append( circle )

if intersecs > N_2:
    print( "greater" )
else:
    print( intersecs )