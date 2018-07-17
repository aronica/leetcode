"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs is None or len(strs) == 0:
            return [[]]
        sorted_dic = dict()

        for i in strs:
            key = str.join("", sorted(i))
            if key in sorted_dic:
                sorted_dic[key].append(i)
            else:
                sorted_dic[key] = [i]
        ret = []
        for _,v in sorted_dic.items():
            ret.append(v)
        return ret

if __name__ == "__main__":
    s = Solution()
    print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])






