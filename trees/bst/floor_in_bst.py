
class Solution:
    def floorCeilOfBST(self, root, key):
        floor = -1
        while root:
            if root.val == key:
                floor = root.val
                return floor
            if root.val<key:
                floor = root.val
                root = root.right # to make it big
            else:
                root = root.left # to make it small