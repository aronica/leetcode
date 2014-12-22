#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'fafu'
from Meta import TreeNode
from Meta import ListNode
class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        def __calc__(head,n):
            if head is None:
                return None
            if head.next is None:
                return TreeNode(head.val)
            if head.next.next is None:
                t1 = TreeNode(head.val)
                t2 = TreeNode(head.next.val)
                t1.right = t2
                return t1
            if head.next.next.next is None:
                t1 = TreeNode(head.val)
                t2 = TreeNode(head.next.val)
                t3 = TreeNode(head.next.next.val)
                t2.right = t3
                t2.left = t1
                return t2

        fast = head.next.next.next
        slow = head.next
        nums = 4
        while fast is not None:
            if fast.next is not None:
                fast = fast.next.next
                slow = slow.next
                if fast is not None:
                    nums += 2
                else:
                    nums += 1
        return __calc__(head,nums)




        