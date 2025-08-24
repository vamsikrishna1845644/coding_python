class Solution:
    def countSubsequenceWithTargetSum(self, nums, k):
        # we need to use functional recurison
        # create another function to take care of recursion
        res = []# result array
        self.recurive(0 , [], 0 , nums , k,res)
        return len(res) # we wwant only lenght
    def recurive(self, index , temp_list,sum, nums, k,res):
        n = len(nums)
        # base case 
        if index >=n:
            if sum == k:
                res.append(temp_list[:]) # add the copy
            return
        
        # take the element
        temp_list.append(nums[index])
        sum+=nums[index] # increase the sum
        self.recurive(index+1,temp_list,sum,nums,k,res)

        # not take the element

        temp_list.pop()
        sum-=nums[index] # decrease the sum
        self.recurive(index+1,temp_list,sum,nums,k,res)


