import copy
class Solution:
    def shortestDistance(self, matrix):
        # coding this using floyd warshell algo
        # this algo is applicable for negative weights grpah
        # and also to detect negative cycles
        # this algo is used when u want to find shortest distance between any two nodes
        # otherwise its useless
        # dijstras and bellman ford are used when u want shortest distance between 1 source and 
        # all the other nodes
        # this algo is very time costly o(v^3) v-> no of nodes

        # quite easy algo 
        # find the shortest path through a node for all the other nodes and update it
        # do this for all the nodes

        # to store the shortest dist between each node to node 
        # initialsie a adj matrix
        # but the matrix given in question it self is a adj matrix
        # if no direct path its represnted by -1 in this matrix
        # to return our ans make a copy of this matrix
        ans = copy.deepcopy(matrix) # copy of all rows and cols # we should make a deepcopy


        no_of_nodes = len(matrix)
        # start -> node -> end if found a shorter path update it

         # convert -1 to inf
        for i in range(no_of_nodes):
            for j in range(no_of_nodes):
                if ans[i][j] == -1:
                    ans[i][j] = float('inf')
                if i == j:
                    ans[i][j]=0 # just in case




        for node in range(no_of_nodes):
            for start in range(no_of_nodes):
                for end in range(no_of_nodes):

                    if ans[start][node] != float('inf') and ans[node][end] != float('inf'):
                        path_length_through_node = ans[start][node] + ans[node][end]
                        # update the lenght if the found path _lenght_through_node is smaller 
                        # than previous
                        # update if minimum is found
                        
                        ans[start][end] = min(ans[start][end],path_length_through_node)
        
        # convert inf to -1 ( all these to match the question)
        for i in range(no_of_nodes):
            for j in range(no_of_nodes):
                if ans[i][j] == float('inf'):
                    ans[i][j] = -1
        
        return ans
sol = Solution()
matrix = [[0, 2, -1, -1],[1, 0, 3, -1],[-1, -1, 0, 1],[3, 5, 4, 0]]
print(sol.shortestDistance(matrix))

