from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # its just extension of course schedule 1
        # here we also need to return the order in which the courses should be taken 
        # if we have cycle in this directed graph , it means we cannt do all the courses
        # we can detect a cycle in directed graphs using dfs(done before ) or bfs(topo sort)
        # doing using topo sort

        # firt convert given prerequistes into a adj list

        # decalare adj list
        adj = [[] for _ in range(numCourses)]
        for a,b in prerequisites: # given in question (verify)
            adj[b].append(a) # b-> a
        
        # now we  have the adj list use topo sort to detect the cycle
        # decalre our queue
        q = deque()
        # we need the order in which the courses should be done so use a list to store the  order
        ans = []

        # indegree list
        indegree = [0]*numCourses

        # populate the indegree list
        for node in range(numCourses):
            for neighbour in  adj[node]:
                indegree[neighbour] += 1 # increase its indegree by one as its attached to the node

        # now our indegree is populated 
        # now check the elements with zero indegree and add them to our queue

        for node in range(numCourses):
            if indegree[node] == 0:
                # add them to the queue
                q.append(node)
        
        # now we have elements having zero indegree in our queue
        # for these element's neigbours minus their indegree by 1 (that is cut their connection with the element) 
        # this is done using bfs
        while q:
            ele = q.popleft()
            ans.append(ele) # add the element to our ans

            # minus the indegree of ele's neighbours by 1
            for neighbour in adj[ele]: 
                indegree[neighbour]-=1
                # if the newly modified indegree is zero
                # add that neigbour to queue
                if indegree[neighbour] == 0:
                    q.append(neighbour)
        

        if len(ans) == numCourses: # no cycle exists  means we can do all the courses , so return the order of doing courses
            return ans
        else: # cycle exists so   return empty list as courses cannot be done
            return []
