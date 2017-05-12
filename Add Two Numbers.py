__author__ = 'fafu'
from Meta import ListNode


class Solution:
    def addTwoNumbers(self, l1, l2):
        def __help__(value, node):
            node.val = value % 10
            newnode = ListNode(value / 10)
            node.next = newnode
            return node, newnode

        if l1 is None:
            return l2
        if l2 is None:
            return l1
        node, pre = ListNode(0), None
        head = node
        while l1 is not None and l2 is not None:
            value = l1.val + l2.val + node.val
            pre, node = __help__(value, node)
            l1 = l1.next
            l2 = l2.next
        still = l1 is None and l2 or l1
        while still is not None:
            value = still.val + node.val
            pre, node = __help__(value, node)
            still = still.next
        if node.val == 0:
            pre.next = None
        return head
