from collections import deque

def bfs( graph, size, node, D ):
    visited = [ False ] * size
    distances = [ -1 ] * size

    alpha = [ None ] * size

    queue = deque()

    visited[ node ] = True
    distances[ node ] = 0

    queue.append( node )

    while queue:
        removed_node = queue.popleft(  )

        for w in graph[ removed_node ]:
            if not visited[ w ]:
                distances[ w ] = distances[ removed_node ] + 1
                visited[ w ] = True
                alpha[ w ] = removed_node
                queue.append( w )
    
    print( distances )

    return visited, distances, alpha

def path( alpha, u, v ):
    path = []
    
    while u != v:
        if not alpha[ v ]:
            break
        path.append( v )
        v = alpha[ v ]

    path.append( u )
    return path

N, M, D = map( int, input().split() )

grafo = { n : list() for n in range( N ) }

for _ in range( M ):
    u, v = map( int, input().split() )
    grafo[ u - 1 ].append( v - 1 )

max_size = 0
for v in grafo:
    _, dists, _ = bfs( grafo, N, v, D )
    curr_s = max( dists )
    if curr_s > max_size:
        max_size = curr_s

print( max_size )