# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        def __binarysearch__(li,start,end,target):
            low,high = start,end
            while low<=high:
                mid = low + ((high-low)>>1)
                if li[mid].val == target.val:
                    return mid
                elif li[mid].val<target.val:
                    low = mid + 1
                else:
                    high = mid - 1
            if li[start].val>target.val:
                return -1
            if li[end].val<target.val:
                return -2
            return low

        if head is None or head.next is None:
            return head
        li = [head]
        node = head.next
        while node is not None:
            idx = __binarysearch__(li,0,len(li)-1,node)
            if idx == -1:
                li.insert(0,node)
                node = node.next
            elif idx == -2:
                li.append(node)
                node = node.next
            else:
                li.insert(idx,node)
                node = node.next
        head = li[0]
        node = head
        for i in xrange(1,len(li)):
            node.next = li[i]
            node = li[i]
        li[-1].next = None
        return head