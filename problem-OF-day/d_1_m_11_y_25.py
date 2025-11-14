from typing import List,Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # easy question
        # diy

        # assuming all elemnts arranged in the range 
        left  = None
        temp = head
        i = 0
        n = len(nums)
        while temp != None and (0<=i < n):
            # go through  ll
            if nums[i] == temp.val:
                if left is not None:
                    # meaning some non head node
                    left.next = temp.next
                    temp.next = None
                    temp = left.next # moved here
                elif left is None:
                    # meaning head node
                    left = temp
                    temp = temp.next # moved
                    left.next = None
                    left = None # make our left none again
                    # assign our ned head
                    head = temp
            else:
                # movement 
                left = temp
                temp = temp.next
                i += 1
        return head
            


            



