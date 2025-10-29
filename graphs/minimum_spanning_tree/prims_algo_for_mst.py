# 🌳 Spanning Tree:
# A spanning tree of a connected, undirected graph is a subgraph that:
# 1. Includes all vertices of the original graph
# 2. Has exactly (V - 1) edges (where V is the number of vertices)
# 3. Contains no cycles (i.e., forms a tree)

# 👉 In short:
# A spanning tree connects all vertices with the minimum number of edges and no cycles.

# 🏗️ Minimum Spanning Tree (MST):
# A Minimum Spanning Tree is a spanning tree in which the total sum of edge weights
# is the smallest possible among all spanning trees of the graph.

# 👉 In other words:
# It connects all the vertices with the least total edge cost and no cycles.

# ⚙️ Algorithms to find MST:
# 1. Kruskal's Algorithm → Uses sorting + Disjoint Set (Union-Find)
# 2. Prim's Algorithm → Uses a Priority Queue (similar to Dijkstra’s algorithm)

# Example:
# For a weighted graph with 4 nodes,
# The MST is the subset of edges that connects all nodes
# with no cycles and the lowest possible total weight.
import heapq

class Solution:
    def spanningTree(self, V, adj):
        # Minimum Spanning Tree (MST) using Prim's Algorithm
        # Time Complexity: O(E log V)
        # Space Complexity: O(V)
        
        vis = [0] * V            # visited array
        pq = []                  # min-heap: stores (edge_weight, node)
        total_weight = 0         # stores total weight of MST

        # start with node 0 and edge weight 0
        heapq.heappush(pq, (0, 0))

        while pq:
            weight, node = heapq.heappop(pq)

            if vis[node]:
                continue   # skip if node already added to MST

            vis[node] = 1
            total_weight += weight

            # Explore all adjacent nodes
            for neighbour_node, edge_weight in adj[node]:
                if not vis[neighbour_node]:
                    heapq.heappush(pq, (edge_weight, neighbour_node))

        return total_weight
        # If you want the actual MST edges,
        # you can store (parent, node, weight) whenever you add a new edge




