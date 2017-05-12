# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return
        pre = None
        node = head
        while node is not None:
            if node.val == val:
                if pre is None:
                    head = node.next
                    node = head
                else:
                    pre.next = node.next
                    node = node.next
            else:
                pre = node
                node = node.next
        return head



def printlistnode(listnode):
    strs = ""
    while listnode is not None:
        strs += str(listnode.val)+"-->"
        listnode = listnode.next
    print strs[0:len(strs)-3]

if __name__=="__main__":
    s = Solution()
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(6)
    l4 = ListNode(3)
    l5 = ListNode(4)
    l6 = ListNode(5)
    l7 = ListNode(6)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6
    l6.next = l7

    printlistnode(s.removeElements(l1,6))



