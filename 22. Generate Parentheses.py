"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        last = set([])
        new = set([])
        for i in xrange(n):
            if len(last) == 0:
                last = ["()"]
                continue
            for e in last:
                new.add("()" + e)
                new.add(e + "()")
                new.add("(" + e + ")")
                val = 0
                start = 0
                for j in xrange(len(e)):
                    if e[j] == '(':
                        val += 1
                    else:
                        val -= 1
                    if val == 0:
                        new.add("(" + e[start:j+1] + ")" + e[j+1:])

            last = new
            new = set([])

        return list(last)


def printParenthesis(s, n):
    ret = s.generateParenthesis(n)
    for i in ret:
        print(i + ",")
    print("Done " + str(n) + "=============")


if __name__ == "__main__":
    s = Solution()
    # printParenthesis(s, 1)
    # printParenthesis(s, 2)
    # printParenthesis(s, 3)
    printParenthesis(s, 4)
    # a = ["((())())","(())()()","(()(()))","((()))()","()(()())","((()()))","()(())()","(()()())","()()()()","()()(())","(()())()","()((()))","(((())))"]
    # b = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
    # for i in b:
    #     if i not in a:
    #         print i

"""
["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
"""
