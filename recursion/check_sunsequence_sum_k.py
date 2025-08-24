class Solution:
    def checkSubsequenceSum(self, nums, k):
        # we need to use functional recurion
       return self.recursive(nums,k,0,0,[])
    def recursive(self, nums ,k,index,sum,temp):
        n = len(nums)
        # base case
        if index >=n:
            if sum == k:
                return True
            else :
                return False
            
        # take
        temp.append(nums[index])
        sum+=nums[index]
        if(self.recursive(nums,k,index+1,sum,temp) == True):
            return True
        # not take
        temp.pop()
        sum-=nums[index]
        if(self.recursive(nums,k,index+1,sum,temp) == True):
            return True
        return False
