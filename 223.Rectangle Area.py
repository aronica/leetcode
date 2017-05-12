__author__ = 'fafu'
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        total = (C-A)*(D-B)+(G-E)*(H-F)
        if E>=C or G<=A or F>=D or H<=B:
            return total
        bl_x = max(A,E)
        bl_y = max(B,F)
        tr_x = min(C,G)
        tr_y = min(D,H)
        return total - abs((tr_x-bl_x)*(tr_y-bl_y))
