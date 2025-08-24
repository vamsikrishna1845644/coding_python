class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #  recursive solution 
        # print all sunsequiences 
        # this pattern is important
        # we will use functional recursion 
        # create another function to implement logic
        res = []# main answer
        self.recurive(0,[],res,nums) # (index , temparory_list)
        return res
    def recurive(self, index , temp_list,res,nums):
        n = len(nums)
        # base case
        if (index >= n):
            res.append(temp_list[:]) # append a copy
            return
        # take
        temp_list.append(nums[index])
        self.recurive(index+1,temp_list,res,nums)
        # not take
        temp_list.pop()
        self.recurive(index+1,temp_list,res,nums)

        

