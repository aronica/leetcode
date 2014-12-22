__author__ = 'fafu'
class Solution:


    #Add Two Numbers
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        node = ListNode(0)
        head = node
        pre = None
        while l1 is not None and l2 is not None:
            value = l1.val + l2.val + node.val
            if value<10:
                node.val = value
                newnode = ListNode(0)
                node.next = newnode
                pre = node
                node = newnode
            else:
                node.val = value - 10
                newnode = ListNode(1)
                node.next = newnode
                pre = node
                node = newnode
            l1 = l1.next
            l2 = l2.next

        still = l1 is None and l2 or l1
        while still is not None:
            value = still.val + node.val
            if value<10:
                node.val = value
                newnode = ListNode(0)
                node.next = newnode
                pre = node
                node = newnode
            else:
                node.val = value - 10
                newnode = ListNode(1)
                node.next = newnode
                pre = node
                node = newnode
            still = still.next
        if node.val==0:
            pre.next = None
        return head
