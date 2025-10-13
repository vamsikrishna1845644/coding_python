def iscycle(V,adj):
    vis = [0]*V # vsisted array
    return dfs(vis,adj,0,-1) # node.parent
def dfs(vis,adj,node,parent):
    # mark it as visited
    vis[node] = 1

    # loop through each of the neighbours
    for neighbour in adj[node]:
        if not vis[neighbour]: # not vsisted
            # mark it as visted
            vis[neighbour] = 1
            # go to the depth of it
            if dfs(vis,adj,neighbour,node):
                return True # if one single call return true return true for all of them no need to check for others
        elif neighbour != parent: # if neighbour is not the parent itself 
            # we have etected a loop
            return True
    # if it comes here 
    # we detected no loop
    return False

edges = [[0, 1], [0, 2], [2, 3]]
V = 4
adj = [[] for _ in range(V)]
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

print(iscycle(V,adj))

# for connected compinets u know thw gig
# do it vueslef


