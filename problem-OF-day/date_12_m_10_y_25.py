from typing import List
from collections import defaultdict
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        # doing this using a hashmap
        #dont know how else can i optimise it
        total_sum = sum(power)
        dic = defaultdict(int)
        for num in power:
            if num in dic:
                dic[num]+=1
            else:
                dic[num] = 1
        
        for num in power:
            for k in [1,-1,2,-2]:
                if num+k in dic and dic[num+k]>0:
                    total_sum-=num+k
                    dic[num+k]-=1
                if num+k in dic and dic[num+k] == 0:
                    del dic[num+k]
        return total_sum
sol = Solution()
print(sol.maximumTotalDamage([7,1,6,6]))

            

