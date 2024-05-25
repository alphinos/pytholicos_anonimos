import heapq

def find( parent, i):
    if parent[ i ] != i:
        parent[ i ] = find( parent, parent[ i ] )
    return parent[ i ]
    # son = i
    # while parent[ son ] != son:
    #     son = parent[ i ]
    #     # print( son )
    #     # print( parent )
    #     # input()
    # return parent[ son ]

def union( parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def kruskal( graph, weights, vertices ):
    result = []

    parent = { node : node for node in vertices }
    rank = { node : 0 for node in vertices }

    print( parent )

    edges = []

    for u in graph:
        for v in graph[ u ]:
            heapq.heappush( edges, ( weights[ ( u, v ) ], u, v ) )

    while edges:
        w, u, v = heapq.heappop( edges )
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            result.append( ( u, v, w ) )
            union(parent, rank, x, y)

    return result


graph = dict(  )
vertices = set()
w = dict(  )

ps = [  ]

while True:
    try:
        u, v, p = input().split()
        if not graph.get( u ):
            graph[ u ] = []
        
        if u not in vertices:
            vertices.add( u )

        if v not in vertices:
            vertices.add( v )

        p = int( p )
        graph[ u ].append( v )
        # graph[ v ].append( u )
        w[ ( u, v ) ] = p
        # w[ ( v, u ) ] = p

        ps.append( p )     
    except:
        break

result = kruskal( graph, w, vertices )

print( result )

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