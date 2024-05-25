import heapq

N, M, K = map( int, input().split() )

edges = list()
visited = set()
chega = [ 0 ] * ( N + 1 )

for _ in range( M ):
    u, v, C = map( int, input().split() )
    heapq.heappush( edges, ( C, u, v ) )
    if C > chega[ u ]:
        chega[ u ] = C
    
    if C > chega[ v ]:
        chega[ v ] = C

amt_visited = 1
res = 0

chega[ 1 ] = 0
visited.add( 1 )

while edges and amt_visited != K:
    c, u, v = heapq.heappop( edges )

    if not u in visited and not v in visited:
        custo = max( chega[ u ], chega[ v ] ) + c
        heapq.heappush( edges, ( custo, u, v ) )
        continue
    elif not u in visited:
        if chega[ v ] > c:
            heapq.heappush( edges, ( chega[ v ] + c, u, v ) )
            continue
        visited.add( u )
        chega[ u ] = c
    elif not v in visited:
        if chega[ u ] > c:
            heapq.heappush( edges, ( chega[ u ] + c, u, v ) )
            continue
        visited.add( v )
        chega[ v ] = c

    amt_visited += 1
    res = c

print( res )
