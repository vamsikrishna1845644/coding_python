import copy
from typing import List
from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i, num in enumerate(nums):
            if num != 0:
                continue

            for start_dir in [-1, 1]:  # -1 = left, 1 = right
                temp = nums[:]
                pos = i
                direc = start_dir

                while 0 <= pos < n:
                    if temp[pos] == 0:
                        pos += direc
                    else:
                        temp[pos] -= 1
                        direc *= -1  # reverse direction
                        pos += direc

                if sum(temp) == 0:
                    ans += 1

        return ans

sol= Solution()
print(sol.countValidSelections([1,0,2,0,3]))




                


