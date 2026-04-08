import heapq

def get_min_max_latency(n, clients, edges):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    servers = [i for i in range(1, n + 1) if i not in clients]
    best_latency = float('inf')

    for server in servers:
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[server] = 0
        pq = [(0, server)]

        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))

        current_max = 0
        for client in clients:
            if dist[client] > current_max:
                current_max = dist[client]

        if current_max < best_latency:
            best_latency = current_max

    return best_latency

def main():
    try:
        with open('gamsrv.in', 'r') as f:
            lines = f.readlines()
            
        if not lines:
            return

        n, m = map(int, lines[0].split())
        clients = list(map(int, lines[1].split()))
        edges = []

        for i in range(2, 2 + m):
            u, v, w = map(int, lines[i].split())
            edges.append((u, v, w))

        result = get_min_max_latency(n, clients, edges)

        with open('gamsrv.out', 'w') as f:
            f.write(str(result) + '\n')
            
    except FileNotFoundError:
        pass


main()