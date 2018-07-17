"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s is None or len(s) <= numRows or numRows < 2:
            return s

        result = ""
        cycle = 2 * numRows - 2;
        for i in xrange(numRows):
            j = i
            while j < len(s):
                result = result + s[j]
                secondJ = (j - i) + cycle - i
                if i != 0 and i != numRows - 1 and secondJ < s.length():
                    result = result + s[secondJ]
                j = j + cycle
        return result
