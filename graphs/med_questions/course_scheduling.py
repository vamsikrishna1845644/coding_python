from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # its just topo sort
        # if we have cycle in this directed graph , it means we cannt do all the courses
        # we can ditect a cycle in directed graphs using dfs(done before ) or bfs(topo sort)
        # doing using topo sort

        # firt convert given prerequistes into a adj list

        # decalare adj list
        adj = [[] for _ in range(numCourses)]
        for a,b in prerequisites: # given in question (verify)
            adj[b].append(a) # b-> a
        
        # now we  have the adj list use topo sort to detect the cycle
        # decalre our queue
        q = deque()
        # we just need the count to store the lenght of the topo sorted ans list , if len = numcourses no cycle if not cycle exists
        count= 0

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
            count+=1 # increase the count by 1

            # minus the indegree of ele's neighbours by 1
            for neighbour in adj[ele]: 
                indegree[neighbour]-=1
                # if the newly modified indegree is zero
                # add that neigbour to queue
                if indegree[neighbour] == 0:
                    q.append(neighbour)
        
        # if count = numcourses no cycle
        # if not cycle exists
        # we can finish all courses if no cycle exists -> True
        # if not False
        if count == numCourses: # non cycle exists -> return True
            return True
        else: # cycle exists  return false
            return False


            
