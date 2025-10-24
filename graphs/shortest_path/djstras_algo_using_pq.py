import heapq

class Solution:
    def dijkstra(self, V, adj, S):
        # Dijkstra's algorithm (using a priority queue)
        # Finds the shortest distance from a source node 'S' to all other vertices
        # in a non-negative weighted graph.

        # STEP 1: Initialize distance array with infinity (means not yet reachable)
        dist = [10e9] * V
        dist[S] = 0  # Distance to the source is always 0

        # STEP 2: Initialize a min-heap (priority queue)
        # Each element in pq = [distance_from_source, node]
        pq = []
        heapq.heappush(pq, [0, S])

        # STEP 3: Process nodes in increasing order of distance
        while pq:
            curr_dist, node = heapq.heappop(pq)

            # STEP 4: Visit all adjacent nodes
            for neighbour, edge_weight in adj[node]:
                # Calculate new possible distance to this neighbour
                new_dist = curr_dist + edge_weight

                # STEP 5: Relaxation — if the new distance is smaller, update it
                if new_dist < dist[neighbour]:
                    dist[neighbour] = new_dist
                    # Push the updated distance for further processing
                    heapq.heappush(pq, [new_dist, neighbour])

        # STEP 6: Return the final distance array
        return dist





