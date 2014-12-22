__author__ = 'fafu'
from Meta import TreeNode
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        node = head
        while node.next is not None and node.val == node.next.val:
            node = node.next
        if node.next is None:
            return None
        if node != head:
            return self.deleteDuplicates(node.next)
        else:
            head.next = self.deleteDuplicates(node.next)
            return head



