__author__ = 'fafu'
class Solution:
    #Bottom Binary Tree Level Order Traverse
    def levelOrderBottom(self, root):
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [[root.val]]
        node = root
        result = []
        nextlevel = [node]
        while len(nextlevel) > 0:
            level = nextlevel
            nextlevel = []
            for i in level:
                if i.left is not None:
                    nextlevel.append(i.left)
                if i.right is not None:
                    nextlevel.append(i.right)
            result.append([x.val for x in level])
        result.reverse()
        return result
