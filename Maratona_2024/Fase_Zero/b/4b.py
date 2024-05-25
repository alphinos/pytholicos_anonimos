import heapq

INF = 8761

def dijkstra( graph, start ):
    predecessors = [ ( v, None ) for v in graph ]
    distances = [ ( v, INF ) for v in graph ]
    distances[ start - 1 ] = ( start, 0 )

    priority_queue = [ ( 0, start ) ]

    while priority_queue:
        curr_distance, curr_vertex = heapq.heappop( priority_queue )

        for c, v in graph[ curr_vertex ]:
            distance = curr_distance + c

            if distances[ v - 1 ][ 1 ] > distances[ curr_vertex - 1 ][ 1 ] + c:
                distances[ v - 1 ] = (curr_vertex, distances[ curr_vertex - 1 ][ 1 ] + c)
                predecessors[ v - 1 ] = ( v, curr_vertex )
                heapq.heappush( priority_queue, ( distance, v ) )
    
    return predecessors, distances

N, M, K = map( int, input().split() )

edges = { n + 1 : list() for n in range( N ) }

for _ in range( M ):
    u, v, C = map( int, input().split() )
    edges[ v ].append( ( C, u ) )
    edges[ u ].append( ( C, v ) )

preds, dists = dijkstra( edges, 1 )

# print( preds, dists )

dists = sorted( dists, key = lambda e : e[ 1 ] )

# print( dists )

h = 0
for d in dists:
    h += 1
    if h == K:
        if d[0] != 1:
            d_a = d[ 1 ] - dists[ preds[ d[ 0 ] - 1 ][ 1 ] ][ 1 ]
        else:
            d_a = d[ 1 ]
        print( d_a )
        break
