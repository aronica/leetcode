__author__ = 'fafu'
class Solution:
    def reverseKGroup(self, head, k):
        if head is None or k is None:
            return None
        if head.next is None:
            return head
        if k==0 or k==1:
            return head

        fast = head
        node = head
        i = 1

        sectionhead = head
        pre = head
        node = head.next
        next = node.next
        fast = head

        while i<2*k and fast is not None:
            fast = fast.next
            i += 1
        if i<=k:
            return head

        j = 1
        sectionhead = pre
        last = False
        round = 0
        newhead = head
        while j<=k and node is not None:
            if j== 1 and fast is not None:
                pre.next = fast
            elif j == 1 and fast is None:
                sectionhead = pre
                last = True
            if j==k-1 and last:
                sectionhead.next = next
            if j == k and last:
                break
            else:
                node.next = pre

            pre = node
            node = next
            if next is not None:
                next = next.next
            else:
                next = None
            if fast is not None:
                fast = fast.next
            if j == k-1:
                if round == 0:
                    newhead = pre
                round += 1
            j += 1
            if j == k+1:
                j = 1
        return newhead
