import heapq

INF = 8761  # Ensure this is a high enough value for the problem's constraints

def dijkstra(graph, start):
    predecessors = {v: None for v in graph}
    distances = {v: INF for v in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        curr_distance, curr_vertex = heapq.heappop(priority_queue)

        if curr_distance > distances[curr_vertex]:
            continue

        for c, v in graph[curr_vertex]:
            distance = curr_distance + c

            if distance < distances[v]:
                distances[v] = distance
                predecessors[v] = curr_vertex
                heapq.heappush(priority_queue, (distance, v))
    
    return predecessors, distances

N, M, K = map(int, input().split())

edges = {n + 1: [] for n in range(N)}

for _ in range(M):
    u, v, C = map(int, input().split())
    edges[u].append((C, v))
    edges[v].append((C, u))

preds, dists = dijkstra(edges, 1)

# Convert distances dictionary to list of tuples and sort
dists_list = sorted(dists.items(), key=lambda e: e[1])
print( dists_list )

h = 0
for d in dists_list:
    h += 1
    if h == K:
        if d[0] != 1:
            d_a = d[1] - dists[preds[d[0]]]
        else:
            d_a = d[1]
        print(d_a)
        break

"""
7 11 5
1 4 0
3 4 3
4 5 2
3 5 8
1 5 5
3 2 9
5 2 8
1 2 2
5 6 9
2 6 9
6 7 0
"""
