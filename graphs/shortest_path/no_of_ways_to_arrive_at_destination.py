import heapq
from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Count the number of shortest paths from node 0 to node n-1
        # Using a modified Dijkstra's algorithm
        MOD = 10**9 + 7

        # Step 1: Build adjacency list (bidirectional graph)
        adj = [[] for _ in range(n)]
        for road in roads:
            start, end, cost = road[0], road[1], road[2]
            adj[start].append([end, cost])
            adj[end].append([start, cost])  # road is bidirectional

        # Step 2: Initialize distance and ways arrays
        dist = [int(1e18)] * n   # shortest distance to each node
        ways = [0] * n           # number of shortest paths to each node

        dist[0] = 0   # distance to source node = 0
        ways[0] = 1   # only 1 way to start at node 0

        # Step 3: Initialize min-heap for Dijkstra
        pq = []
        heapq.heappush(pq, (0, 0))  # (current distance, node)

        # Step 4: Dijkstra traversal
        while pq:
            curr_distance, node = heapq.heappop(pq)

            # Explore all neighbors of current node
            for neighbour_node, edge_weight in adj[node]:
                new_distance = curr_distance + edge_weight

                # Case 1: Found a shorter path to neighbor
                if new_distance < dist[neighbour_node]:
                    dist[neighbour_node] = new_distance        # update shortest distance
                    ways[neighbour_node] = ways[node]         # reset ways to reach neighbor
                    heapq.heappush(pq, (new_distance, neighbour_node))  # add neighbor to PQ

                # Case 2: Found another shortest path with same distance
                elif new_distance == dist[neighbour_node]:
                    ways[neighbour_node] = (ways[neighbour_node] + ways[node]) % MOD
                    # no need to push neighbor to PQ again

        # Step 5: Return total number of shortest paths to destination
        return ways[n-1]

                