from typing import List
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # i think this is a graphs question
        # doing this witth a vague idea

        # my idea is wrong
        # given as string 

        # coding by seeing hints
        n = len(bank)
        m = len(bank[0])
        arr= [0]*n
        for i in range(n):
            for j in range(m):
                if bank[i][j] == '1':
                    arr[i]+=1
        
        # now i have arr with each elemnt representing no of devices in each row

        # now have to find product between adj elents leaving 0 device elments
        ans = []
        for element in arr:
            if element!=0:
                ans.append(element)
        
        # find the product of adj elements and add them
        pointer1 = 0
        pointer2 = 1
        result = 0
        while pointer2<len(ans):
            mul = ans[pointer1]*ans[pointer2]
            result+=mul
            pointer1+=1
            pointer2+=1
        
        return result

sol = Solution()
print(sol.numberOfBeams(["000","111","000"]))