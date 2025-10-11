from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) <3:
            return 2
        # doing this
        p1 = 0
        p2 = 1
        ind = 2
        lenght = 2
        maxi = 2
        while ind<=(len(nums) - 1):
            if nums[p1]+nums[p2] == nums[ind]:
                lenght+=1
                maxi = max(maxi,lenght)

            else:
                lenght = 2
            p1+=1
            p2+=1
            ind+=1
        return maxi
sol = Solution()
print(sol.longestSubarray([1, 2, 3, 7, 10, 17, 27]))
