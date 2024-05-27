from collections import deque

def bfs( graph, size, node ):
    visited = [ False ] * size
    distances = [ -1 ] * size

    alpha = [ None ] * size

    queue = []

    visited[ node ] = True
    distances[ node ] = 0

    deque.append( queue, node )

    while queue:
        removed_node = deque.popleft( queue )

        for w in graph[ removed_node ]:
            if not visited[ w ]:
                distances[ w ] = distances[ removed_node ] + 1
                visited[ w ] = True
                alpha[ w ] = removed_node
                deque.append( w )
    
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
