file:///c%3A/Users/ASUS/Desktop/coding_python/subsets_powerset.py {"mtime":1755537484220,"ctime":1755496791221,"size":166,"etag":"3emacap5r5b","orphaned":false,"typeId":""}
class Solution:
    def subsets_powerset(self, nums: List[int]) -> List[List[int]]:
        # non recursive solution -> powerset
        # print all sunsequiences (power set)
        n = len(nums)
        res = []
        for i in range(0,(2**n)):# check the condition
            # loop through all subsets
            # add them to a temp list and add to res list at last
            temp = []
            for j in range(0,n):
                if i & (1 << j) != 0: # check this bit manupulation condition
                    # means the bit is set 
                    # means we should take that element (so add to our list)
                    temp.append(nums[j])
            res.append(temp) # add the subset to answer
        return res