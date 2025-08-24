def permutation(n,k):
    fact = 1
    num = []
    ans=""
    for  i in  range(1,n):
        fact = fact*i
        num.append(i)
    num.append(n)
    k = k - 1
    while(True):
        ans = ans + str(num[k//fact])
        num.pop(k//fact) # use pop when removing by index and remove when removing by value
        if len(num) == 0:
            break
        k = k% fact
        fact = fact//len(num)
    return ans

print(permutation(4,17))