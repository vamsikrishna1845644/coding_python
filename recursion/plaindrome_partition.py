file:///c%3A/Users/ASUS/Desktop/coding_python/plaindrome_partition.py {"mtime":1755886211371,"ctime":1755886211371,"size":0,"etag":"3emrccbr30","orphaned":false,"typeId":""}
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = [] # to store all the answers
        temp = []
        self.recursive(s , 0,ans,temp)
        return ans
    def recursive(self ,s,  index , ans  ,temp):
        # base case
        if index ==len(s):
            ans.append(temp[:])
            return
        
        for i in range(index, len(s)):
            if self.palindrome(s,index,i):
                temp.append(s[index : i+1])
                self.recursive(s,i+1,ans,temp)
                temp.pop()
    def palindrome(self,s,start,end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start+=1
            end-=1
        return True