__author__ = 'fafu'
import math
from datetime import datetime
import time


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        if a is None or len(a) == 0:
            return b
        if b is None or len(b) == 0:
            return a
        big = len(a)>len(b) and a or b
        small = len(a)>len(b) and b or a
        longs = len(big)
        short = len(small)
        result = ["0" for i in xrange(0,longs+1)]
        i = 0
        resultlength = longs + 1
        target = small
        while i<longs:
            if i == short:
                target = result
                short = resultlength
            if big[longs-i-1]>'9' or big[longs-i-1]<'0':
                return None
            if target==small and target[short-i-1]>'9' or target[short-i-1]<'0':
                return None
            if big[longs-i-1] == "0" and target[short - i -1] == "1" \
                or (big[longs-i-1] == "1" and target[short - i -1] == "0"):
                if target == result or result[resultlength-i-1]=="0":
                    result[resultlength-i-1] = "1"
                else:
                    result[resultlength-i-1] = "0"
                    result[resultlength-i-2] = "1"
            elif big[longs-i-1] == "1" and target[short - i -1] == "1":
                if target != result:
                    result[resultlength-i-2] = "1"
                else:
                    result[resultlength-i-2] = "1"
                    result[resultlength-i-1] = "0"
            i += 1
        if result[0] == "0":
            return "".join(result[1:])
        return "".join(result)

    #Longest Common Prefix
    def longestCommonPrefix(self, strs):
        if strs is None or len(strs)==0:
            return None
        if len(strs)==1:
            return strs[0]
        maxs =  min(len(i) for i in strs)
        prefix = ""
        length = len(strs)
        i = 1
        while i<length:
            a = strs[i]
            b = strs[i - 1]
            while a[0:maxs] != b[0:maxs]:
                maxs -= 1
            if maxs == 0:
                break
            i += 1
        if maxs == 0:
            return ""
        return strs[0][0:maxs]

    def sqrt(self, x):
        if x is None:
            return None
        if x <0:
            return None
        if x==0:
            return 0
        if x==1:
            return 1
        small = 1
        big = x
        while big-small>1:
            mid = (small+big)/2
            val = mid*mid
            if val<x:
                small = mid
            elif val>x:
                big = mid
            else:
                return mid
        if big == small:
            return small
        smalls = small*small
        bigs = big*big
        return float(x-smalls)/x < float(bigs-x)/x and small or big


    def isSymmetric(self, root):
        if root is None:
            return False
        #return self.__isSymmetric(root.left,root.right)
        return self.__isSymmetricNoneRecursively(root)


    def __isSymmetric(self,first,second):
        if first is None and second is None:
            return True
        result = first is not None and second is not None
        if not result:
            return False
        if first.val != second.val:
            return False
        rel1 = self.__isSymmetric(first.left,second.right)
        rel2 = self.__isSymmetric(first.right,second.left)
        return rel1 and rel2

    def __isSymmetricNoneRecursively(self,root):
        first = root.left
        second = root.right
        stack = list()
        stack.append((first,second))
        while len(stack)>0:
            first,second = stack.pop()
            if first is None and second is None:
                continue
            result = first is not None and second is not None
            if not result:
                return False
            if first.val != second.val:
                return False
            stack.append((first.left,second.right))
            stack.append((first.right,second.left))
        return True
    #longest consecutive sequence
    def longestConsecutive(self, num):
        if num is None:
            return 0
        if len(num) == 1:
            return 1
        dic = {i:False for i in num}
        maxnum = 1
        for i in num:
            if dic[i]:
                continue
            less = i-1
            count = 1
            while less in dic:
                dic[less] = True
                less -= 1
                count += 1
            less = i+1
            while less in dic:
                dic[less] = True
                less += 1
                count += 1
            if count>maxnum:
                maxnum = count
        return maxnum
    #Populating Next Right Pointers in Each Node
    def connect(self, root):
        if root is None:
            return None
        if root.left is None:
            return root
        node = root.left
        node.next = root.right
        parent = root
        stack = list()
        stack.append((root.right,root))
        while len(stack)>0:
            if node is None:
                node,parent = stack.pop()
            if parent.next is not None:
                node.next = parent.next.left
            while node.left is not None:
                node.left.next = node.right
                stack.append((node.right,node))
                parent = node
                node = node.left
            if node == parent.right and parent.next is not None:
                node.next = parent.next.left
            node = None
        return root

    def lengthOfLongestSubstring(self, s):
        if s is None:
            return 0
        if len(s)==1:
            return 1
        dic = {}
        maxcount = 1
        count = 0
        startindex = 0
        for index,i in enumerate(s):
            if i not in dic:
                count += 1
                dic[i] = index
            else:
                idx = dic[i]
                oldstartindex = startindex
                while startindex<idx:
                    del dic[s[startindex]]
                    startindex += 1
                dic[i] = index
                startindex = idx+1
                count -= startindex - oldstartindex - 1
            if count>maxcount:
                maxcount = count
        return maxcount

    #Add Two Numbers
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        node = ListNode(0)
        head = node
        pre = None
        while l1 is not None and l2 is not None:
            value = l1.val + l2.val + node.val
            if value<10:
                node.val = value
                newnode = ListNode(0)
                node.next = newnode
                pre = node
                node = newnode
            else:
                node.val = value - 10
                newnode = ListNode(1)
                node.next = newnode
                pre = node
                node = newnode
            l1 = l1.next
            l2 = l2.next

        still = l1 is None and l2 or l1
        while still is not None:
            value = still.val + node.val
            if value<10:
                node.val = value
                newnode = ListNode(0)
                node.next = newnode
                pre = node
                node = newnode
            else:
                node.val = value - 10
                newnode = ListNode(1)
                node.next = newnode
                pre = node
                node = newnode
            still = still.next
        if node.val==0:
            pre.next = None
        return head

    #Longest Palindromic Substring
    def longestPalindrome(self, s):
        if s is None or len(s) == 0 or len(s) ==1 :
            return s
        if len(s) == 2:
            return s[0] == s[1] and s or s[0]
        maxlen = 1
        length = len(s)
        i = 1
        dp =  [[False for x in xrange(length)] for x in xrange(length)]
        if s[0] == s[1]:
            maxlen = 2
            dp[0][1] = True
        dp[0][0] = True
        dp[1][1] = True

        for i in xrange(2,len(s)):
            dp[i][i] = True
            if maxlen == 1:
                if s[i-1] == s[i]:
                    dp[i-1][i] = True
                    if maxlen<2:
                        maxlen = 2
            index = (i - maxlen/2) == i and i-1 or i-maxlen/2
            for j in xrange(index,0,-1):

                if dp[j][i-1] and s[j-1]==s[i]:
                    dp[j-1][i] = True
                    if i+1-j+1>maxlen:
                        maxlen = i-j+2
        return maxlen


    def ladderLength(self, start, end, dict):
        if start == end:
            return 1

        all_chars = map(chr, xrange(ord('a'), ord('z') + 1))
        visited = set()
        bfs = [start, None]

        # at which distance the following to-be-processed nodes are
        distance = 2

        while len(bfs) > 1:
            word = bfs.pop(0)
            if word is None:
                distance += 1
                bfs.append(None)
                continue

            for i in xrange(len(word)):
                for char in all_chars:
                    new_word = word[:i] + char + word[i + 1:]
                    if new_word == end:
                        return distance
                    if new_word in dict and new_word not in visited:
                        bfs.append(new_word)
                        visited.add(new_word)

        return 0

    #word ladder2
    def ladderLength2(self, start, end, dict):
        if start == end:
            return [[start]]
        if dict is None:
            return []

        all_chars = map(chr, xrange(ord('a'), ord('z') + 1))
        visited = {}
        dis = {start:1}
        bfs = [ListNode(start), None]
        distance = 2
        # at which distance the following to-be-processed nodes are
        result = []
        found = False
        while len(bfs) > 1:
            node = bfs.pop(0)

            if node is None:
                distance  += 1
                if not found:
                    bfs.append(None)
                    continue
                else:
                    break
            word = node.val

            for i in xrange(len(word)):
                for char in all_chars:
                    new_word = word[:i] + char + word[i + 1:]
                    if new_word == end:
                        result.append(node)
                        if not found:
                            found = True
                        break
                    elif new_word == word:
                        Found = True
                        continue
                    elif new_word in dict and new_word not in visited:
                        newnode = ListNode(new_word)
                        newnode.next = [node]
                        bfs.append(newnode)
                        visited[new_word] = (newnode,distance)
                        if new_word in dis and dis[new_word]<distance-1:
                            continue
                        else:
                            dis[new_word] = distance-1
                    elif new_word in dict and new_word in visited and new_word in dis:
                        if dis[new_word]<distance-1:
                            continue
                        newnode = visited[new_word]
                        if newnode[1] < distance:
                            newnode[0].next.append(node)

        newresult = []

        for i in result:
            self.dfs_wordladder(i,[end],newresult)
        return newresult

    def isMatch(self, s, p):
        if s is None or p is None:
            return False
        if s == p:
            return True
        if p==".*":
            return True
        if len(s)==1 and p==".":
            return True
        if p[0] == "*":
            return False
        if p.find("**")>-1:
            return False
        i = 0
        j = 0
        dp = [None for i in len(p)]

        while j<len(p) and i<len(s):
            if p[j] not in "*.":
                if p[j] == s[i]:
                    if j == 0:
                        dp[j] = p[j]
                        i += 1
                        j += 1
                else:
                    if j == len(p)-1:
                        return False
                    else:
                        if p[j+1]!="*":
                            return False
                        dp[j] = p[j]
                        dp[j+1] = "*"
                    i += 1
                    j += 1
            elif p[j] == ".":
                if dp[j] == "*":
                    return False
                dp[j] = "."
                i += 1
                j += 1
            else:  # *
                dp[j] = "*"
                if p[j-1] == ".":  #backtracing
                    i += 1
                    j += 1
                else:
                    if p[j-1] != s[i]:
                        if j == len(p) -1:
                            return False
                        dp[j] = s[i]
                        j += 1
                    else:
                        dp[j] = s[i]
                        i +=  1
                        j += 1



    def findLadders(self, start, end, words):
        pathes=[];
        graphNodes={};
        queue=[(start,0,[])];
        minPath=0;
        nodeShortPathCache={};

        while(len(queue)>0):
            node,dis,path=queue.pop(0);

            if(node not in graphNodes):
                graphNodes[node]=[];
                for i in range(len(node)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if(j==node[i]):
                            continue;
                        newNode = node[0:i] + j + node[i + 1:]
                        if(newNode in words):
                            graphNodes[node].append(newNode)

            if(node in nodeShortPathCache):
                if(dis>nodeShortPathCache[node]):
                    continue;
            else:
                nodeShortPathCache[node]=dis;
            if(node==end):
                newpath=list(path);
                newpath.append(node);
                if(minPath==0):
                    minPath=dis;
                if(dis==minPath):
                    pathes.append(newpath);
            else:
                newpath=list(path);
                newpath.append(node);
                for childNode in graphNodes[node]:
                    if(childNode in nodeShortPathCache):
                        if(dis+1>nodeShortPathCache[childNode]):
                            continue;
                    queue.append((childNode,dis+1,newpath));
        return pathes;

    def dfs_wordladder(self,node,result,newresult):
        result.append(node.val)
        leng = len(result)
        if node.next is not None:
            for i in node.next:
                self.dfs_wordladder(i,result,newresult)
                del result[leng:]
        else:
            tmp = [i for i in result]
            tmp.reverse()
            newresult.append(tmp)

    #subset 2
    def subsetsWithDup(self, S):
        if S is None:
            return []
        if len(S)==0:
            return [S,[]]
        S.sort()
        result = [S]
        for i in xrange(1,len(S)):pass

    def combine(self, n, k):
        return self.__combine__(1,n,k)

    def __combine__(self,start,end,k):
        if end-start+1 is None or k is None:
            return []
        if k == 1:
            return [[i] for i in xrange(start,end+1)]
        if end-start+1<k:
            return []
        if end-start+1 == k:
            return [[i for i in xrange(start,end+1)]]
        result = []
        res1 = self.__combine__(start+1,end,k-1)
        for i in res1:
            i.insert(0,start)
        res2 = self.__combine__(start+1,end,k)
        res1.extend(res2)
        return res1
    #Fibonacci
    def climbStairs(self, n):
        if n is None or n==0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        f1 = 1;f2 = 2;f3 = None
        i = 3
        while i <= n:
            f3 = f1 + f2
            f1 = f2
            f2 = f3
            i += 1
        return f3

    #Container With Most Water
    def maxArea(self, height):
        if height is None or len(height) < 2:
            return 0
        max_water = 0
        dp = [[] for i in xrange(len(height))]

        dp[1] = 0

        for i in xrange(2,len(height)-1):
            maxval = 0
            dp[i] = 0
            for j in xrange(i):
                if height[i]>height[j] or (height[i]<height[j] and height[i]>height[dp[j]]):
                    val1 =  (i - dp[j]) * min(height[i],height[dp[j]])
                    val2 = (i-j)*min(height[i],height[j])
                    if val1>=val2 and val1>maxval:
                        dp[i] = dp[j]
                        max_water = max(val1,max_water)
                    else:
                        if val2>maxval:
                            dp[i] = j
                        max_water = max(val2,max_water)
                else:
                    val = (i - dp[j])*height[i]
                    if val>maxval:
                        dp[i] = dp[j]
                        max_water = max(val,max_water)
        return max_water
    #4 Sums
    def fourSum(self, num, target):
        num.sort()

    def reverseKGroup(self, head, k):
        if head is None or k is None:
            return None
        if head.next is None:
            return head
        if k==0 or k==1:
            return head

        fast = head
        node = head
        i = 1

        sectionhead = head
        pre = head
        node = head.next
        next = node.next
        fast = head

        while i<2*k and fast is not None:
            fast = fast.next
            i += 1
        if i<=k:
            return head

        j = 1
        sectionhead = pre
        last = False
        round = 0
        newhead = head
        while j<=k and node is not None:
            if j== 1 and fast is not None:
                pre.next = fast
            elif j == 1 and fast is None:
                sectionhead = pre
                last = True
            if j==k-1 and last:
                sectionhead.next = next
            if j == k and last:
                break
            else:
                node.next = pre

            pre = node
            node = next
            if next is not None:
                next = next.next
            else:
                next = None
            if fast is not None:
                fast = fast.next
            if j == k-1:
                if round == 0:
                    newhead = pre
                round += 1
            j += 1
            if j == k+1:
                j = 1
        return newhead

    #Interleaving String
    def isInterleave(self, s1, s2, s3):
        if s1 is None or s2 is None or s3 is None or len(s1)+len(s2)!=len(s3):
            return False
        m = 0;n=0;k = 0;nn = False
        dp = []
        while m<len(s1) and n<len(s2) and m+n < len(s3)-1:
            if s1[m] == s3[m+n] and s2[n] == s1[m]:
                m += 1
                dp.append((m,n))
            elif s1[m] == s3[m+n]:
                m += 1
            elif s2[n] == s3[m+n]:
                n += 1
            else:
                while len(dp)>0 and not dp[-1]:
                    n -= 1







    def sumNumbers(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val
        stack = list()
        node = root
        value = 0
        total = 0
        while len(stack)>0 or node is not None:
            if node is not None:
                if node.left is None and node.right is None:
                    total += value*10 + node.val
                    node = None
                else:
                    value = value*10 + node.val
                    stack.append((node,value))
                    node = node.left
            else:
                node,value = stack.pop()
                node = node.right
        return total
    #swap pair
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        if head.next.next is None:
            next = head.next
            head.next = None
            next.next = head
            return next

        node = head.next
        pre = head
        newhead = node
        fast = node
        while node is not None:
            if fast is not None and fast.next is not None and fast.next.next is not None:
                fast = fast.next.next
            elif fast is not None and fast.next is not None:
                fast = fast.next
            else:
                fast = None
            pre.next = fast

            newnode = None
            if node.next is not None and node.next.next is not None:
                newnode = node.next.next
            oldpre = pre
            pre = node.next
            node.next = oldpre
            node = newnode
        return newhead
    #combination sum
    def combinationSum(self, candidates, target):
        def __combination__(candidates,target):
            result = []
            for i in xrange(len(candidates)-1,-1,-1):
                val = target/candidates[i]
                remainder = target%candidates[i]
                if remainder == 0:
                    result.append([candidates[i] for j in xrange(val)])

                for j in xrange(val,0,-1):
                    tmp = target - j*candidates[i]
                    if tmp == 0:
                        continue
                    elif tmp<candidates[0]:
                        continue
                    res = __combination__(candidates[0:i],tmp)
                    for m in res:
                        m.extend([candidates[i] for n in xrange(j)])
                    result.extend(res)
            return result



        while len(candidates)>0 and candidates[len(candidates)-1]>target:
            candidates.pop()
        candidates.sort()
        return __combination__(candidates,target)

    #combination sum2: each element in candidates may only be used once.
    def combinationSum2(self, candidates, target):
        def __combines__(candidates,dic,target):
            i = len(candidates)-1
            result = []
            while i>-1:
                if i != 0 and candidates[i] == candidates[i-1]:
                    i -= 1
                    continue
                if target<candidates[i]:
                    i -= 1
                    continue
                val = dic[candidates[i]]
                for j in xrange(val,0,-1):
                    tmp = target - j*candidates[i]
                    if tmp == 0:
                        result.append([candidates[i] for m in xrange(j)])
                        continue
                    elif tmp<candidates[0]:
                        continue
                    res = __combines__(candidates[0:i],dic,tmp)
                    for m in res:
                        m.extend([candidates[i] for n in xrange(j)])
                    result.extend(res)
                i -= 1
            return result

        candidates.sort()

        while len(candidates)>0 and candidates[len(candidates)-1]>target:
            candidates.pop()

        if len(candidates)==1:
            if candidates[0] == target:
                return [[target]]
            else:
                return []
        dic={}
        for i in candidates:
            if i in dic:
                dic[i] = dic[i]+1
            else:
                dic[i] = 1
        i = 0;j=len(candidates)-1
        result = []
        return __combines__(candidates,dic,target)
    #Binary Tree maximum path sum
    def maxPathSum(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val
        left = None
        right = None
        if root.left is not None:
            left = self.maxPathSum(root.left)
        if root.right is not None:
            right = self.maxPathSum(root.right)
        if left is None and right is not None:
            return max(root.val,root.val+right,right)
        elif left is not None and right is None:
            return max(root.val,root.val+left,left)
        return max(root.val,root.val+left,root.val+right,root.val+left+right,left,right)
        # stack = list()
        # node = root
        # val = 0
        # sum = 0
        # maximum = root.val
        # while node is not None or len(stack)>0:
        #     if node is not None:
        #         if maximum<sum:
        #             maximum = sum+node.val
        #         stack.append((node,sum,"1"))
        #         sum += node.val
        #         node = node.left
        #     else:
        #         node,parentsum,dir = stack.pop()
        #         if dir=="1" and node.right is not None:
        #             stack.append((node,parentsum,"2"))
        #             node = node.right
        #         elif dir=="2" or node.right is None:
        #             if node.val>0:
        #                 if parentsum>sum:
        #                     sum = parentsum +node.val
        #             else:
        #                 if parentsum>sum:
        #                     sum = parentsum
        #             node = None
    #Maximum Depth of Binary Tree
    def maxDepth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        left = 0
        right = 0
        if root.left is not None:
            left = self.maxDepth(root.left)
        if root.right is not None:
            right = self.maxDepth(root.right)
        return max(left+1,right+1)

    #valid sudoku
    def isValidSudoku(self, board):
        for j in board:
            for i in xrange(len(board)):
                if j[i]==".":
                    continue
                else:
                    return
    #Minimum Window Substring
    def minWindow(self, S, T):
        if S is None or T is None or len(S)<len(T):
            return ""
        s_set = set(T)
        minlen = S
        tlen = len(T)

        t_count_set = dict()
        for i in xrange(len(T)):
            if T[i] in t_count_set:
                t_count_set[T[i]].append(i)
            else:
                t_count_set[T[i]] = [i]

        r_set = dict()
        queue = []
        found = False
        count = 0
        for i in xrange(len(S)):
            if S[i] in s_set:
                queue.append(i)
                if S[i] not in r_set:
                    r_set[S[i]] = [i]
                    count += 1
                else:
                    r_set[S[i]].append(i)
                    if len(r_set[S[i]])<=len(t_count_set[S[i]]):
                        count += 1
                while count == tlen:
                    found = True
                    if i-queue[0]+1<len(minlen):
                        minlen = S[queue[0]:i+1]
                    head = queue[0]
                    del queue[0]
                    del r_set[S[head]][0]
                    if len(r_set[S[head]])<len(t_count_set[S[head]]):
                        count -= 1
        if found:
            return minlen
        return ""

    #max profit of selling stocks
    def maxProfit(self, prices):
        if prices is None or len(prices)==0:
            return 0
        if len(prices) == 2:
            return max(0,prices[1]-prices[0])
        stack = [prices[len(prices)-1]]
        for i in xrange(len(prices)-2,0,-1):
            stack.append(max(prices[i],stack[len(stack)-1]))
        profit = 0
        for i in xrange(len(prices)-1):
            profit = max(profit,stack.pop()-prices[i])
        return profit
    #we can do the transaction multiple times
    def maxProfit2(self, prices):
        if prices is None or len(prices)==0:
            return 0
        if len(prices) == 2:
            return max(0,prices[1]-prices[0])
        dp = (0,-prices[0])   #resource 1,0
        for i in xrange(1,len(prices)):
            resource1 = max(dp[0],prices[i]+dp[1])#you
            resource0 = max(dp[1],dp[0]-prices[i])#meiyou
            dp = (resource1,resource0)
        return max(dp[0],dp[1])

    #we can only do the transaction at most twice.
    def maxProfit3(self, prices):
        def __max__(prices,stack,start,end):
            if end-start == 1:
                if prices[1]>prices[0]:
                    return prices[1]-prices[0],0,1
                return 0,None,None
            profit = 0
            head = None;tail=None
            for i in xrange(start,end-1,1):
                if stack[end-i-2][0] - prices[i]> profit:
                    profit = stack[end-i-2][0] - prices[i]
                    head = i;tail = stack[end-i-2][1]
            return profit,head,tail
        if prices is None or len(prices) < 2:
            return 0
        if len(prices) == 2:
            if prices[1]>prices[0]:
                return prices[1]-prices[0]
            return 0
        if len(prices) ==3:
            return max(0,max(prices[1:])-prices[0],prices[2]-min(prices[0:2]))

        stack = [(prices[len(prices)-1],len(prices)-1)]
        for i in xrange(len(prices)-2,0,-1):
            if prices[i]>=stack[len(stack)-1][0]:
                stack.append((prices[i],i))
            else:
                stack.append(stack[len(stack)-1])
        p1 = 0;h1 = None;t1 = None
        maxval = __max__(prices,stack,0,len(prices))[0]
        if prices[1]>prices[0]:
            p1 = prices[1] - prices[0]
            h1 = 0;t1 =1
        p2,h2,t2 = __max__(prices,stack,2,len(prices))
        maxval = max(p1 + p2 ,maxval)

        for i in xrange(2,len(prices)-2,1):
            if h1 is None:
                if prices[i]>prices[i-1]:
                    p1 = prices[i]-prices[i-1]
                    h1 = i-1
                    t1 = i
            else:
                if prices[i]>=prices[t1]:
                    t1 = i
                    p1 = prices[i] - prices[h1]
                elif prices[i]<prices[h1]:
                    h1 = i
                    p1 += prices[h1]-prices[i]
            if h2 is None:
                if maxval<p1:
                    maxval = p1
                continue
            else:
                if i == h2:
                    p2,h2,t2 = __max__(prices,stack,i+1,len(prices))
                if maxval < p1+p2:
                    maxval = p1+p2
        return maxval

    def firstMissingPositive(self, A):
        if A is None or len(A)==0 or len(A)==1 and A[0]==0:
            return 1
        if len(A)==1 and len(A)==1:
            return 2
        elif len(A)==1 and len(A)>1:
            return len(A)-1

        minval = None
        maxval = 0
        j = len(A)-1
        i = 0
        while i<=j:
            while A[j]<=0:
                j-= 1
            if A[i]<=0:
                tmp = A[j]
                A[j] = A[i]
                A[i] = tmp
                j -= 1
            else:
                if minval is None or minval>A[i]:
                    minval = A[i]
                if A[i]>maxval:
                    maxval = A[i]
                i += 1

        if maxval-minval == j:
            if minval == 1:
                return maxval+1
            return minval-1
        if maxval==minval:
            if minval == 1:
                return maxval+1
            return minval-1
        i = 0
        newj = j
        while i<=j:
            if A[i]-minval==i:
                i+= 1
            elif A[i]-minval>i:
                tmp = A[i]
                idx= A[i]-minval
                if A[idx]>0:
                    A[i] = A[idx]
                else:
                    A[i] = None
                    i+=1
                A[idx]= tmp
        i = 0
        while i<=j:
            if A[i]!=i+minval:
                return i+minval
            i+=1
    #construct binary tree with preorder sequence and inorder sequence
    def buildTree(self, preorder, inorder):
        if preorder is None or inorder is None or len(preorder)==0:
            return None
        if len(preorder)!=len(inorder):
            return None
        if len(preorder)==1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        root_index_in_inorder = 0
        for i in xrange(len(inorder)):
            if inorder[i] == preorder[0]:
                root_index_in_inorder = i
                break
        if root_index_in_inorder == 0:
            root.right = self.buildTree(preorder[1:],inorder[1:])
        elif root_index_in_inorder == len(inorder)-1:
            root.left = self.buildTree(preorder[1:],inorder[0:root_index_in_inorder])
        else:
            root.left = self.buildTree(preorder[1:root_index_in_inorder+1],inorder[0:root_index_in_inorder])
            root.right = self.buildTree(preorder[root_index_in_inorder+1:],inorder[root_index_in_inorder+1:])
        return root

    #construct binary tree with preorder sequence and inorder sequence :TLE
    def buildTree2(self, inorder, postorder):
        if postorder is None or inorder is None or len(postorder)==0:
            return None
        root = TreeNode(postorder[-1])
        root_index_in_inorder = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[0:root_index_in_inorder],postorder[0:root_index_in_inorder])
        root.right = self.buildTree(inorder[root_index_in_inorder+1:],postorder[root_index_in_inorder:-1])
        return root

    def buildTree4(self, inorder, postorder):
        if len(postorder) == 0 :
            return None
        else:
            node = TreeNode(postorder[-1])
            i = inorder.index(postorder[-1])
            node.left = self.buildTree(inorder[0:i],postorder[0:i])
            node.right = self.buildTree(inorder[i+1:],postorder[i:-1])
            return node

    def inorderTraversal(self, root):
        if root is None or len(root)==0:
            return []
        res = []
        stack = []
        node = root
        while node is not None or len(stack)>0:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res.append(node.val)
                if node.right is not None:
                    node = node.right
                else:
                    node = None
        return res




s = Solution()
print "111,11=",s.addBinary("101111","10")
l = ['abc','abcd','ab']
print "longestCommonPrefix(",l,")=",s.longestCommonPrefix(l)

n = 25
print "sqrt(",n,"):",s.sqrt(n)
n=24
print "sqrt(",n,"):",s.sqrt(n)
n=3
print "sqrt(",n,"):",math.sqrt(n),",",s.sqrt(n)
n=5
print "sqrt(",n,"):",math.sqrt(n),",",s.sqrt(n)
n=6
print "sqrt(",n,"):",math.sqrt(n),",",s.sqrt(n)
n=7
print "sqrt(",n,"):",math.sqrt(n),",",s.sqrt(n)
n=8
print "sqrt(",n,"):",math.sqrt(n),",",s.sqrt(n)
n=9
print "sqrt(",n,"):",math.sqrt(n),",",s.sqrt(n)
n=10
print "sqrt(",n,"):",math.sqrt(n),",",s.sqrt(n)
n=11
print "sqrt(",n,"):",math.sqrt(n),",",s.sqrt(n)
n=12
print "sqrt(",n,"):",math.sqrt(n),",",s.sqrt(n)
n=13
print "sqrt(",n,"):",math.sqrt(n),",",s.sqrt(n)
n=14
print "sqrt(",n,"):",math.sqrt(n),",",s.sqrt(n)

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t7 = TreeNode(7)
t8 = TreeNode(8)
t9 = TreeNode(9)
t10 = TreeNode(10)
t11 = TreeNode(11)
t12 = TreeNode(12)
t13 = TreeNode(13)
t14 = TreeNode(14)
t15 = TreeNode(15)
t1.left = t2
t1.right = t3
t2.left=t4
t2.right=t5
t3.left = t6
t3.right=t7
t4.left=t8
t4.right=t9
t5.left=t10
t5.right=t11
t6.left=t12
t6.right=t13
t7.left=t14
t7.right=t15
s.connect(t1)
ss = "abcabcab"
print "lengthOfLongestSubstring(",ss,")=",s.lengthOfLongestSubstring(ss)

ss = "abccbad"
print "lengthOfLongestSubstring(",ss,")=",s.lengthOfLongestSubstring(ss)

l1 = ListNode(1)
l2 = ListNode(1)
l3 = ListNode(1)

l4 = ListNode(9)
l5 = ListNode(9)
l6 = ListNode(9)
l7 = ListNode(9)

l1.next = l2
l2.next = l3

l4.next = l5
l5.next = l6

def printlistnode(listnode):
    strs = ""
    while listnode is not None:
        strs += str(listnode.val)+"-->"
        listnode = listnode.next
    print strs[0:len(strs)-3]
#print printlistnode(s.addTwoNumbers(l1,l4))
ss="vmqjjfnxtyciixhceqyvibhdmivndvxyzzamcrtpywczjmvlodtqbpjayfchpisbiycczpgjdzezzprfyfwiujqbcubohvvyakxfmsyqkysbigwcslofikvurcbjxrccasvyflhwkzlrqowyijfxacvirmyuhtobbpadxvngydlyzudvnyrgnipnpztdyqledweguchivlwfctafeavejkqyxvfqsigjwodxoqeabnhfhuwzgqarehgmhgisqetrhuszoklbywqrtauvsinumhnrmfkbxffkijrbeefjmipocoeddjuemvqqjpzktxecolwzgpdseshzztnvljbntrbkealeemgkapikyleontpwmoltfwfnrtnxcwmvshepsahffekaemmeklzrpmjxjpwqhihkgvnqhysptomfeqsikvnyhnujcgokfddwsqjmqgsqwsggwhxyinfspgukkfowoxaxosmmogxephzhhy"
ss2="abccbaabcdcbaa"
print time.clock()
#print "longestPalindrome(",ss,")=",s.longestPalindrome(ss)
print time.clock()

#print "wordLadder2()=",s.ladderLength2("red","tax",["ted","tex","red","tax","tad","den","rex","pee"])
print time.clock()
#print "wordLadder2()=",s.ladderLength2("nanny", "aloud", ["ricky","grind","cubic","panic","lover","farce","gofer","sales","flint","omens","lipid","briny","cloth","anted","slime","oaten","harsh","touts","stoop","cabal","lazed","elton","skunk","nicer","pesky","kusch","bused","kinda","tunis","enjoy","aches","prowl","babar","rooms","burst","slush","pines","urine","pinky","bayed","mania","light","flare","wares","women","verne","moron","shine","bluer","zeros","bleak","brief","tamra","vasts","jamie","lairs","penal","worst","yowls","pills","taros","addle","alyce","creep","saber","floyd","cures","soggy","vexed","vilma","cabby","verde","euler","cling","wanna","jenny","donor","stole","sakha","blake","sanes","riffs","forge","horus","sered","piked","prosy","wases","glove","onset","spake","benin","talks","sites","biers","wendy","dante","allan","haven","nears","shaka","sloth","perky","spear","spend","clint","dears","sadly","units","vista","hinds","marat","natal","least","bough","pales","boole","ditch","greys","slunk","bitch","belts","sense","skits","monty","yawns","music","hails","alien","gibes","lille","spacy","argot","wasps","drubs","poops","bella","clone","beast","emend","iring","start","darla","bells","cults","dhaka","sniff","seers","bantu","pages","fever","tacky","hoses","strop","climb","pairs","later","grant","raven","stael","drips","lucid","awing","dines","balms","della","galen","toned","snips","shady","chili","fears","nurse","joint","plump","micky","lions","jamal","queer","ruins","frats","spoof","semen","pulps","oldie","coors","rhone","papal","seals","spans","scaly","sieve","klaus","drums","tided","needs","rider","lures","treks","hares","liner","hokey","boots","primp","laval","limes","putts","fonda","damon","pikes","hobbs","specs","greet","ketch","braid","purer","tsars","berne","tarts","clean","grate","trips","chefs","timex","vicky","pares","price","every","beret","vices","jodie","fanny","mails","built","bossy","farms","pubic","gongs","magma","quads","shell","jocks","woods","waded","parka","jells","worse","diner","risks","bliss","bryan","terse","crier","incur","murky","gamed","edges","keens","bread","raced","vetch","glint","zions","porno","sizes","mends","ached","allie","bands","plank","forth","fuels","rhyme","wimpy","peels","foggy","wings","frill","edgar","slave","lotus","point","hints","germs","clung","limed","loafs","realm","myron","loopy","plush","volts","bimbo","smash","windy","sours","choke","karin","boast","whirr","tiber","dimes","basel","cutes","pinto","troll","thumb","decor","craft","tared","split","josue","tramp","screw","label","lenny","apses","slept","sikhs","child","bouts","cites","swipe","lurks","seeds","fists","hoard","steed","reams","spoil","diego","peale","bevel","flags","mazes","quart","snipe","latch","lards","acted","falls","busby","holed","mummy","wrong","wipes","carlo","leers","wails","night","pasty","eater","flunk","vedas","curse","tyros","mirth","jacky","butte","wired","fixes","tares","vague","roved","stove","swoon","scour","coked","marge","cants","comic","corns","zilch","typos","lives","truer","comma","gaily","teals","witty","hyper","croat","sways","tills","hones","dowel","llano","clefs","fores","cinch","brock","vichy","bleed","nuder","hoyle","slams","macro","arabs","tauts","eager","croak","scoop","crime","lurch","weals","fates","clipt","teens","bulls","domed","ghana","culls","frame","hanky","jared","swain","truss","drank","lobby","lumps","pansy","whews","saris","trite","weeps","dozes","jeans","flood","chimu","foxes","gelds","sects","scoff","poses","mares","famed","peers","hells","laked","zests","wring","steal","snoot","yodel","scamp","ellis","bandy","marry","jives","vises","blurb","relay","patch","haley","cubit","heine","place","touch","grain","gerry","badly","hooke","fuchs","savor","apron","judge","loren","britt","smith","tammy","altar","duels","huber","baton","dived","apace","sedan","basts","clark","mired","perch","hulks","jolly","welts","quack","spore","alums","shave","singe","lanny","dread","profs","skeet","flout","darin","newed","steer","taine","salvo","mites","rules","crash","thorn","olive","saves","yawed","pique","salon","ovens","dusty","janie","elise","carve","winds","abash","cheep","strap","fared","discs","poxed","hoots","catch","combo","maize","repay","mario","snuff","delve","cored","bards","sudan","shuns","yukon","jowls","wayne","torus","gales","creek","prove","needy","wisps","terri","ranks","books","dicky","tapes","aping","padre","roads","nines","seats","flats","rains","moira","basic","loves","pulls","tough","gills","codes","chest","teeny","jolts","woody","flame","asked","dulls","hotly","glare","mucky","spite","flake","vines","lindy","butts","froth","beeps","sills","bunny","flied","shaun","mawed","velds","voled","doily","patel","snake","thigh","adler","calks","desks","janus","spunk","baled","match","strip","hosed","nippy","wrest","whams","calfs","sleet","wives","boars","chain","table","duked","riped","edens","galas","huffs","biddy","claps","aleut","yucks","bangs","quids","glenn","evert","drunk","lusts","senna","slate","manet","roted","sleep","loxes","fluky","fence","clamp","doted","broad","sager","spark","belch","mandy","deana","beyer","hoist","leafy","levee","libel","tonic","aloes","steam","skews","tides","stall","rifts","saxon","mavis","asama","might","dotes","tangs","wroth","kited","salad","liens","clink","glows","balky","taffy","sided","sworn","oasis","tenth","blurt","tower","often","walsh","sonny","andes","slump","scans","boded","chive","finer","ponce","prune","sloes","dined","chums","dingo","harte","ahead","event","freer","heart","fetch","sated","soapy","skins","royal","cuter","loire","minot","aisle","horny","slued","panel","eight","snoop","pries","clive","pored","wrist","piped","daren","cells","parks","slugs","cubed","highs","booze","weary","stain","hoped","finny","weeds","fetid","racer","tasks","right","saint","shahs","basis","refer","chart","seize","lulls","slant","belay","clots","jinny","tours","modes","gloat","dunks","flute","conch","marts","aglow","gayer","lazes","dicks","chime","bears","sharp","hatch","forms","terry","gouda","thins","janet","tonya","axons","sewed","danny","rowdy","dolts","hurry","opine","fifty","noisy","spiky","humid","verna","poles","jayne","pecos","hooky","haney","shams","snots","sally","ruder","tempe","plunk","shaft","scows","essie","dated","fleet","spate","bunin","hikes","sodas","filly","thyme","fiefs","perks","chary","kiths","lidia","lefty","wolff","withe","three","crawl","wotan","brown","japed","tolls","taken","threw","crave","clash","layer","tends","notes","fudge","musky","bawdy","aline","matts","shirr","balks","stash","wicks","crepe","foods","fares","rotes","party","petty","press","dolly","mangy","leeks","silly","leant","nooks","chapt","loose","caged","wages","grist","alert","sheri","moody","tamps","hefts","souls","rubes","rolex","skulk","veeps","nonce","state","level","whirl","bight","grits","reset","faked","spiny","mixes","hunks","major","missy","arius","damns","fitly","caped","mucus","trace","surat","lloyd","furry","colin","texts","livia","reply","twill","ships","peons","shear","norms","jumbo","bring","masks","zippy","brine","dorks","roded","sinks","river","wolfs","strew","myths","pulpy","prank","veins","flues","minus","phone","banns","spell","burro","brags","boyle","lambs","sides","knees","clews","aired","skirt","heavy","dimer","bombs","scums","hayes","chaps","snugs","dusky","loxed","ellen","while","swank","track","minim","wiled","hazed","roofs","cantu","sorry","roach","loser","brass","stint","jerks","dirks","emory","campy","poise","sexed","gamer","catty","comte","bilbo","fasts","ledge","drier","idles","doors","waged","rizal","pured","weirs","crisp","tasty","sored","palmy","parts","ethel","unify","crows","crest","udder","delis","punks","dowse","totes","emile","coded","shops","poppa","pours","gushy","tiffs","shads","birds","coils","areas","boons","hulls","alter","lobes","pleat","depth","fires","pones","serra","sweat","kline","malay","ruled","calve","tired","drabs","tubed","wryer","slung","union","sonya","aided","hewed","dicey","grids","nixed","whits","mills","buffs","yucky","drops","ready","yuppy","tweet","napes","cadre","teach","rasps","dowdy","hoary","canto","posed","dumbo","kooks","reese","snaky","binge","byron","phony","safer","friar","novel","scale","huron","adorn","carla","fauna","myers","hobby","purse","flesh","smock","along","boils","pails","times","panza","lodge","clubs","colby","great","thing","peaks","diana","vance","whets","bergs","sling","spade","soaks","beach","traps","aspen","romps","boxed","fakir","weave","nerds","swazi","dotty","curls","diver","jonas","waite","verbs","yeast","lapel","barth","soars","hooks","taxed","slews","gouge","slags","chang","chafe","saved","josie","syncs","fonds","anion","actor","seems","pyrex","isiah","glued","groin","goren","waxes","tonia","whine","scads","knelt","teaks","satan","tromp","spats","merry","wordy","stake","gland","canal","donna","lends","filed","sacks","shied","moors","paths","older","pooch","balsa","riced","facet","decaf","attic","elder","akron","chomp","chump","picky","money","sheer","bolls","crabs","dorms","water","veers","tease","dummy","dumbs","lethe","halls","rifer","demon","fucks","whips","plops","fuses","focal","taces","snout","edict","flush","burps","dawes","lorry","spews","sprat","click","deann","sited","aunts","quips","godly","pupil","nanny","funks","shoon","aimed","stacy","helms","mints","banks","pinch","local","twine","pacts","deers","halos","slink","preys","potty","ruffs","pusan","suits","finks","slash","prods","dense","edsel","heeds","palls","slats","snits","mower","rares","ailed","rouge","ellie","gated","lyons","duded","links","oaths","letha","kicks","firms","gravy","month","kongo","mused","ducal","toted","vocal","disks","spied","studs","macao","erick","coupe","starr","reaps","decoy","rayon","nicks","breed","cosby","haunt","typed","plain","trays","muled","saith","drano","cower","snows","buses","jewry","argus","doers","flays","swish","resin","boobs","sicks","spies","bails","wowed","mabel","check","vapid","bacon","wilda","ollie","loony","irked","fraud","doles","facts","lists","gazed","furls","sunks","stows","wilde","brick","bowed","guise","suing","gates","niter","heros","hyped","clomp","never","lolls","rangy","paddy","chant","casts","terns","tunas","poker","scary","maims","saran","devon","tripe","lingo","paler","coped","bride","voted","dodge","gross","curds","sames","those","tithe","steep","flaks","close","swops","stare","notch","prays","roles","crush","feuds","nudge","baned","brake","plans","weepy","dazed","jenna","weiss","tomes","stews","whist","gibed","death","clank","cover","peeks","quick","abler","daddy","calls","scald","lilia","flask","cheer","grabs","megan","canes","jules","blots","mossy","begun","freak","caved","hello","hades","theed","wards","darcy","malta","peter","whorl","break","downs","odder","hoofs","kiddo","macho","fords","liked","flees","swing","elect","hoods","pluck","brook","astir","bland","sward","modal","flown","ahmad","waled","craps","cools","roods","hided","plath","kings","grips","gives","gnats","tabby","gauls","think","bully","fogey","sawed","lints","pushy","banes","drake","trail","moral","daley","balds","chugs","geeky","darts","soddy","haves","opens","rends","buggy","moles","freud","gored","shock","angus","puree","raves","johns","armed","packs","minis","reich","slots","totem","clown","popes","brute","hedge","latin","stoke","blend","pease","rubik","greer","hindi","betsy","flows","funky","kelli","humps","chewy","welds","scowl","yells","cough","sasha","sheaf","jokes","coast","words","irate","hales","camry","spits","burma","rhine","bends","spill","stubs","power","voles","learn","knoll","style","twila","drove","dacca","sheen","papas","shale","jones","duped","tunny","mouse","floss","corks","skims","swaps","inned","boxer","synch","skies","strep","bucks","belau","lower","flaky","quill","aural","rufus","floes","pokes","sends","sates","dally","boyer","hurts","foyer","gowns","torch","luria","fangs","moats","heinz","bolts","filet","firth","begot","argue","youth","chimp","frogs","kraft","smite","loges","loons","spine","domes","pokey","timur","noddy","doggy","wades","lanes","hence","louts","turks","lurid","goths","moist","bated","giles","stood","winos","shins","potts","brant","vised","alice","rosie","dents","babes","softy","decay","meats","tanya","rusks","pasts","karat","nuked","gorge","kinks","skull","noyce","aimee","watch","cleat","stuck","china","testy","doses","safes","stage","bayes","twins","limps","denis","chars","flaps","paces","abase","grays","deans","maria","asset","smuts","serbs","whigs","vases","robyn","girls","pents","alike","nodal","molly","swigs","swill","slums","rajah","bleep","beget","thanh","finns","clock","wafts","wafer","spicy","sorer","reach","beats","baker","crown","drugs","daisy","mocks","scots","fests","newer","agate","drift","marta","chino","flirt","homed","bribe","scram","bulks","servo","vesta","divas","preps","naval","tally","shove","ragas","blown","droll","tryst","lucky","leech","lines","sires","pyxed","taper","trump","payee","midge","paris","bored","loads","shuts","lived","swath","snare","boned","scars","aeons","grime","writs","paige","rungs","blent","signs","davis","dials","daubs","rainy","fawns","wrier","golds","wrath","ducks","allow","hosea","spike","meals","haber","muses","timed","broom","burks","louis","gangs","pools","vales","altai","elope","plied","slain","chasm","entry","slide","bawls","title","sings","grief","viola","doyle","peach","davit","bench","devil","latex","miles","pasha","tokes","coves","wheel","tried","verdi","wanda","sivan","prior","fryer","plots","kicky","porch","shill","coats","borne","brink","pawed","erwin","tense","stirs","wends","waxen","carts","smear","rival","scare","phase","bragg","crane","hocks","conan","bests","dares","molls","roots","dunes","slips","waked","fours","bolds","slosh","yemen","poole","solid","ports","fades","legal","cedes","green","curie","seedy","riper","poled","glade","hosts","tools","razes","tarry","muddy","shims","sword","thine","lasts","bloat","soled","tardy","foots","skiff","volta","murks","croci","gooks","gamey","pyxes","poems","kayla","larva","slaps","abuse","pings","plows","geese","minks","derby","super","inked","manic","leaks","flops","lajos","fuzes","swabs","twigs","gummy","pyres","shrew","islet","doled","wooly","lefts","hunts","toast","faith","macaw","sonia","leafs","colas","conks","altos","wiped","scene","boors","patsy","meany","chung","wakes","clear","ropes","tahoe","zones","crate","tombs","nouns","garth","puked","chats","hanks","baked","binds","fully","soaps","newel","yarns","puers","carps","spelt","lully","towed","scabs","prime","blest","patty","silky","abner","temps","lakes","tests","alias","mines","chips","funds","caret","splat","perry","turds","junks","cramp","saned","peary","snarl","fired","stung","nancy","bulge","styli","seams","hived","feast","triad","jaded","elvin","canny","birth","routs","rimed","pusey","laces","taste","basie","malls","shout","prier","prone","finis","claus","loops","heron","frump","spare","menus","ariel","crams","bloom","foxed","moons","mince","mixed","piers","deres","tempt","dryer","atone","heats","dario","hawed","swims","sheet","tasha","dings","clare","aging","daffy","wried","foals","lunar","havel","irony","ronny","naves","selma","gurus","crust","percy","murat","mauro","cowed","clang","biker","harms","barry","thump","crude","ulnae","thong","pager","oases","mered","locke","merle","soave","petal","poser","store","winch","wedge","inlet","nerdy","utter","filth","spray","drape","pukes","ewers","kinds","dates","meier","tammi","spoor","curly","chill","loped","gooey","boles","genet","boost","beets","heath","feeds","growl","livid","midst","rinds","fresh","waxed","yearn","keeps","rimes","naked","flick","plies","deeps","dirty","hefty","messy","hairy","walks","leper","sykes","nerve","rover","jived","brisk","lenin","viper","chuck","sinus","luger","ricks","hying","rusty","kathy","herds","wider","getty","roman","sandy","pends","fezes","trios","bites","pants","bless","diced","earth","shack","hinge","melds","jonah","chose","liver","salts","ratty","ashed","wacky","yokes","wanly","bruce","vowel","black","grail","lungs","arise","gluts","gluey","navel","coyer","ramps","miter","aldan","booth","musty","rills","darns","tined","straw","kerri","hared","lucks","metes","penny","radon","palms","deeds","earls","shard","pried","tampa","blank","gybes","vicki","drool","groom","curer","cubes","riggs","lanky","tuber","caves","acing","golly","hodge","beard","ginny","jibed","fumes","astor","quito","cargo","randi","gawky","zings","blind","dhoti","sneak","fatah","fixer","lapps","cline","grimm","fakes","maine","erika","dealt","mitch","olden","joist","gents","likes","shelf","silts","goats","leads","marin","spire","louie","evans","amuse","belly","nails","snead","model","whats","shari","quote","tacks","nutty","lames","caste","hexes","cooks","miner","shawn","anise","drama","trike","prate","ayers","loans","botch","vests","cilia","ridge","thugs","outed","jails","moped","plead","tunes","nosed","wills","lager","lacks","cried","wince","berle","flaws","boise","tibet","bided","shred","cocky","brice","delta","congo","holly","hicks","wraps","cocks","aisha","heard","cured","sades","horsy","umped","trice","dorky","curve","ferry","haler","ninth","pasta","jason","honer","kevin","males","fowls","awake","pores","meter","skate","drink","pussy","soups","bases","noyes","torts","bogus","still","soupy","dance","worry","eldon","stern","menes","dolls","dumpy","gaunt","grove","coops","mules","berry","sower","roams","brawl","greed","stags","blurs","swift","treed","taney","shame","easel","moves","leger","ville","order","spock","nifty","brian","elias","idler","serve","ashen","bizet","gilts","spook","eaten","pumas","cotes","broke","toxin","groan","laths","joins","spots","hated","tokay","elite","rawer","fiats","cards","sassy","milks","roost","glean","lutes","chins","drown","marks","pined","grace","fifth","lodes","rusts","terms","maxes","savvy","choir","savoy","spoon","halve","chord","hulas","sarah","celia","deems","ninny","wines","boggy","birch","raved","wales","beams","vibes","riots","warty","nigel","askew","faxes","sedge","sheol","pucks","cynic","relax","boers","whims","bents","candy","luann","slogs","bonny","barns","iambs","fused","duffy","guilt","bruin","pawls","penis","poppy","owing","tribe","tuner","moray","timid","ceded","geeks","kites","curio","puffy","perot","caddy","peeve","cause","dills","gavel","manse","joker","lynch","crank","golda","waits","wises","hasty","paves","grown","reedy","crypt","tonne","jerky","axing","swept","posse","rings","staff","tansy","pared","glaze","grebe","gonna","shark","jumps","vials","unset","hires","tying","lured","motes","linen","locks","mamas","nasty","mamie","clout","nader","velma","abate","tight","dales","serer","rives","bales","loamy","warps","plato","hooch","togae","damps","ofter","plumb","fifes","filmy","wiper","chess","lousy","sails","brahe","ounce","flits","hindu","manly","beaux","mimed","liken","forts","jambs","peeps","lelia","brews","handy","lusty","brads","marne","pesos","earle","arson","scout","showy","chile","sumps","hiked","crook","herbs","silks","alamo","mores","dunce","blaze","stank","haste","howls","trots","creon","lisle","pause","hates","mulch","mined","moder","devin","types","cindy","beech","tuned","mowed","pitts","chaos","colds","bidet","tines","sighs","slimy","brain","belle","leery","morse","ruben","prows","frown","disco","regal","oaken","sheds","hives","corny","baser","fated","throe","revel","bores","waved","shits","elvia","ferns","maids","color","coifs","cohan","draft","hmong","alton","stine","cluck","nodes","emily","brave","blair","blued","dress","bunts","holst","clogs","rally","knack","demos","brady","blues","flash","goofy","blocs","diane","colic","smile","yules","foamy","splay","bilge","faker","foils","condo","knell","crack","gallo","purls","auras","cakes","doves","joust","aides","lades","muggy","tanks","middy","tarps","slack","capet","frays","donny","venal","yeats","misty","denim","glass","nudes","seeps","gibbs","blows","bobbi","shane","yards","pimps","clued","quiet","witch","boxes","prawn","kerry","torah","kinko","dingy","emote","honor","jelly","grins","trope","vined","bagel","arden","rapid","paged","loved","agape","mural","budge","ticks","suers","wendi","slice","salve","robin","bleat","batik","myles","teddy","flatt","puppy","gelid","largo","attar","polls","glide","serum","fundy","sucks","shalt","sewer","wreak","dames","fonts","toxic","hines","wormy","grass","louse","bowls","crass","benny","moire","margo","golfs","smart","roxie","wight","reign","dairy","clops","paled","oddly","sappy","flair","shown","bulgy","benet","larch","curry","gulfs","fends","lunch","dukes","doris","spoke","coins","manna","conga","jinns","eases","dunno","tisha","swore","rhino","calms","irvin","clans","gully","liege","mains","besot","serge","being","welch","wombs","draco","lynda","forty","mumps","bloch","ogden","knits","fussy","alder","danes","loyal","valet","wooer","quire","liefs","shana","toyed","forks","gages","slims","cloys","yates","rails","sheep","nacho","divan","honks","stone","snack","added","basal","hasps","focus","alone","laxes","arose","lamed","wrapt","frail","clams","plait","hover","tacos","mooch","fault","teeth","marva","mucks","tread","waves","purim","boron","horde","smack","bongo","monte","swirl","deals","mikes","scold","muter","sties","lawns","fluke","jilts","meuse","fives","sulky","molds","snore","timmy","ditty","gasps","kills","carey","jawed","byers","tommy","homer","hexed","dumas","given","mewls","smelt","weird","speck","merck","keats","draws","trent","agave","wells","chews","blabs","roves","grieg","evens","alive","mulls","cared","garbo","fined","happy","trued","rodes","thurs","cadet","alvin","busch","moths","guild","staci","lever","widen","props","hussy","lamer","riley","bauer","chirp","rants","poxes","shyer","pelts","funny","slits","tinge","ramos","shift","caper","credo","renal","veils","covey","elmer","mated","tykes","wooed","briar","gears","foley","shoes","decry","hypes","dells","wilds","runts","wilts","white","easts","comer","sammy","lochs","favor","lance","dawns","bushy","muted","elsie","creel","pocks","tenet","cagey","rides","socks","ogled","soils","sofas","janna","exile","barks","frank","takes","zooms","hakes","sagan","scull","heaps","augur","pouch","blare","bulbs","wryly","homey","tubas","limbo","hardy","hoagy","minds","bared","gabby","bilks","float","limns","clasp","laura","range","brush","tummy","kilts","cooed","worms","leary","feats","robes","suite","veals","bosch","moans","dozen","rarer","slyer","cabin","craze","sweet","talon","treat","yanks","react","creed","eliza","sluts","cruet","hafts","noise","seder","flies","weeks","venus","backs","eider","uriel","vouch","robed","hacks","perth","shiny","stilt","torte","throb","merer","twits","reeds","shawl","clara","slurs","mixer","newts","fried","woolf","swoop","kaaba","oozed","mayer","caned","laius","lunge","chits","kenny","lifts","mafia","sowed","piled","stein","whack","colts","warms","cleft","girds","seeks","poets","angel","trade","parsi","tiers","rojas","vexes","bryce","moots","grunt","drain","lumpy","stabs","poohs","leapt","polly","cuffs","giddy","towns","dacha","quoth","provo","dilly","carly","mewed","tzars","crock","toked","speak","mayas","pssts","ocher","motel","vogue","camps","tharp","taunt","drone","taint","badge","scott","scats","bakes","antes","gruel","snort","capes","plate","folly","adobe","yours","papaw","hench","moods","clunk","chevy","tomas","narcs","vonda","wiles","prigs","chock","laser","viced","stiff","rouse","helps","knead","gazer","blade","tumid","avail","anger","egged","guide","goads","rabin","toddy","gulps","flank","brats","pedal","junky","marco","tinny","tires","flier","satin","darth","paley","gumbo","rared","muffs","rower","prude","frees","quays","homes","munch","beefs","leash","aston","colon","finch","bogey","leaps","tempo","posts","lined","gapes","locus","maori","nixes","liven","songs","opted","babel","wader","barer","farts","lisps","koran","lathe","trill","smirk","mamma","viler","scurf","ravel","brigs","cooky","sachs","fulls","goals","turfs","norse","hauls","cores","fairy","pluto","kneed","cheek","pangs","risen","czars","milne","cribs","genes","wefts","vents","sages","seres","owens","wiley","flume","haded","auger","tatty","onion","cater","wolfe","magic","bodes","gulls","gazes","dandy","snags","rowed","quell","spurn","shore","veldt","turns","slavs","coach","stalk","snuck","piles","orate","joyed","daily","crone","wager","solos","earns","stark","lauds","kasey","villa","gnaws","scent","wears","fains","laced","tamer","pipes","plant","lorie","rivet","tamed","cozen","theme","lifer","sunny","shags","flack","gassy","eased","jeeps","shire","fargo","timer","brash","behan","basin","volga","krone","swiss","docks","booed","ebert","gusty","delay","oared","grady","buick","curbs","crete","lucas","strum","besom","gorse","troth","donne","chink","faced","ahmed","texas","longs","aloud","bethe","cacao","hilda","eagle","karyn","harks","adder","verse","drays","cello","taped","snide","taxis","kinky","penes","wicca","sonja","aways","dyers","bolas","elfin","slope","lamps","hutch","lobed","baaed","masts","ashes","ionic","joyce","payed","brays","malts","dregs","leaky","runny","fecal","woven","hurls","jorge","henna","dolby","booty","brett","dykes","rural","fight","feels","flogs","brunt","preen","elvis","dopey","gripe","garry","gamma","fling","space","mange","storm","arron","hairs","rogue","repel","elgar","ruddy","cross","medan","loses","howdy","foams","piker","halts","jewel","avery","stool","cruel","cases","ruses","cathy","harem","flour","meted","faces","hobos","charm","jamar","cameo","crape","hooey","reefs","denny","mitts","sores","smoky","nopes","sooty","twirl","toads","vader","julep","licks","arias","wrote","north","bunks","heady","batch","snaps","claws","fouls","faded","beans","wimps","idled","pulse","goons","noose","vowed","ronda","rajas","roast","allah","punic","slows","hours","metal","slier","meaty","hanna","curvy","mussy","truth","troys","block","reels","print","miffs","busts","bytes","cream","otter","grads","siren","kilos","dross","batty","debts","sully","bares","baggy","hippy","berth","gorky","argon","wacko","harry","smoke","fails","perms","score","steps","unity","couch","kelly","rumps","fines","mouth","broth","knows","becky","quits","lauri","trust","grows","logos","apter","burrs","zincs","buyer","bayer","moose","overt","croon","ousts","lands","lithe","poach","jamel","waive","wiser","surly","works","paine","medal","glads","gybed","paint","lorre","meant","smugs","bryon","jinni","sever","viols","flubs","melts","heads","peals","aiken","named","teary","yalta","styes","heist","bongs","slops","pouts","grape","belie","cloak","rocks","scone","lydia","goofs","rents","drive","crony","orlon","narks","plays","blips","pence","march","alger","baste","acorn","billy","croce","boone","aaron","slobs","idyls","irwin","elves","stoat","doing","globe","verve","icons","trial","olsen","pecks","there","blame","tilde","milky","sells","tangy","wrack","fills","lofty","truce","quark","delia","stowe","marty","overs","putty","coral","swine","stats","swags","weans","spout","bulky","farsi","brest","gleam","beaks","coons","hater","peony","huffy","exert","clips","riven","payer","doped","salas","meyer","dryad","thuds","tilts","quilt","jetty","brood","gulch","corps","tunic","hubby","slang","wreck","purrs","punch","drags","chide","sulks","tints","huger","roped","dopes","booby","rosin","outer","gusto","tents","elude","brows","lease","ceres","laxer","worth","necks","races","corey","trait","stuns","soles","teems","scrip","privy","sight","minor","alisa","stray","spank","cress","nukes","rises","gusts","aurae","karma","icing","prose","biked","grand","grasp","skein","shaky","clump","rummy","stock","twain","zoned","offed","ghats","mover","randy","vault","craws","thees","salem","downy","sangs","chore","cited","grave","spinx","erica","raspy","dying","skips","clerk","paste","moved","rooks","intel","moses","avers","staid","yawls","blast","lyres","monks","gaits","floor","saner","waver","assam","infer","wands","bunch","dryly","weedy","honey","baths","leach","shorn","shows","dream","value","dooms","spiro","raped","shook","stead","moran","ditto","loots","tapir","looms","clove","stops","pinks","soppy","ripen","wench","shone","bauds","doric","leans","nadia","cries","camus","boozy","maris","fools","morns","bides","greek","gauss","roget","lamar","hazes","beefy","dupes","refed","felts","larry","guile","ables","wants","warns","toils","bathe","edger","paced","rinks","shoos","erich","whore","tiger","jumpy","lamas","stack","among","punts","scalp","alloy","solon","quite","comas","whole","parse","tries","reeve","tiled","deena","roomy","rodin","aster","twice","musts","globs","parch","drawn","filch","bonds","tells","droop","janis","holds","scant","lopes","based","keven","whiny","aspic","gains","franz","jerri","steel","rowel","vends","yelps","begin","logic","tress","sunni","going","barge","blood","burns","basks","waifs","bones","skill","hewer","burly","clime","eking","withs","capek","berta","cheap","films","scoot","tweed","sizer","wheat","acton","flung","ponds","tracy","fiver","berra","roger","mutes","burke","miked","valve","whisk","runes","parry","toots","japes","roars","rough","irons","romeo","cages","reeks","cigar","saiph","dully","hangs","chops","rolls","prick","acuff","spent","sulla","train","swell","frets","names","anita","crazy","sixth","blunt","fewer","large","brand","slick","spitz","rears","ogres","toffy","yolks","flock","gnawn","eries","blink","skier","feted","tones","snail","ether","barbs","noses","hears","upset","awash","cloud","trunk","degas","dungs","rated","shall","yeahs","coven","sands","susan","fable","gunny","began","serfs","balls","dinky","madge","prong","spilt","lilly","brawn","comet","spins","raids","dries","sorts","makes","mason","mayra","royce","stout","mealy","pagan","nasal","folds","libby","coups","photo","mosey","amens","speed","lords","board","fetal","lagos","scope","raked","bonus","mutts","willy","sport","bingo","thant","araby","bette","rebel","gases","small","humus","grosz","beset","slays","steve","scrap","blahs","south","pride","heels","tubes","beady","lacey","genus","mauls","vying","spice","sexes","ester","drams","today","comae","under","jests","direr","yoked","tempi","early","boats","jesus","warts","guppy","gilda","quota","token","edwin","ringo","gaped","lemon","hurst","manor","arrow","mists","prize","silas","blobs","diets","ervin","stony","buddy","bates","rabid","ducat","ewing","jaunt","beads","doyen","blush","thoth","tiles","piper","short","peron","alley","decks","shunt","whirs","cushy","roils","betty","plugs","woken","jibes","foray","merak","ruing","becks","whale","shoot","dwelt","spawn","fairs","dozed","celts","blond","tikes","sabin","feint","vamps","cokes","willa","slues","bills","force","curst","yokel","surer","miler","fices","arced","douse","hilly","lucio","tongs","togas","minty","sagas","pates","welsh","bruno","decal","elate","linux","gyros","pryor","mousy","pains","shake","spica","pupal","probe","mount","shirk","purus","kilns","rests","graze","hague","spuds","sweep","momma","burch","maces","samar","brace","riser","booms","build","camel","flyer","synge","sauna","tonga","tings","promo","hides","clair","elisa","bower","reins","diann","lubed","nulls","picks","laban","milch","buber","stomp","bosom","lying","haled","avert","wries","macon","skids","fumed","ogles","clods","antic","nosey","crimp","purge","mommy","cased","taxes","covet","clack","butch","panty","lents","machs","exude","tooth","adore","shuck","asses","after","terra","dices","aryan","regor","romes","stile","cairo","maura","flail","eaves","estes","sousa","visas","baron","civet","kitty","freed","ralph","tango","gawks","cheat","study","fancy","fiber","musks","souse","brims","claim","bikes","venue","sired","thymi","rivas","skimp","pleas","woman","gimpy","cawed","minos","pints","knock","poked","bowen","risky","towel","oinks","linus","heals","pears","codas","inner","pitch","harpy","niger","madly","bumpy","stair","files","nobel","celli","spars","jades","balmy","kooky","plums","trues","gloss","trims","daunt","tubby","dared","wadis","smell","darby","stink","drill","dover","ruler","laden","dikes","layla","fells","maker","joked","horns","these","baize","spahn","whens","edged","mushy","plume","tucks","spurs","husky","dried","bigot","pupas","drily","aware","hagar","newly","knots","pratt","feces","sabik","watts","cooke","riles","seamy","fleas","dusts","barfs","roans","pawns","vivid","kirks","tania","feral","tubae","horne","aries","brits","combs","chunk","stork","waned","texan","elide","glens","emery","autos","trams","dosed","cheri","baits","jacks","whose","fazed","matte","swans","maxed","write","spays","orion","traci","horse","stars","strut","goods","verge","scuff","award","dives","wires","burnt","dimly","sleds","mayan","biped","quirk","sofia","slabs","waste","robby","mayor","fatty","items","bowel","mires","swarm","route","swash","sooth","paved","steak","upend","sough","throw","perts","stave","carry","burgs","hilts","plane","toady","nadir","stick","foist","gnarl","spain","enter","sises","story","scarf","ryder","glums","nappy","sixes","honed","marcy","offer","kneel","leeds","lites","voter","vince","bursa","heave","roses","trees","argos","leann","grimy","zelma","crick","tract","flips","folks","smote","brier","moore","goose","baden","riled","looks","sober","tusks","house","acmes","lubes","chows","neath","vivas","defer","allay","casey","kmart","pests","proms","eying","cider","leave","shush","shots","karla","scorn","gifts","sneer","mercy","copes","faxed","spurt","monet","awoke","rocky","share","gores","drawl","tears","mooed","nones","wined","wrens","modem","beria","hovel","retch","mates","hands","stymy","peace","carat","coots","hotel","karen","hayed","mamet","cuing","paper","rages","suave","reuse","auden","costs","loner","rapes","hazel","rites","brent","pumps","dutch","puffs","noons","grams","teats","cease","honda","pricy","forgo","fleck","hired","silos","merge","rafts","halon","larks","deere","jello","cunts","sifts","boner","morin","mimes","bungs","marie","harts","snobs","sonic","hippo","comes","crops","mango","wrung","garbs","natty","cents","fitch","moldy","adams","sorta","coeds","gilds","kiddy","nervy","slurp","ramon","fuzed","hiker","winks","vanes","goody","hawks","crowd","bract","marla","limbs","solve","gloom","sloop","eaton","memos","tames","heirs","berms","wanes","faint","numbs","holes","grubs","rakes","waist","miser","stays","antis","marsh","skyed","payne","champ","jimmy","clues","fatal","shoed","freon","lopez","snowy","loins","stale","thank","reads","isles","grill","align","saxes","rubin","rigel","walls","beers","wispy","topic","alden","anton","ducts","david","duets","fries","oiled","waken","allot","swats","woozy","tuxes","inter","dunne","known","axles","graph","bumps","jerry","hitch","crews","lucia","banal","grope","valid","meres","thick","lofts","chaff","taker","glues","snubs","trawl","keels","liker","stand","harps","casks","nelly","debby","panes","dumps","norma","racks","scams","forte","dwell","dudes","hypos","sissy","swamp","faust","slake","maven","lowed","lilts","bobby","gorey","swear","nests","marci","palsy","siege","oozes","rates","stunt","herod","wilma","other","girts","conic","goner","peppy","class","sized","games","snell","newsy","amend","solis","duane","troop","linda","tails","woofs","scuds","shies","patti","stunk","acres","tevet","allen","carpi","meets","trend","salty","galls","crept","toner","panda","cohen","chase","james","bravo","styed","coals","oates","swami","staph","frisk","cares","cords","stems","razed","since","mopes","rices","junes","raged","liter","manes","rearm","naive","tyree","medic","laded","pearl","inset","graft","chair","votes","saver","cains","knobs","gamay","hunch","crags","olson","teams","surge","wests","boney","limos","ploys","algae","gaols","caked","molts","glops","tarot","wheal","cysts","husks","vaunt","beaus","fauns","jeers","mitty","stuff","shape","sears","buffy","maced","fazes","vegas","stamp","borer","gaged","shade","finds","frock","plods","skied","stump","ripes","chick","cones","fixed","coled","rodeo","basil","dazes","sting","surfs","mindy","creak","swung","cadge","franc","seven","sices","weest","unite","codex","trick","fusty","plaid","hills","truck","spiel","sleek","anons","pupae","chiba","hoops","trash","noted","boris","dough","shirt","cowls","seine","spool","miens","yummy","grade","proxy","hopes","girth","deter","dowry","aorta","paean","corms","giant","shank","where","means","years","vegan","derek","tales"])
print time.clock()

s = Solution()
print time.clock()
# print s.combine(20,5)
print time.clock()

print time.clock()
# print s.climbStairs(4)
# print s.climbStairs(5)
# print s.climbStairs(6)
# print s.climbStairs(7)
# print s.climbStairs(8)
# print s.climbStairs(9)
# print s.climbStairs(10)
print time.clock()

t1 = ListNode(1)
t2 = ListNode(2)
t3 = ListNode(3)
t4 = ListNode(4)
t5 = ListNode(5)
t6 = ListNode(6)
t7 = ListNode(7)
t8 = ListNode(8)
t9 = ListNode(9)
t10 = ListNode(10)
t11 = ListNode(11)
t12 = ListNode(12)
t13 = ListNode(13)
t14 = ListNode(14)
t15 = ListNode(15)
t1.next = t2
t2.next = t3
t3.next = t4
t4.next = t5
t5.next = t6
#t6.next = t7
#t7.next = t8
#t8.next = t9
#t9.next = t10
#printlistnode(s.reverseKGroup(t1,3))
printlistnode(s.swapPairs(t1))
print time.clock()
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t7 = TreeNode(7)
t8 = TreeNode(8)
t9 = TreeNode(9)
t10 = TreeNode(10)
t11 = TreeNode(11)
t12 = TreeNode(12)
t13 = TreeNode(13)
t14 = TreeNode(14)
t15 = TreeNode(15)
t1.left = t2
t1.right = t3
t2.left=t4
t2.right=t5
t3.left = t6
t3.right=t7
#t4.left=t8
# t4.right=t9
# t5.left=t10
# t5.right=t11
# t6.left=t12
# t6.right=t13
# t7.left=t14
# t7.right=t15
print s.sumNumbers(t1)
print time.clock()
print s.combinationSum([2],1)
print time.clock()
print s.combinationSum2([14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12], 27)
t1 = TreeNode(1)
t2 = TreeNode(-11)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t7 = TreeNode(7)
t8 = TreeNode(8)
t9 = TreeNode(9)
t10 = TreeNode(10)
t11 = TreeNode(11)
t12 = TreeNode(12)
t13 = TreeNode(13)
t14 = TreeNode(14)
t15 = TreeNode(15)
t1.left = t2
t1.right = t3
t2.left=t4
t2.right=t5
t3.left = t6
t3.right=t7
print s.maxPathSum(t1)
print time.clock()
print s.minWindow("addadfa","aabc")
print time.clock()
print s.maxProfit3([5,2,3,0,3,5,6,8,1,5])

class MinStack:
    def __init__(self):
        self.res = []
        self.minstack = []
    def push(self, x):
        self.res.append(x)
        if len(self.minstack)==0:
            self.minstack.append(x)
        elif x<=self.minstack[-1]:
            self.minstack.append(x)
        else:
            pass
        #self.minstack.append(self.minstack[-1])


    # @return nothing
    def pop(self):
        if len(self.res)>0 and self.res.pop()==self.minstack[-1]:
            self.minstack.pop()


    # @return an integer
    def top(self):
        if len(self.res)>0:
            return self.res[-1]
        return None


    # @return an integer
    def getMin(self):
        if len(self.minstack)>0:
            return self.minstack[-1]
        return None

stack = MinStack()
stack.push(4)
stack.push(2)
print stack.top()
print stack.getMin()
stack.pop()
stack.push(3)
print stack.getMin()

print s.buildTree4([-999,-998,-997,-996,-995,-994,-993,-992,-991,-990,-989,-988,-987,-986,-985,-984,-983,-982,-981,-980,-979,-978,-977,-976,-975,-974,-973,-972,-971,-970,-969,-968,-967,-966,-965,-964,-963,-962,-961,-960,-959,-958,-957,-956,-955,-954,-953,-952,-951,-950,-949,-948,-947,-946,-945,-944,-943,-942,-941,-940,-939,-938,-937,-936,-935,-934,-933,-932,-931,-930,-929,-928,-927,-926,-925,-924,-923,-922,-921,-920,-919,-918,-917,-916,-915,-914,-913,-912,-911,-910,-909,-908,-907,-906,-905,-904,-903,-902,-901,-900,-899,-898,-897,-896,-895,-894,-893,-892,-891,-890,-889,-888,-887,-886,-885,-884,-883,-882,-881,-880,-879,-878,-877,-876,-875,-874,-873,-872,-871,-870,-869,-868,-867,-866,-865,-864,-863,-862,-861,-860,-859,-858,-857,-856,-855,-854,-853,-852,-851,-850,-849,-848,-847,-846,-845,-844,-843,-842,-841,-840,-839,-838,-837,-836,-835,-834,-833,-832,-831,-830,-829,-828,-827,-826,-825,-824,-823,-822,-821,-820,-819,-818,-817,-816,-815,-814,-813,-812,-811,-810,-809,-808,-807,-806,-805,-804,-803,-802,-801,-800,-799,-798,-797,-796,-795,-794,-793,-792,-791,-790,-789,-788,-787,-786,-785,-784,-783,-782,-781,-780,-779,-778,-777,-776,-775,-774,-773,-772,-771,-770,-769,-768,-767,-766,-765,-764,-763,-762,-761,-760,-759,-758,-757,-756,-755,-754,-753,-752,-751,-750,-749,-748,-747,-746,-745,-744,-743,-742,-741,-740,-739,-738,-737,-736,-735,-734,-733,-732,-731,-730,-729,-728,-727,-726,-725,-724,-723,-722,-721,-720,-719,-718,-717,-716,-715,-714,-713,-712,-711,-710,-709,-708,-707,-706,-705,-704,-703,-702,-701,-700,-699,-698,-697,-696,-695,-694,-693,-692,-691,-690,-689,-688,-687,-686,-685,-684,-683,-682,-681,-680,-679,-678,-677,-676,-675,-674,-673,-672,-671,-670,-669,-668,-667,-666,-665,-664,-663,-662,-661,-660,-659,-658,-657,-656,-655,-654,-653,-652,-651,-650,-649,-648,-647,-646,-645,-644,-643,-642,-641,-640,-639,-638,-637,-636,-635,-634,-633,-632,-631,-630,-629,-628,-627,-626,-625,-624,-623,-622,-621,-620,-619,-618,-617,-616,-615,-614,-613,-612,-611,-610,-609,-608,-607,-606,-605,-604,-603,-602,-601,-600,-599,-598,-597,-596,-595,-594,-593,-592,-591,-590,-589,-588,-587,-586,-585,-584,-583,-582,-581,-580,-579,-578,-577,-576,-575,-574,-573,-572,-571,-570,-569,-568,-567,-566,-565,-564,-563,-562,-561,-560,-559,-558,-557,-556,-555,-554,-553,-552,-551,-550,-549,-548,-547,-546,-545,-544,-543,-542,-541,-540,-539,-538,-537,-536,-535,-534,-533,-532,-531,-530,-529,-528,-527,-526,-525,-524,-523,-522,-521,-520,-519,-518,-517,-516,-515,-514,-513,-512,-511,-510,-509,-508,-507,-506,-505,-504,-503,-502,-501,-500,-499,-498,-497,-496,-495,-494,-493,-492,-491,-490,-489,-488,-487,-486,-485,-484,-483,-482,-481,-480,-479,-478,-477,-476,-475,-474,-473,-472,-471,-470,-469,-468,-467,-466,-465,-464,-463,-462,-461,-460,-459,-458,-457,-456,-455,-454,-453,-452,-451,-450,-449,-448,-447,-446,-445,-444,-443,-442,-441,-440,-439,-438,-437,-436,-435,-434,-433,-432,-431,-430,-429,-428,-427,-426,-425,-424,-423,-422,-421,-420,-419,-418,-417,-416,-415,-414,-413,-412,-411,-410,-409,-408,-407,-406,-405,-404,-403,-402,-401,-400,-399,-398,-397,-396,-395,-394,-393,-392,-391,-390,-389,-388,-387,-386,-385,-384,-383,-382,-381,-380,-379,-378,-377,-376,-375,-374,-373,-372,-371,-370,-369,-368,-367,-366,-365,-364,-363,-362,-361,-360,-359,-358,-357,-356,-355,-354,-353,-352,-351,-350,-349,-348,-347,-346,-345,-344,-343,-342,-341,-340,-339,-338,-337,-336,-335,-334,-333,-332,-331,-330,-329,-328,-327,-326,-325,-324,-323,-322,-321,-320,-319,-318,-317,-316,-315,-314,-313,-312,-311,-310,-309,-308,-307,-306,-305,-304,-303,-302,-301,-300,-299,-298,-297,-296,-295,-294,-293,-292,-291,-290,-289,-288,-287,-286,-285,-284,-283,-282,-281,-280,-279,-278,-277,-276,-275,-274,-273,-272,-271,-270,-269,-268,-267,-266,-265,-264,-263,-262,-261,-260,-259,-258,-257,-256,-255,-254,-253,-252,-251,-250,-249,-248,-247,-246,-245,-244,-243,-242,-241,-240,-239,-238,-237,-236,-235,-234,-233,-232,-231,-230,-229,-228,-227,-226,-225,-224,-223,-222,-221,-220,-219,-218,-217,-216,-215,-214,-213,-212,-211,-210,-209,-208,-207,-206,-205,-204,-203,-202,-201,-200,-199,-198,-197,-196,-195,-194,-193,-192,-191,-190,-189,-188,-187,-186,-185,-184,-183,-182,-181,-180,-179,-178,-177,-176,-175,-174,-173,-172,-171,-170,-169,-168,-167,-166,-165,-164,-163,-162,-161,-160,-159,-158,-157,-156,-155,-154,-153,-152,-151,-150,-149,-148,-147,-146,-145,-144,-143,-142,-141,-140,-139,-138,-137,-136,-135,-134,-133,-132,-131,-130,-129,-128,-127,-126,-125,-124,-123,-122,-121,-120,-119,-118,-117,-116,-115,-114,-113,-112,-111,-110,-109,-108,-107,-106,-105,-104,-103,-102,-101,-100,-99,-98,-97,-96,-95,-94,-93,-92,-91,-90,-89,-88,-87,-86,-85,-84,-83,-82,-81,-80,-79,-78,-77,-76,-75,-74,-73,-72,-71,-70,-69,-68,-67,-66,-65,-64,-63,-62,-61,-60,-59,-58,-57,-56,-55,-54,-53,-52,-51,-50,-49,-48,-47,-46,-45,-44,-43,-42,-41,-40,-39,-38,-37,-36,-35,-34,-33,-32,-31,-30,-29,-28,-27,-26,-25,-24,-23,-22,-21,-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599,600,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677,678,679,680,681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,766,767,768,769,770,771,772,773,774,775,776,777,778,779,780,781,782,783,784,785,786,787,788,789,790,791,792,793,794,795,796,797,798,799,800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847,848,849,850,851,852,853,854,855,856,857,858,859,860,861,862,863,864,865,866,867,868,869,870,871,872,873,874,875,876,877,878,879,880,881,882,883,884,885,886,887,888,889,890,891,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920,921,922,923,924,925,926,927,928,929,930,931,932,933,934,935,936,937,938,939,940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989,990,991,992,993,994,995,996,997,998,999,1000,1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068,1069,1070,1071,1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087,1088,1089,1090,1091,1092,1093,1094,1095,1096,1097,1098,1099,1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,1148,1149,1150,1151,1152,1153,1154,1155,1156,1157,1158,1159,1160,1161,1162,1163,1164,1165,1166,1167,1168,1169,1170,1171,1172,1173,1174,1175,1176,1177,1178,1179,1180,1181,1182,1183,1184,1185,1186,1187,1188,1189,1190,1191,1192,1193,1194,1195,1196,1197,1198,1199,1200,1201,1202,1203,1204,1205,1206,1207,1208,1209,1210,1211,1212,1213,1214,1215,1216,1217,1218,1219,1220,1221,1222,1223,1224,1225,1226,1227,1228,1229,1230,1231,1232,1233,1234,1235,1236,1237,1238,1239,1240,1241,1242,1243,1244,1245,1246,1247,1248,1249,1250,1251,1252,1253,1254,1255,1256,1257,1258,1259,1260,1261,1262,1263,1264,1265,1266,1267,1268,1269,1270,1271,1272,1273,1274,1275,1276,1277,1278,1279,1280,1281,1282,1283,1284,1285,1286,1287,1288,1289,1290,1291,1292,1293,1294,1295,1296,1297,1298,1299,1300,1301,1302,1303,1304,1305,1306,1307,1308,1309,1310,1311,1312,1313,1314,1315,1316,1317,1318,1319,1320,1321,1322,1323,1324,1325,1326,1327,1328,1329,1330,1331,1332,1333,1334,1335,1336,1337,1338,1339,1340,1341,1342,1343,1344,1345,1346,1347,1348,1349,1350,1351,1352,1353,1354,1355,1356,1357,1358,1359,1360,1361,1362,1363,1364,1365,1366,1367,1368,1369,1370,1371,1372,1373,1374,1375,1376,1377,1378,1379,1380,1381,1382,1383,1384,1385,1386,1387,1388,1389,1390,1391,1392,1393,1394,1395,1396,1397,1398,1399,1400,1401,1402,1403,1404,1405,1406,1407,1408,1409,1410,1411,1412,1413,1414,1415,1416,1417,1418,1419,1420,1421,1422,1423,1424,1425,1426,1427,1428,1429,1430,1431,1432,1433,1434,1435,1436,1437,1438,1439,1440,1441,1442,1443,1444,1445,1446,1447,1448,1449,1450,1451,1452,1453,1454,1455,1456,1457,1458,1459,1460,1461,1462,1463,1464,1465,1466,1467,1468,1469,1470,1471,1472,1473,1474,1475,1476,1477,1478,1479,1480,1481,1482,1483,1484,1485,1486,1487,1488,1489,1490,1491,1492,1493,1494,1495,1496,1497,1498,1499,1500,1501,1502,1503,1504,1505,1506,1507,1508,1509,1510,1511,1512,1513,1514,1515,1516,1517,1518,1519,1520,1521,1522,1523,1524,1525,1526,1527,1528,1529,1530,1531,1532,1533,1534,1535,1536,1537,1538,1539,1540,1541,1542,1543,1544,1545,1546,1547,1548,1549,1550,1551,1552,1553,1554,1555,1556,1557,1558,1559,1560,1561,1562,1563,1564,1565,1566,1567,1568,1569,1570,1571,1572,1573,1574,1575,1576,1577,1578,1579,1580,1581,1582,1583,1584,1585,1586,1587,1588,1589,1590,1591,1592,1593,1594,1595,1596,1597,1598,1599,1600,1601,1602,1603,1604,1605,1606,1607,1608,1609,1610,1611,1612,1613,1614,1615,1616,1617,1618,1619,1620,1621,1622,1623,1624,1625,1626,1627,1628,1629,1630,1631,1632,1633,1634,1635,1636,1637,1638,1639,1640,1641,1642,1643,1644,1645,1646,1647,1648,1649,1650,1651,1652,1653,1654,1655,1656,1657,1658,1659,1660,1661,1662,1663,1664,1665,1666,1667,1668,1669,1670,1671,1672,1673,1674,1675,1676,1677,1678,1679,1680,1681,1682,1683,1684,1685,1686,1687,1688,1689,1690,1691,1692,1693,1694,1695,1696,1697,1698,1699,1700,1701,1702,1703,1704,1705,1706,1707,1708,1709,1710,1711,1712,1713,1714,1715,1716,1717,1718,1719,1720,1721,1722,1723,1724,1725,1726,1727,1728,1729,1730,1731,1732,1733,1734,1735,1736,1737,1738,1739,1740,1741,1742,1743,1744,1745,1746,1747,1748,1749,1750,1751,1752,1753,1754,1755,1756,1757,1758,1759,1760,1761,1762,1763,1764,1765,1766,1767,1768,1769,1770,1771,1772,1773,1774,1775,1776,1777,1778,1779,1780,1781,1782,1783,1784,1785,1786,1787,1788,1789,1790,1791,1792,1793,1794,1795,1796,1797,1798,1799,1800,1801,1802,1803,1804,1805,1806,1807,1808,1809,1810,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,1821,1822,1823,1824,1825,1826,1827,1828,1829,1830,1831,1832,1833,1834,1835,1836,1837,1838,1839,1840,1841,1842,1843,1844,1845,1846,1847,1848,1849,1850,1851,1852,1853,1854,1855,1856,1857,1858,1859,1860,1861,1862,1863,1864,1865,1866,1867,1868,1869,1870,1871,1872,1873,1874,1875,1876,1877,1878,1879,1880,1881,1882,1883,1884,1885,1886,1887,1888,1889,1890,1891,1892,1893,1894,1895,1896,1897,1898,1899,1900,1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,1917,1918,1919,1920,1921,1922,1923,1924,1925,1926,1927,1928,1929,1930,1931,1932,1933,1934,1935,1936,1937,1938,1939,1940,1941,1942,1943,1944,1945,1946,1947,1948,1949,1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000], [-999,-998,-997,-996,-995,-994,-993,-992,-991,-990,-989,-988,-987,-986,-985,-984,-983,-982,-981,-980,-979,-978,-977,-976,-975,-974,-973,-972,-971,-970,-969,-968,-967,-966,-965,-964,-963,-962,-961,-960,-959,-958,-957,-956,-955,-954,-953,-952,-951,-950,-949,-948,-947,-946,-945,-944,-943,-942,-941,-940,-939,-938,-937,-936,-935,-934,-933,-932,-931,-930,-929,-928,-927,-926,-925,-924,-923,-922,-921,-920,-919,-918,-917,-916,-915,-914,-913,-912,-911,-910,-909,-908,-907,-906,-905,-904,-903,-902,-901,-900,-899,-898,-897,-896,-895,-894,-893,-892,-891,-890,-889,-888,-887,-886,-885,-884,-883,-882,-881,-880,-879,-878,-877,-876,-875,-874,-873,-872,-871,-870,-869,-868,-867,-866,-865,-864,-863,-862,-861,-860,-859,-858,-857,-856,-855,-854,-853,-852,-851,-850,-849,-848,-847,-846,-845,-844,-843,-842,-841,-840,-839,-838,-837,-836,-835,-834,-833,-832,-831,-830,-829,-828,-827,-826,-825,-824,-823,-822,-821,-820,-819,-818,-817,-816,-815,-814,-813,-812,-811,-810,-809,-808,-807,-806,-805,-804,-803,-802,-801,-800,-799,-798,-797,-796,-795,-794,-793,-792,-791,-790,-789,-788,-787,-786,-785,-784,-783,-782,-781,-780,-779,-778,-777,-776,-775,-774,-773,-772,-771,-770,-769,-768,-767,-766,-765,-764,-763,-762,-761,-760,-759,-758,-757,-756,-755,-754,-753,-752,-751,-750,-749,-748,-747,-746,-745,-744,-743,-742,-741,-740,-739,-738,-737,-736,-735,-734,-733,-732,-731,-730,-729,-728,-727,-726,-725,-724,-723,-722,-721,-720,-719,-718,-717,-716,-715,-714,-713,-712,-711,-710,-709,-708,-707,-706,-705,-704,-703,-702,-701,-700,-699,-698,-697,-696,-695,-694,-693,-692,-691,-690,-689,-688,-687,-686,-685,-684,-683,-682,-681,-680,-679,-678,-677,-676,-675,-674,-673,-672,-671,-670,-669,-668,-667,-666,-665,-664,-663,-662,-661,-660,-659,-658,-657,-656,-655,-654,-653,-652,-651,-650,-649,-648,-647,-646,-645,-644,-643,-642,-641,-640,-639,-638,-637,-636,-635,-634,-633,-632,-631,-630,-629,-628,-627,-626,-625,-624,-623,-622,-621,-620,-619,-618,-617,-616,-615,-614,-613,-612,-611,-610,-609,-608,-607,-606,-605,-604,-603,-602,-601,-600,-599,-598,-597,-596,-595,-594,-593,-592,-591,-590,-589,-588,-587,-586,-585,-584,-583,-582,-581,-580,-579,-578,-577,-576,-575,-574,-573,-572,-571,-570,-569,-568,-567,-566,-565,-564,-563,-562,-561,-560,-559,-558,-557,-556,-555,-554,-553,-552,-551,-550,-549,-548,-547,-546,-545,-544,-543,-542,-541,-540,-539,-538,-537,-536,-535,-534,-533,-532,-531,-530,-529,-528,-527,-526,-525,-524,-523,-522,-521,-520,-519,-518,-517,-516,-515,-514,-513,-512,-511,-510,-509,-508,-507,-506,-505,-504,-503,-502,-501,-500,-499,-498,-497,-496,-495,-494,-493,-492,-491,-490,-489,-488,-487,-486,-485,-484,-483,-482,-481,-480,-479,-478,-477,-476,-475,-474,-473,-472,-471,-470,-469,-468,-467,-466,-465,-464,-463,-462,-461,-460,-459,-458,-457,-456,-455,-454,-453,-452,-451,-450,-449,-448,-447,-446,-445,-444,-443,-442,-441,-440,-439,-438,-437,-436,-435,-434,-433,-432,-431,-430,-429,-428,-427,-426,-425,-424,-423,-422,-421,-420,-419,-418,-417,-416,-415,-414,-413,-412,-411,-410,-409,-408,-407,-406,-405,-404,-403,-402,-401,-400,-399,-398,-397,-396,-395,-394,-393,-392,-391,-390,-389,-388,-387,-386,-385,-384,-383,-382,-381,-380,-379,-378,-377,-376,-375,-374,-373,-372,-371,-370,-369,-368,-367,-366,-365,-364,-363,-362,-361,-360,-359,-358,-357,-356,-355,-354,-353,-352,-351,-350,-349,-348,-347,-346,-345,-344,-343,-342,-341,-340,-339,-338,-337,-336,-335,-334,-333,-332,-331,-330,-329,-328,-327,-326,-325,-324,-323,-322,-321,-320,-319,-318,-317,-316,-315,-314,-313,-312,-311,-310,-309,-308,-307,-306,-305,-304,-303,-302,-301,-300,-299,-298,-297,-296,-295,-294,-293,-292,-291,-290,-289,-288,-287,-286,-285,-284,-283,-282,-281,-280,-279,-278,-277,-276,-275,-274,-273,-272,-271,-270,-269,-268,-267,-266,-265,-264,-263,-262,-261,-260,-259,-258,-257,-256,-255,-254,-253,-252,-251,-250,-249,-248,-247,-246,-245,-244,-243,-242,-241,-240,-239,-238,-237,-236,-235,-234,-233,-232,-231,-230,-229,-228,-227,-226,-225,-224,-223,-222,-221,-220,-219,-218,-217,-216,-215,-214,-213,-212,-211,-210,-209,-208,-207,-206,-205,-204,-203,-202,-201,-200,-199,-198,-197,-196,-195,-194,-193,-192,-191,-190,-189,-188,-187,-186,-185,-184,-183,-182,-181,-180,-179,-178,-177,-176,-175,-174,-173,-172,-171,-170,-169,-168,-167,-166,-165,-164,-163,-162,-161,-160,-159,-158,-157,-156,-155,-154,-153,-152,-151,-150,-149,-148,-147,-146,-145,-144,-143,-142,-141,-140,-139,-138,-137,-136,-135,-134,-133,-132,-131,-130,-129,-128,-127,-126,-125,-124,-123,-122,-121,-120,-119,-118,-117,-116,-115,-114,-113,-112,-111,-110,-109,-108,-107,-106,-105,-104,-103,-102,-101,-100,-99,-98,-97,-96,-95,-94,-93,-92,-91,-90,-89,-88,-87,-86,-85,-84,-83,-82,-81,-80,-79,-78,-77,-76,-75,-74,-73,-72,-71,-70,-69,-68,-67,-66,-65,-64,-63,-62,-61,-60,-59,-58,-57,-56,-55,-54,-53,-52,-51,-50,-49,-48,-47,-46,-45,-44,-43,-42,-41,-40,-39,-38,-37,-36,-35,-34,-33,-32,-31,-30,-29,-28,-27,-26,-25,-24,-23,-22,-21,-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599,600,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677,678,679,680,681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,766,767,768,769,770,771,772,773,774,775,776,777,778,779,780,781,782,783,784,785,786,787,788,789,790,791,792,793,794,795,796,797,798,799,800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847,848,849,850,851,852,853,854,855,856,857,858,859,860,861,862,863,864,865,866,867,868,869,870,871,872,873,874,875,876,877,878,879,880,881,882,883,884,885,886,887,888,889,890,891,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920,921,922,923,924,925,926,927,928,929,930,931,932,933,934,935,936,937,938,939,940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989,990,991,992,993,994,995,996,997,998,999,1000,1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068,1069,1070,1071,1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087,1088,1089,1090,1091,1092,1093,1094,1095,1096,1097,1098,1099,1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,1148,1149,1150,1151,1152,1153,1154,1155,1156,1157,1158,1159,1160,1161,1162,1163,1164,1165,1166,1167,1168,1169,1170,1171,1172,1173,1174,1175,1176,1177,1178,1179,1180,1181,1182,1183,1184,1185,1186,1187,1188,1189,1190,1191,1192,1193,1194,1195,1196,1197,1198,1199,1200,1201,1202,1203,1204,1205,1206,1207,1208,1209,1210,1211,1212,1213,1214,1215,1216,1217,1218,1219,1220,1221,1222,1223,1224,1225,1226,1227,1228,1229,1230,1231,1232,1233,1234,1235,1236,1237,1238,1239,1240,1241,1242,1243,1244,1245,1246,1247,1248,1249,1250,1251,1252,1253,1254,1255,1256,1257,1258,1259,1260,1261,1262,1263,1264,1265,1266,1267,1268,1269,1270,1271,1272,1273,1274,1275,1276,1277,1278,1279,1280,1281,1282,1283,1284,1285,1286,1287,1288,1289,1290,1291,1292,1293,1294,1295,1296,1297,1298,1299,1300,1301,1302,1303,1304,1305,1306,1307,1308,1309,1310,1311,1312,1313,1314,1315,1316,1317,1318,1319,1320,1321,1322,1323,1324,1325,1326,1327,1328,1329,1330,1331,1332,1333,1334,1335,1336,1337,1338,1339,1340,1341,1342,1343,1344,1345,1346,1347,1348,1349,1350,1351,1352,1353,1354,1355,1356,1357,1358,1359,1360,1361,1362,1363,1364,1365,1366,1367,1368,1369,1370,1371,1372,1373,1374,1375,1376,1377,1378,1379,1380,1381,1382,1383,1384,1385,1386,1387,1388,1389,1390,1391,1392,1393,1394,1395,1396,1397,1398,1399,1400,1401,1402,1403,1404,1405,1406,1407,1408,1409,1410,1411,1412,1413,1414,1415,1416,1417,1418,1419,1420,1421,1422,1423,1424,1425,1426,1427,1428,1429,1430,1431,1432,1433,1434,1435,1436,1437,1438,1439,1440,1441,1442,1443,1444,1445,1446,1447,1448,1449,1450,1451,1452,1453,1454,1455,1456,1457,1458,1459,1460,1461,1462,1463,1464,1465,1466,1467,1468,1469,1470,1471,1472,1473,1474,1475,1476,1477,1478,1479,1480,1481,1482,1483,1484,1485,1486,1487,1488,1489,1490,1491,1492,1493,1494,1495,1496,1497,1498,1499,1500,1501,1502,1503,1504,1505,1506,1507,1508,1509,1510,1511,1512,1513,1514,1515,1516,1517,1518,1519,1520,1521,1522,1523,1524,1525,1526,1527,1528,1529,1530,1531,1532,1533,1534,1535,1536,1537,1538,1539,1540,1541,1542,1543,1544,1545,1546,1547,1548,1549,1550,1551,1552,1553,1554,1555,1556,1557,1558,1559,1560,1561,1562,1563,1564,1565,1566,1567,1568,1569,1570,1571,1572,1573,1574,1575,1576,1577,1578,1579,1580,1581,1582,1583,1584,1585,1586,1587,1588,1589,1590,1591,1592,1593,1594,1595,1596,1597,1598,1599,1600,1601,1602,1603,1604,1605,1606,1607,1608,1609,1610,1611,1612,1613,1614,1615,1616,1617,1618,1619,1620,1621,1622,1623,1624,1625,1626,1627,1628,1629,1630,1631,1632,1633,1634,1635,1636,1637,1638,1639,1640,1641,1642,1643,1644,1645,1646,1647,1648,1649,1650,1651,1652,1653,1654,1655,1656,1657,1658,1659,1660,1661,1662,1663,1664,1665,1666,1667,1668,1669,1670,1671,1672,1673,1674,1675,1676,1677,1678,1679,1680,1681,1682,1683,1684,1685,1686,1687,1688,1689,1690,1691,1692,1693,1694,1695,1696,1697,1698,1699,1700,1701,1702,1703,1704,1705,1706,1707,1708,1709,1710,1711,1712,1713,1714,1715,1716,1717,1718,1719,1720,1721,1722,1723,1724,1725,1726,1727,1728,1729,1730,1731,1732,1733,1734,1735,1736,1737,1738,1739,1740,1741,1742,1743,1744,1745,1746,1747,1748,1749,1750,1751,1752,1753,1754,1755,1756,1757,1758,1759,1760,1761,1762,1763,1764,1765,1766,1767,1768,1769,1770,1771,1772,1773,1774,1775,1776,1777,1778,1779,1780,1781,1782,1783,1784,1785,1786,1787,1788,1789,1790,1791,1792,1793,1794,1795,1796,1797,1798,1799,1800,1801,1802,1803,1804,1805,1806,1807,1808,1809,1810,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,1821,1822,1823,1824,1825,1826,1827,1828,1829,1830,1831,1832,1833,1834,1835,1836,1837,1838,1839,1840,1841,1842,1843,1844,1845,1846,1847,1848,1849,1850,1851,1852,1853,1854,1855,1856,1857,1858,1859,1860,1861,1862,1863,1864,1865,1866,1867,1868,1869,1870,1871,1872,1873,1874,1875,1876,1877,1878,1879,1880,1881,1882,1883,1884,1885,1886,1887,1888,1889,1890,1891,1892,1893,1894,1895,1896,1897,1898,1899,1900,1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,1917,1918,1919,1920,1921,1922,1923,1924,1925,1926,1927,1928,1929,1930,1931,1932,1933,1934,1935,1936,1937,1938,1939,1940,1941,1942,1943,1944,1945,1946,1947,1948,1949,1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000])
n = s.buildTree2([1,2,3,4,5],[1,2,3,4,5])
print 1

