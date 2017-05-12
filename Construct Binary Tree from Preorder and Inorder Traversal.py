__author__ = 'fafu'
from Meta import TreeNode
class Solution:
    #construct binary tree with preorder sequence and inorder sequence
    def buildTree(self, preorder, inorder):
        if preorder is None or inorder is None or len(preorder)==0:
            return None
        if len(preorder)!=len(inorder):
            return None
        if len(preorder)==1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        root_index_in_inorder = 0
        for i in xrange(len(inorder)):
            if inorder[i] == preorder[0]:
                root_index_in_inorder = i
                break
        if root_index_in_inorder == 0:
            root.right = self.buildTree(preorder[1:],inorder[1:])
        elif root_index_in_inorder == len(inorder)-1:
            root.left = self.buildTree(preorder[1:],inorder[0:root_index_in_inorder])
        else:
            root.left = self.buildTree(preorder[1:root_index_in_inorder+1],inorder[0:root_index_in_inorder])
            root.right = self.buildTree(preorder[root_index_in_inorder+1:],inorder[root_index_in_inorder+1:])
        return root

    #construct binary tree with preorder sequence and inorder sequence :TLE
    def buildTree2(self, inorder, postorder):
        if postorder is None or inorder is None or len(postorder)==0:
            return None
        root = TreeNode(postorder[-1])
        root_index_in_inorder = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[0:root_index_in_inorder],postorder[0:root_index_in_inorder])
        root.right = self.buildTree(inorder[root_index_in_inorder+1:],postorder[root_index_in_inorder:-1])
        return root
