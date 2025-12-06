from typing import List
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        ans = float("-inf")
        for pointer1 in range(n):
            max_energy = 0
            pointer2 = pointer1
            while pointer2<n:
                max_energy+=energy[pointer2]
                pointer2+=k
            ans = max(ans,max_energy)
        return ans
    
sol = Solution()
energy = [5,-10,4,3,5,-9,9,-7]
k = 2
print(sol.maximumEnergy(energy,k))