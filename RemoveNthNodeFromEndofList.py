__author__ = 'fafu'
class Solution:
    #Remove Nth Node From End of List
    def removeNthFromEnd(self, head, n):
        if head is None or n is None:
            return head
        node = head
        tail = node
        pre = head
        for i in range(n):
            if node is not None:
                pre = node
                node = node.next
            elif i == n-1:
                head = head.next
                return head
            else:
                return head

        if node is None and i == n-1:
            head = head.next
            return head

        while node.next is not None:
            node = node.next
            tail = tail.next

        if tail is not None and tail.next is not None:
            tail.next = tail.next.next
        elif tail is not None and tail.next is None:
            tail.next = None
        return head
