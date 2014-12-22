__author__ = 'fafu'
class Solution:
    #swap pair
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        if head.next.next is None:
            next = head.next
            head.next = None
            next.next = head
            return next

        node = head.next
        pre = head
        newhead = node
        fast = node
        while node is not None:
            if fast is not None and fast.next is not None and fast.next.next is not None:
                fast = fast.next.next
            elif fast is not None and fast.next is not None:
                fast = fast.next
            else:
                fast = None
            pre.next = fast

            newnode = None
            if node.next is not None and node.next.next is not None:
                newnode = node.next.next
            oldpre = pre
            pre = node.next
            node.next = oldpre
            node = newnode
        return newhead
