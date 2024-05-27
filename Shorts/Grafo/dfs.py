from collections import deque

def dfs( graph, size, node ):
    visited = [ False ] * size
    distances = [ -1 ] * size

    stack = deque

    visited[ node ] = True
    distances[ node ] = 0

    stack.append( node )

    while stack:
        removed_node = stack.pop(  )

        for w in graph[ removed_node ]:
            if not visited[ w ]:
                distances[ w ] = distances[ removed_node ] + 1
                visited[ w ] = True
                stack.append( w )
    
    return visited, distances