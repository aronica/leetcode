__author__ = 'fafu'
from Meta import ListNode
class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        m ,n = 1,1
        node = headA.next
        while node is not None:
            m += 1
            node = node.next
        node = headB.next
        while node is not None:
            n += 1
            node = node.next
        node1 = headA
        if m!=n:
            if m<n:
                node1 = headA
                node = headB
            elif m>n:
                node = headA
                node1 = headB
            i = 0
            while i<abs(m-n):
                node = node.next
                i+=1
        else:
            node1 = headA
            node = headB
        while node is not None and node1 is not None and node != node1:
            node = node.next
            node1 = node1.next
        if node is None or node1 is None:
            return None
        return node


