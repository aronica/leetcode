__author__ = 'fafu'
"""
Given an array of integers, find out whether there are two distinct indices i and j in the array such that
the difference between nums[i] and nums[j]
is at most t and the difference between i and j is at most k.
"""

class TreeNode(object):
    def __init__(self,value,index):
        self.value = value
        self.index = list([index])
        self.left = None
        self.right = None

    def add_index(self,new_index):
        self.index.append(new_index)

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, value,index):
        if self.root is None:
            self.root = TreeNode(value,index)
        else:
            node = self.root
            parent = None
            direction = None
            while node is not None:
                if node.value == value:
                    node.add_index(index)
                    return
                elif node.value > value:
                    parent = node
                    direction = "left"
                    node = node.left
                else:
                    parent = node
                    direction = "right"
                    node = node.right
            node = TreeNode(value,index)
            if direction == "left":
                parent.left = node
            else:
                parent.right = node

def mid_traverse(root,result):
    if root is None:
        return
    mid_traverse(root.left,result)
    for i in root.index:
        result.append((root.value,i))
    mid_traverse(root.right,result)





class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if len(nums) is None or len(nums) == 0:
            return False
        if len(nums) < 2:
            return False

        tree = BinarySearchTree()
        for i in xrange(len(nums)):
            tree.add(nums[i], i)
        result = list()
        mid_traverse(tree.get_root(),result)
        i ,j = 0, 1
        if len(result)<2:
            return 0<=t

        while i < len(result)-1:
            if (abs(result[j][1] - result[i][1]) <= k and abs(result[j][0] - result[i][0]) <= t) or (abs(result[i][1] - result[j][1]) <= k and abs(result[i][0] - result[j][0]) <= t):
                return True
            if result[j][0] - result[i][0] > t or j == len(result)-1:
                i += 1
                j = i+1
            else:
                j += 1
        return False



if __name__=="__main__":
    s = Solution()
    print s.containsNearbyAlmostDuplicate([0],0,0)



