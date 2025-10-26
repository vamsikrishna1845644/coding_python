from collections import deque
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # n → number of cities (nodes)
        # k → maximum number of stops allowed
        # src → starting city
        # dst → destination city
        # flights → list of flights [start, end, cost]

        # Step 1: Create an adjacency list to represent the graph
        adj = [[] for _ in range(n)]
        for flight in flights:
            source = flight[0]
            destination = flight[1]
            cost = flight[2]
            adj[source].append([destination, cost])
        # Each node stores (neighbour, cost) pairs

        # Step 2: Create a distance array to store the minimum cost to reach each city
        dist = [int(10e9)] * n
        dist[src] = 0  # cost to reach source city is always 0

        # Step 3: Initialize a queue for BFS → (stops, current_city, total_cost)
        q = deque()
        q.append((0, src, 0))

        # Step 4: Perform BFS traversal (level = stops)
        while q:
            stops, node, cost = q.popleft()

            # If we have already taken more than k stops, skip this path
            if stops > k:
                continue

            # Step 5: Explore all neighbouring cities connected to the current city
            for neighbour in adj[node]:
                neighbour_node = neighbour[0]
                edge_weight = neighbour[1]

                # If we find a cheaper way to reach this neighbour, update and continue
                if cost + edge_weight < dist[neighbour_node] and stops <= k:
                    dist[neighbour_node] = cost + edge_weight
                    # Add this neighbour to the queue for further exploration
                    q.append((stops + 1, neighbour_node, cost + edge_weight))

        # Step 6: If destination is reachable, return its cost; otherwise, return -1
        if dist[dst] != 10e9:
            return dist[dst]
        else:
            return -1

