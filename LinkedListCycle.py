__author__ = 'fafu'
class Solution:
    #Linked List Cycle
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
        fast = head.next.next
        slow = head.next
        while True:
            if fast is None or fast.next is None or fast.next.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
