import heapq

class Solution:
    def dijstras(self, adj, V, S):
        """
        adj: adjacency list of graph where adj[u] = [(v, weight), ...]
        V: number of vertices (1-based or 0-based depending on input)
        S: source node (1-based)
        Returns: list containing shortest path from S to V
        """

        # Distance array, initialized with a very large number
        dist = [10**9] * (V + 1)  # +1 if nodes are 1-based
        dist[S] = 0

        # Priority queue (min-heap) for choosing the node with smallest distance
        pq = []
        heapq.heappush(pq, [0, S])  # (distance, node)

        # Parent array to reconstruct the shortest path
        parent = [i for i in range(V + 1)]

        while pq:
            curr_distance, node = heapq.heappop(pq)

            # Explore all neighbors
            for neighbor, edgeweight in adj[node]:
                total_dist = curr_distance + edgeweight

                # If we found a shorter path to neighbor
                if total_dist < dist[neighbor]:
                    dist[neighbor] = total_dist
                    parent[neighbor] = node
                    heapq.heappush(pq, [total_dist, neighbor])

        # Reconstruct path from source S to destination V
        path = []
        node = V
        if dist[V] == 10**9:  # no path exists
            return [-1]

        while node != parent[node]:
            path.append(node)
            node = parent[node]

        path.append(S)
        path.reverse()
        return path
