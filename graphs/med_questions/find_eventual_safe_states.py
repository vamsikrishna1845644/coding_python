from collections import deque 
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # actually this question should be done using cycle detection in directed graph using dfs
        # we use pathvis and vis array 
        # but i got lazy and havent done this question
        #so doing this now using topo sort(bfs)

        #  first wwe know that topo sort takes indegree into consideration
        # but in this question terminal node is a node who has no outgoing edges
        # and safe nodes should be conneted to terminal node via a path with no cycles in between
        # so to use our indegree logic here , we need to reverse the graph 
        # that is element -> neighbour , we do neighbour -> element
        # by doing this terminals nodes become the nodes with zero indegree 
        # so from that we can apply our topo sort and minius the indegree of termianl node's neighbours by 1
        #  and so on
        # so we are practically bactracking form the terminal node
        # and as we minus thier indegree by 1 in each iteretion , we can find the safe nodes connected to the termianl nodes

        # reversed adjlist
        adjrev= [[] for _ in range(len(graph))]
        #indegree list
        indegree = [0]*len(graph)
        # reverse the adj list
        for node in range(len(graph)):
            for neighbour in graph[node]:
                adjrev[neighbour].append(node) # neighbour -> node
                # here only we can also calculate indegre as node's indegree is increased by 1
                indegree[node]+=1 
        
        # now we have our adjrev and indegree

        # now lets start our topo sort

        # initialise the queue
        q = deque()

        # also the ans
        ans= []

        # check for elements having zero indegree and add them to our queue
        for node in range(len(graph)):
            if indegree[node] == 0:
                # add that node to the queue
                q.append(node)

        while q:
            ele = q.popleft()

            # add the element to ans
            ans.append(ele)

            for neighbour in adjrev[ele]:
                # minus their indegree by 1
                indegree[neighbour]-=1
                # check if any of their indegree has became zero or not
                if indegree[neighbour] == 0:
                    # if yes then add them to the queue
                    q.append(neighbour)
        
        # return the ans in sorted way
        return sorted(ans)


