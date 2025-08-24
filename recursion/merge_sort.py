file:///c%3A/Users/ASUS/Desktop/coding_python/merge_sort.py {"mtime":1755583438716,"ctime":1755583438716,"size":0,"etag":"3emcja2pl0","orphaned":false,"typeId":""}
class solution:
    def mergesort(self, nums , low ,high):
        # base case
        if low >=high :
            return
        mid = (low + high) //2 # index should be int

        self.mergesort(nums, low ,mid) # left half
        self.mergesort(nums, mid+1 , high) # right half
        self.merge(nums, low, mid ,high) # merge two sorted parts
    def merge(self, nums, low, mid ,high ):
        temp = []
        left = low
        right = mid +1 
        while ( left<=mid and right <=high ):

            if nums[left] <= nums[right]:
                # add left element
                temp.append(nums[left])
                left+=1
            else:
                # add right element
                temp.append(nums[right])
                right+=1
        # add remaing elements to list
        while (left <=mid):
            temp.append(nums[left])
            left+=1
        while (right <=high):
            temp.append(nums[right])
            right+=1
        for i in range(len(temp)):
            nums[low + i] = temp[i]
        