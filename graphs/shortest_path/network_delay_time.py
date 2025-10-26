import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Problem: Find the minimum time required for a signal
        # to travel from the source node 'k' to all other nodes.
        # If even one node cannot be reached, return -1.

        # Step 1: Create an adjacency list for the directed graph
        adj = [[] for _ in range(n + 1)]  # using 1-based indexing

        for time in times:
            source = time[0]
            destination = time[1]
            signal_time = time[2]
            adj[source].append([destination, signal_time])

        # Step 2: Declare a priority queue (min-heap) for Dijkstra's algorithm
        pq = []
        heapq.heappush(pq, (0, k))  # (time so far, current node)

        # Step 3: Create a distance array to store minimum signal time for each node
        dist = [int(10e9)] * (n + 1)  # 1-based indexing
        dist[k] = 0  # signal takes 0 time to reach the source itself

        # Step 4: Dijkstra's algorithm (using priority queue)
        while pq:
            curr_time, node = heapq.heappop(pq)

            # Traverse all neighbours of the current node
            for neighbour in adj[node]:
                neighbour_node = neighbour[0]
                edge_weight = neighbour[1]

                # If a shorter path to neighbour is found, update it
                if edge_weight + curr_time < dist[neighbour_node]:
                    dist[neighbour_node] = edge_weight + curr_time
                    heapq.heappush(pq, (dist[neighbour_node], neighbour_node))

        # Step 5: After processing all nodes, check if all were reachable
        max_time = max(dist[1:])  # ignore index 0 (1-based indexing)

        if max_time == int(10e9):
            return -1  # at least one node was not reachable
        else:
            return max_time  # time taken for signal to reach the farthest node




