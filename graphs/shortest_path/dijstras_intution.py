# Dijkstra's algorithm can be implemented using:
# 1. Simple Queue (BFS-style)
# 2. Priority Queue (heap)
# 3. Set (like C++ std::set)

# Using a simple queue:
# - Processes nodes in the order they were added.
# - Explores all possible paths, even longer ones.
# - Nodes may be visited multiple times unnecessarily.
# - Time complexity can be high: O(V^2 + E)
# - Suitable mainly for unweighted graphs.

# Using a priority queue:
# - Always selects the node with the minimum current distance.
# - Follows a greedy approach: explore the most promising nodes first.
# - Skips unnecessary paths; updates distances only if a shorter path is found.
# - Very efficient: O((V + E) log V)
# - Ideal for weighted graphs with non-negative weights.

# Key difference:
# - Queue: FIFO → may explore suboptimal paths.
# - Priority Queue: greedy → always explores shortest distance first.


