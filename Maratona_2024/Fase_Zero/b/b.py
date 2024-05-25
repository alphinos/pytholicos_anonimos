from collections import deque

# def dfs( graph, size, node, K ):
#     visited = [ False ] * size
#     distances = [ -1 ] * size

#     stack = deque()

#     visited[ node ] = True
#     distances[ node ] = 0

#     stack.append( (0, node) )

#     amt_hours = 0
#     amt_visited = 0

#     while stack:
#         h, removed_node = stack.pop(  )
#         amt_hours += h
#         amt_visited += 1
#         if amt_visited == K:
#             break

#         for c, w in graph[ removed_node ]:
#             if not visited[ w ]:
#                 distances[ w ] = distances[ removed_node ] + 1
#                 visited[ w ] = True
#                 stack.append( ( c, w ) )
    
#     return amt_hours

def bfs( graph, size, node, K ):
    visited = [ False ] * size
    distances = [ -1 ] * size

    alpha = [ None ] * size

    queue = deque()

    visited[ node ] = True
    distances[ node ] = 0

    amt_hours = 0
    amt_visited = 0

    queue.append( ( 0, node ) )

    while queue:
        h, removed_node = queue.popleft(  )
        amt_hours += h
        amt_visited += 1
        if amt_visited == K:
            break

        for c, w in graph[ removed_node ]:
            if not visited[ w ]:
                distances[ w ] = distances[ removed_node ] + 1
                visited[ w ] = True
                alpha[ w ] = removed_node
                queue.append( ( c, w ) )

    return amt_hours

N, M, K = map( int, input().split() )

grafo = { n : list() for n in range( N ) }

for _ in range( M ):
    u, v, C = map( int, input().split() )
    grafo[ u - 1 ].append( ( C, v - 1 ) )
    grafo[ v - 1 ].append( ( C, u - 1 ) )

print( bfs( grafo, N, 0, K ) )
# def bfs( graph, size, node, K ):
#     visited = [ False ] * size
#     distances = [ -1 ] * size

#     alpha = [ None ] * size

#     queue = deque()

#     visited[ node ] = True
#     distances[ node ] = 0

#     amt_hours = 0

#     queue.append( node )

#     while queue:
#         if amt_hours >= K:
#             break

#         removed_node = queue.popleft(  )

#         for c, w in graph[ removed_node ]:
#             if not visited[ w ]:
#                 distances[ w ] = distances[ removed_node ] + 1
#                 visited[ w ] = True
#                 alpha[ w ] = removed_node
#                 queue.append( w )
#                 amt_hours += c
    
#     print( distances )

#     return amt_hours

# def path( alpha, u, v ):
#     path = []
    
#     while u != v:
#         if not alpha[ v ]:
#             break
#         path.append( v )
#         v = alpha[ v ]

#     path.append( u )
#     return path

# def dijkstra( edges, start, K ):
#     visited = [ False ] * N
#     distances = [ INF ] * N
#     distances[ start ] = 0

#     priority_queue = [ ( 0, start[ 0 ], start[ 1 ] ) ]

#     amt_hours = 0
#     amt_visited = 0

#     while priority_queue:
#         curr_distance, curr_vertex = heapq.heappop( priority_queue )
#         if not visited[ curr_vertex ]:
#             visited[ curr_vertex ] = True
#             amt_visited += 1
#             amt_hours = curr_distance
#         if amt_visited == K:
#             break

#         for c, v in edges[ curr_vertex ]:
#             distance = curr_distance + c

#             if not visited[ v ] and distances[ v ] > distances[ curr_vertex ] + c:
#                 distances[ v ] = distances[ curr_vertex ] + c
#                 heapq.heappush( priority_queue, ( distance, v ) )

#     return amt_hours

# edges = { n : list() for n in range( N ) }