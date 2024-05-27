import heapq

def prim( graph, maxn, w, r ):
    p = { k : maxn + 1 for k in graph }
    pi = { k : -1 for k in graph }

    p[ r ] = 0

    heap = [ ( 0, r ) ]
    in_heap = { k : False for k in graph }
    in_heap[ r ] = True

    S = []

    while heap:
        _, u = heapq.heappop( heap )
        S.append( u )

        for v in graph[ u ]:
            if not in_heap[ v ] and ( p[ v ] > w[ (u, v) ] ):
                p[ v ] = w[ (u, v) ]
                pi[ v ] = u
                heapq.heappush( heap, ( p[ v ], v ) )
                in_heap[ v ] = True

                print( u, v )
    
    return S, pi

graph = dict(  )
w = dict(  )

ps = [  ]

while True:
    try:
        u, v, p = input().split()
        if not graph.get( u ):
            graph[ u ] = []
        if not graph.get( v ):
            graph[ v ] = []
        

        p = int( p )
        graph[ u ].append( v )
        graph[ v ].append( u )
        w[ ( u, v ) ] = p
        w[ ( v, u ) ] = p

        ps.append( p )     
    except:
        break

S, pi = prim( graph, max( ps ), w, 'a' )

print( S )
print( pi )

"""
a b 4
a h 8
b c 8 
b h 11
c i 2
c f 4
c d 7
d e 9 
d f 14
e f 10
f g 2
g i 6
g h 1
i h 7
aaaaa
"""