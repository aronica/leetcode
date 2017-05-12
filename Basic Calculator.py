__author__ = 'fafu'
class Solution(object):

    def calculate(self, s):
        """
        "(1+(4+5+2)-3)+(6+8)" = 23
        :type s: str
        :rtype: int
        """
        stack = []
        current = 0
        oper = ['(',')']
        for i in s:
            if i=="(":
                stack.append(current)






