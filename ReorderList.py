__author__ = 'fafu'
class Solution:
    #reorder list
    def reorderList(self, head):
        if head is None or head.next is None or head.next.next is None:
            return head
        tail = head
        num = 1
        while tail.next is not None:
            tail = tail.next
            num += 1
        half = (num + 1)/2

        index = 1
        tail = head
        while index < half:
            index += 1
            tail = tail.next

        tail = tail.next
        pre = None
        tailnext = None
        end = tail
        #reverse the second half nodes
        while tail is not None:
            tailnext = tail.next
            tail.next = pre
            pre = tail
            if tailnext is not None:
                tail = tailnext
            else:
                break

        node = head
        #merge to linkedlists
        index = 1
        while tail is not None:
            if index%2 == 1:
                nodenext = node.next
                node.next = tail
                node = nodenext
            else:
                nodenext = tail.next
                tail.next = node
                tail = nodenext
                if tail is None:
                    if node.next is not None:
                        node.next = None
            index += 1
        return head
