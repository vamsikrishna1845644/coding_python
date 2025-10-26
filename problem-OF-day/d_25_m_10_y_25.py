class Solution:
    def totalMoney(self, n: int) -> int:
        # mul*28 + (mul-1)*7 -> eq1
        # mul*rem + (rem*(rem+1))//2 -> eq2
        # total  = eq1 + eq2
        if n < 7:
            total =  (n*(n+1))//2
        elif n >= 7:
            mul = n//7
            rem = n%7
            eq1 = mul*28 + ((mul-1)*(mul)*7)//2
            eq2 = mul*rem + (rem*(rem+1))//2
            total = eq1+eq2
        return total
    
sol = Solution()
print(sol.totalMoney(10))
