class solution:
    def mergesort(self, nums , low ,high):
        count = 0
        # base case
        if low >=high :
            return
        mid = (low + high) //2 # index should be int

        count += self.mergesort(nums, low ,mid) # left half
        count += self.mergesort(nums, mid+1 , high) # right half
        count += self.merge(nums, low, mid ,high) # merge two sorted parts
        return count
    def merge(self, nums, low, mid ,high ):
        count = 0
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
                count+= mid-low + 1
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
        return count
        
