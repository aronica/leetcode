__author__ = 'fafu'
class Solution:

    #linked list cycle II ,first found the node which we found while we looking for if it has a cycle,
    #if found, then the linkedlist starts from head and the linkedlist starts from the founded node will meet
    #at the node where the cycle begins and the lengths until this node of two linkedlist must be equal.
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None
        if head.next == head:
            return head
        slow = head
        fast = head
        hasCycle = False
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                hasCycle = True
                break
        if hasCycle:
            slow = head
            while slow != fast:
                fast = fast.next
                slow = slow.next
            return fast
        return None