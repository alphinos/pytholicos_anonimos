import heapq

INF = 8761

N, M, K = map( int, input().split() )

def dijkstra( edges, start, K ):
    visited = [ False ] * N
    distances = [ [0, INF] ] * N
    distances[ start ] = [ 0, 0 ]

    priority_queue = [ ( 0, start ) ]

    amt_hours = 0
    amt_visited = 0

    while priority_queue:
        curr_distance, curr_vertex = heapq.heappop( priority_queue )
        print( curr_vertex )
        if not visited[ curr_vertex ]:
            visited[ curr_vertex ] = True
            amt_visited += 1
            amt_hours = distances[ curr_vertex ][ 0 ]
        if amt_visited == K:
            break

        for c, v in edges[ curr_vertex ]:
            distance = curr_distance + c

            if not visited[ v ] and distances[ v ][ 1 ] >= distances[ curr_vertex ][ 1 ] + c:
                distances[ v ][ 1 ] = distances[ curr_vertex ][ 1 ] + c
                distances[ v ][ 0 ] = c
                heapq.heappush( priority_queue, ( distance, v ) )

        print( priority_queue )

    return amt_hours

edges = { n : list() for n in range( N ) }

for _ in range( M ):
    u, v, C = map( int, input().split() )
    edges[ u - 1 ].append( ( C, v - 1 ) )
    edges[ v - 1 ].append( ( C, u - 1 ) )

print( dijkstra( edges, 0, K ) )