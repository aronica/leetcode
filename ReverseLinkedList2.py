__author__ = 'fafu'
from Meta import ListNode
from Meta import print_linkedlist
class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        i = 1
        node = head
        pre = head
        while i<m:
            pre = node
            node = node.next
            i +=1
        #m ==1
        if node == head:
            next = node.next
            while i<n and next is not None:
                nnext = next.next
                next.next = node
                node = next
                next = nnext
                i += 1
            head.next = next
            head = node
        else:
            tmphead = node
            next = node.next
            while i<n and next is not None:
                nnext = next.next
                next.next = node
                node = next
                next = nnext
                i += 1
            pre.next = node
            #if next is not None:
            pre.next = node
            tmphead.next = next
        return head
if __name__=="__main__":
    s = Solution()
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l1.next = l2
    l2.next = l3
    l3.next = l4

    print_linkedlist(s.reverseBetween(l1,1,2))





