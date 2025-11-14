from collections import defaultdict
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # first method 
        # using a map , extra space

        d = defaultdict(int)
        # ans array
        ans = []

        # loop through the array
        for num in nums:
            if num not in d:
                d[num]+=1
            elif num in d:
                ans.append(num)
        
        return ans
    def getSneakyNumbers1(self, nums: List[int]) -> List[int]:
        # second menthod using sorting
        nums = sorted(nums)
        # to store ans 
        ans = []

        for i in range(len(nums)-1):

            if nums[i] == nums[i+1]:
                # add to ans 
                ans.append(nums[i+1])
        
        return ans


