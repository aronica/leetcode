__author__ = 'fafu'
class Solution:

    #merge k sorted linked list
    def mergeKLists(self, lists):
        if lists is None:
            return None
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return self.merge(lists[0],lists[1])
        l1 = self.mergeKLists(lists[0:len(lists)/2+1])
        l2 = self.mergeKLists(lists[len(lists)/2+1:])
        self.merge(l1,l2)
