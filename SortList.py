__author__ = 'fafu'
class Solution:
    def sortList(self, head):
        assert head is not None
        if head.next is None:
            return head
        if head.next.next is None:
            next = head.next
            if head.val>next.val:
                head.next = None
                next.next = head
                return next
            return head

        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        head2 = slow.next
        slow.next = None

        subhead1 = self.sortList(head)
        subhead2 = self.sortList(head2)
        return self.merge(subhead1,subhead2)

    def merge(self, first,second):
        if first is None:
            return second
        if second is None:
            return first
        node1 = first
        node2 = second
        oldnode1 = first
        oldnode2 = second
        head = None
        if node1.val<=node2.val:
            head = node1
        else:
            head = node2

        while node1 is not None and node2 is not None:
            while node1 is not None and node2 is not None and node1.val<=node2.val:
                oldnode1 = node1
                node1 = node1.next
            if node2 is not None and oldnode1.val<=node2.val:
                oldnode1.next = node2
            elif node2 is None:
                break

            while node2 is not None and node1 is not None and node2.val<node1.val:
                oldnode2 = node2
                node2 = node2.next
            if node1 is not None and oldnode2.val<node1.val:
                oldnode2.next = node1
            elif node1 is None:
                break
        return head