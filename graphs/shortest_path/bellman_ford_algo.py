class Solution:
    def bellman_ford(self, V, edges, S):
        # in this i try to code bellman ford algo 

        # in this algo we need to relax edges
        # this algo works for negative weighted graphs also unlike 
        # dijstras algo
        # it can also detect negative weighted cycles in our grph
        # note that a negative weighted cyclic graph has no shortest path solution
        # so its imp to indentify them
        # this algo mainly works on directed graphs 
        # but by converting un directed grphs into directed(by adding edges from a-> b and b -> a)
        # this algo can work for undirected graphs also

        # we dont need a adj list for this 
        # we just need the edges from whom to whom and what edge weight
        # note: the edges can be in any order this algo works fine

        # step 1 create a dist array with 10e9
        dist =  [int(10e9)]*V
        # mark the source dist as zero
        dist[S] = 0
        # we need to do V-1 iterations 
        # in each iteration , we need to check relaxation for all the edges
        for _ in range(V-1): 
            # for each iteration 
            # check relation for all edges
            # add a flag for optimization
            updated = False
            for edge in edges:
                start = edge[0]
                end = edge[1]
                weight = edge[2]

                # for each edge 
                # check relaxtion
                if dist[start]!=int(10e9) and  dist[start]+weight<dist[end]:
                    # relaxtion is possible
                    # do the relaxtion
                    dist[end] = dist[start]+weight
                    # update the flag as relaxtion occured
                    updated = True
                else:
                    #if relaxtion is not possible do nothing
                    continue
            # if in any itertaion no updation occured
            #  it means that the shortest distance for all nodes from
            # the source node has been found
            # no need to check further 
            # waste of time 
            # optimization
            if updated == False:
                # no need to check for further
                # break out of loop
                break
        # we have done v-1 itertaions 
        # if this graph doesnot have negative cycle 
        # then thats it this is the algo
        # but in the question they also asked us to find if the grapsh contains negative cycle
        #  if yes then , we should return -1

        # to check this we need to do one more itertation
        # if the relaxtion happens in this iteration then it means the 
        # grapsh contains a negative cycle 
        # because we know for a non negative cycle graph 
        # all relaxtion should happen in v-1 itertaions in the worst case

        # if agin in the vth itertaion relaxtion is happening then it means 
        # the graphs contains a negative cycle

        # 1 more itertaion for checking the cycle

        for edge in edges:
                start = edge[0]
                end = edge[1]
                weight = edge[2]

                # for each edge 
                # check relaxtion
                if dist[start]!=int(10e9) and  dist[start]+weight<dist[end]:
                    # relaxtion is possible
                    # cycle exist
                    return [-1] # return -1 and break out 
                
                else:
                    #if relaxtion is not possible do nothing
                    continue
        # we came here means no relaxtion  occured in last itertaion 
        # so no cycle return ans
        return dist

sol = Solution()
V = 6
edges = [[3, 2, 6], [5, 3, 1], [0, 1, 5], [1, 5, -3], [1, 2, -2], [3, 4, -2], [2, 4, 3]]
S = 0
print(sol.bellman_ford( V, edges, S))



