from collections import defaultdict,deque
class Solution:
    def bottomView(self, root):
        q = deque()
        dic = defaultdict(int)
        q.append([root,0]) # [node,level]
        res = []
        while q:
            node , x = q.popleft()
            dic[x] = node.val
            if node.left is not None:
               q.append([node.left,x-1])
            if node.right is not None:
               q.append([node.right,x+1])
        for x in sorted(dic.keys()):
           res.append(dic[x])
        return res