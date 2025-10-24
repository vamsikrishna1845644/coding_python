class Solution:
    def dijkstra(self, V, adj, S):
        # Dijkstra's Algorithm using a Set data structure (conceptually)
        # -------------------------------------------------------------
        # In theory, using a set instead of a priority queue can sometimes
        # give better efficiency for certain operations, depending on the graph.
        # The overall logic remains the same as the priority queue version:
        #   1. Maintain a distance array to store the shortest known distance 
        #      to each node.
        #   2. Use a data structure (set or PQ) to always extract the node 
        #      with the smallest distance next.
        #
        # However:
        # - In C++, a balanced tree-based set (like std::set) can efficiently
        #   maintain sorted order, allowing easy extraction of the smallest element.
        # - In Python, the built-in `set` is *unordered* and implemented using hashing.
        #   This means:
        #       -> Elements are not stored in sorted order.
        #       -> You can’t directly access or iterate by ascending order.
        #       -> So, Python’s `set` cannot replace C++’s `std::set` in Dijkstra.
        #
        # Therefore, in Python we stick with a priority queue (`heapq`) implementation.
        # Once you’re comfortable with DSA and want to optimize further,
        # you can try the `set` implementation in C++.

        # Initialize distance array with "infinity" (10e9 used here)
        dist = [10e9] * V

        # Distance of the source node from itself is always 0
        dist[S] = 0

        # Conceptually, we would push [distance, node] = [0, S] into the set
        # But since Python lacks an ordered set, we'll skip actual implementation here
        # and rely on the priority queue version instead.

