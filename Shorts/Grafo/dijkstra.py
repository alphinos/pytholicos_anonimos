import heapq

INF = 10**9

def dijkstra( vertices, edges, weights, start ):
    predecessors = { v : None for v in edges }
    distances = { v : INF for v in vertices }
    distances[ start ] = 0

    priority_queue = [ ( 0, start ) ]

    while priority_queue:
        curr_distance, curr_vertex = heapq.heappop( priority_queue )

        for v in edges[ curr_vertex ]:
            weight = weights[ ( curr_vertex, v ) ]
            distance = curr_distance + weight

            if distances[ v ] > distances[ curr_vertex ] + weights[ ( curr_vertex, v ) ]:
                distances[ v ] = distances[ curr_vertex ] + weights[ ( curr_vertex, v ) ]
                predecessors[ v ] = curr_vertex
                heapq.heappush( priority_queue, ( distance, v ) )
    
    return predecessors, distances

vertices = set()
edges = dict()
weights = dict()

N, M = map( int, input().split() ) # N vértices, M arestas
vertices = set( input().split() )
start = input()
for _ in range( M ):
    u, v, w = input().split()
    w = int( w )
    edges[ u ] = v
    weights[ ( u, v ) ] = w

preds, dists = dijkstra( vertices, edges, weights, start )

print( preds )

print( dists )

"""
9 14
a b c d e f g h i
a
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
"""
