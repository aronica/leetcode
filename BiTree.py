__author__ = 'fafu'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        assert root is not None
        stack = list()
        result = list()

        node = root
        stack.append(node)

        while len(stack) > 0:
            node = stack.pop()
            result.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return result

    def postorderTraversal(self, root):
        assert root is not None
        stack = list()
        result = list()
        node = root
        last = None
        while node is not None or len(stack) > 0:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.right is None or node.right == last:
                result.append(node.val)
                last = node
                node = None
            else:
                stack.append(node)
                node = node.right
        return result

    def isPalindrome(self, s):
        if s is None or len(s.strip()) == 0:
            return True
        s = s.strip()
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i:i + 1].isalnum():
                i += 1
                continue
            if not s[j:j + 1].isalnum():
                j -= 1
                continue
            first = s[i:i + 1]
            second = s[j:j + 1]
            if first.lower() != second.lower():
                return False
            i += 1
            j -= 1
        return True

    #Pascal's Triangle II
    def getRow(self, rowIndex):
        if rowIndex is None or rowIndex < 0:
            return []
        result = list()
        i = 1
        result.append(1)
        while i < rowIndex + 1:
            j = i - 1
            result.append(1)
            while j > 0:
                result[j] = result[j - 1] + result[j]
                j -= 1
            i += 1
        return result


    #Pascal's Triangle
    def generate(self, numRows):
        if numRows is None or numRows == 0:
            return [[]]
        i = 1
        out = list()
        last = [1]
        out.append(last)
        while i < numRows:
            j = 1
            inner = list()
            inner.append(1)
            while j < i:
                inner.append(last[j - 1] + last[j])
                j += 1
            inner.append(1)
            last = inner
            out.append(inner)
            i += 1
        return out

    #Same Tree Easy
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if (p is None and q is not None) or (p is not None and q is None):
            return False

        if p.val != q.val:
            return False

        T = self.isSameTree(p.left, q.left)
        if not T:
            return False
        T = self.isSameTree(p.right, q.right)
        return T


    #Path Sum
    def hasPathSum(self, root, sum):
        if root is None:
            return False

        stack = list()
        sumofpart = list()

        node = root
        stack.append(node)
        sumofpart.append(node.val)

        while len(stack) > 0:
            node = stack.pop()
            sumofpartial = sumofpart.pop()

            if node.left is None and node.right is None:
                if sumofpartial == sum:
                    return True
            else:
                if node.right is not None:
                    stack.append(node.right)
                    sumofpart.append(sumofpartial + node.right.val)
                if node.left is not None:
                    stack.append(node.left)
                    sumofpart.append(sumofpartial + node.left.val)
        return True



    def minDepth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        elif root.left is not None and root.right is not None:
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            return min(left, right) + 1
        elif root.left is not None:
            return self.minDepth(root.left) + 1
        else:
            return self.minDepth(root.right) + 1

    def isPalindrome(self, x):
        if x < 0:
            return False
        if x < 10:
            return True

        leng = self.length(x)
        i = 0
        j = leng - 1
        while i < j:
            if self.idx(x, i + 1) != self.idx(x, j + 1):
                return False
            i += 1
            j -= 1
        return True

    def idx(self, x, index):
        while index > 1:
            x = x / 10
            index -= 1
        return x % 10

    def length(self, x):
        length = 1
        tmp = 10
        while tmp <= x:
            tmp *= 10
            length += 1
        return length


    def deleteDuplicates(self, head):
        if head is None:
            return
        if head.next is None:
            return

        node = head
        first = node
        while node.next is not None:
            if node.val != node.next.val:
                first.next = node.next
                first = node.next
            node = node.next
        first.next = None

    #Find minimal in rotated sorted array
    def findMin(self, num):
        if num is None:
            return None
        return self.find(num, 0, len(num) - 1)

    def find(self, num, start, end):
        if end - start == 0:
            return num[start]
        if end - start == 1:
            return min(num[start], num[end])
        mid = start + (end - start) / 2
        if num[start] < num[mid] and num[mid] > num[end]:
            return self.find(num, mid + 1, end)
        elif num[start] < num[mid] and num[mid] < num[end]:
            return num[start]
        else:
            return self.find(num, start, mid)

    #Remove Element
    def removeElement(self, A, elem):
        if A is None or elem is None: return 0
        if len(A) == 1:
            if A[0] == elem:
                return 0
            else:
                return 1
        i = 0
        last = len(A) - 1
        while i <= last:
            if A[i] == elem:
                while i<= last and A[last] == elem:
                    last -= 1
                    A.pop()
                if i < last:
                    A[i] = A[last]
                    A.pop()
                    last -= 1
            i += 1
        return last + 1

    #Is Number
    def isNumber(self, s):
        if s is None:
            return False
        s = s.strip()
        if len(s) == 0:
            return False
        if s[0] == "e" or s[0] == "E" or s[len(s)-1] == "e" or s[len(s) -1] == "E":
            return False

        ecount = -1
        pointcount = -1
        pointhead = False
        sign = -1
        for index,i in enumerate(s):
            if i.isdigit():
                continue
            elif i == "e" or i == "E":
                if pointhead and index == 1:
                    return False
                if ecount == -1:
                    if i == (len(s) - 1) or i == 0:
                        return False
                    ecount = index
                else:
                    return False
            elif i == "." :
                if sign == 0 and index == 1 and len(s) == 2:
                    return False
                if ecount != -1:
                    return False

                if index == 0:
                    pointhead = True
                if pointcount == -1:
                    if len(s) == 1:
                        return False
                    pointcount = index
                else:
                    return False
            elif i=="-" or i== "+":
                if index == 0:
                    sign = 0
                elif ecount != (index-1):
                    return False
                elif index == len(s)-1:
                    return False

            else:
                return False
        return True

    #Merge Sorted Array
    def merge(self, A, m, B, n):
        indexa = m-1
        indexb = n-1
        i = 0
        while indexa >= 0 and indexb>=0:
            if B[indexb]>A[indexa]:
                A[indexa+indexb+1] = B[indexb]
                indexb -= 1
            else:
                A[indexa+indexb+1] = A[indexa]
                indexa -= 1
        while indexb >= 0:
            A[indexb] = B[indexb]
            indexb -= 1
        return A
    #Remove Duplicates from Sorted Array
    def removeDuplicates(self, A):
        if A is None or len(A) == 0:
            return 0
        if len(A) == 1:
            return 1
        cursor = A[0]
        i = 1
        duplicated = 0
        while i<len(A):
            if A[i] == cursor:
                duplicated += 1
            else:
                cursor = A[i]
            i += 1
        print duplicated
        cursor = A[0]
        i = 1
        j = 1
        left = len(A) - duplicated
        while i < left:
            if A[j] != cursor:
                A[i] = A[j]
                i += 1
                cursor = A[j]
            j += 1
        del A[left:]
        return len(A)

    #Remove Nth Node From End of List
    def removeNthFromEnd(self, head, n):
        if head is None or n is None:
            return head
        node = head
        tail = node
        pre = head
        for i in range(n):
            if node is not None:
                pre = node
                node = node.next
            elif i == n-1:
                head = head.next
                return head
            else:
                return head

        if node is None and i == n-1:
            head = head.next
            return head

        while node.next is not None:
            node = node.next
            tail = tail.next

        if tail is not None and tail.next is not None:
            tail.next = tail.next.next
        elif tail is not None and tail.next is None:
            tail.next = None
        return head

    #string to integer
    def atoi(self, str):
        if str is None:
            return 0

        str = str.strip()
        tmp = 0
        start = 0

        if len(str) == 0:
            return 0
        sign = 0
        if str[0] == "-":
            sign = 1
            start = 1
        elif str[0] == "+":
            sign = 0
            start = 1
        elif not self.isNumeric(str[0]):
            return
        else:
            #tmp = int(str[0])
            pass



        for j in range(start,len(str)):
            i = str[j]
            if not self.isNumeric(i):
                break
            if sign == 0:
                if tmp>214748364 or (tmp == 214748364 and int(i)>7):
                    return 2147483647
            elif sign == 1:
                if tmp>214748364 or (tmp == 214748364 and int(i)>8):
                    return -2147483648
            tmp = tmp*10 + int(i)
        if sign == 1:
            return tmp*-1
        return tmp

    def isNumeric(self,char):
        return "0"<=char and char<="9"


    #max product
    def maxProduct(self,A):
        if A is None or len(A) == 0:
            return 0
        if len(A) == 1:
            return A[0]
        maxone = A[0]
        # for i in A:
        #     if i>maxone:
        #         maxone = i
        amax = dict()
        if A[0] > 0:
            amax[0] = (None,None,A[0])
        elif A[0] < 0:
            amax[0] = (A[0],None,None)
        else:
            amax[0] = (None,0,None)

        for i in xrange(1,len(A)):
            #for j in xrange(0,i + 1):
            negmax = amax[i-1][0]
            zeromax = amax[i-1][1]
            posmax = amax[i-1][2]

            new_negmax = None
            new_zeromax = None
            new_posmax = None

            if A[i]<0:
                if negmax is not None:
                    new_posmax = negmax * A[i]
                if posmax is not None:
                    new_negmax = min(A[i],A[i]*posmax)
                else:
                    new_negmax = A[i]
                if zeromax is not None:
                    new_zeromax = 0
            elif A[i] == 0:
                new_posmax = 0
                new_negmax = 0
                new_zeromax = 0
            elif A[i]>0:
                if negmax is not None:
                    new_negmax = negmax*A[i]
                if posmax is not None:
                    new_posmax = max(A[i],A[i]*posmax)
                else:
                    new_posmax = A[i]
                if zeromax is not None:
                    new_zeromax = 0
            maxone = max(maxone,new_posmax,new_zeromax,new_negmax)
            amax[i] = (new_negmax,new_zeromax,new_posmax)
        return maxone

    def sortList(self, head):
        assert head is not None
        if head.next is None:
            return head
        if head.next.next is None:
            next = head.next
            if head.val>next.val:
                head.next = None
                next.next = head
                return next
            return head

        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        head2 = slow.next
        slow.next = None

        subhead1 = self.sortList(head)
        subhead2 = self.sortList(head2)
        return self.merge(subhead1,subhead2)

    def merge(self, first,second):
        if first is None:
            return second
        if second is None:
            return first
        node1 = first
        node2 = second
        oldnode1 = first
        oldnode2 = second
        head = None
        if node1.val<=node2.val:
            head = node1
        else:
            head = node2

        while node1 is not None and node2 is not None:
            while node1 is not None and node2 is not None and node1.val<=node2.val:
                oldnode1 = node1
                node1 = node1.next
            if node2 is not None and oldnode1.val<=node2.val:
                oldnode1.next = node2
            elif node2 is None:
                break

            while node2 is not None and node1 is not None and node2.val<node1.val:
                oldnode2 = node2
                node2 = node2.next
            if node1 is not None and oldnode2.val<node1.val:
                oldnode2.next = node1
            elif node1 is None:
                break
        return head

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














    #max product
    def maxProduct2(self, A):
        if A is None or len(A) == 0:
            return 0
        if len(A) == 1:
            return A[0]

        negative = 0
        maxone = A[0]
        for i in A:
            if i<0:
                negative += 1
            if i>maxone:
                maxone = i
        fn = 0
        if max < 0:
            fn = 1
        foundmax = max
        j = 1
        startindex = 0
        negativestart = -1
        if A[0] < 0:
            negativestart = 0
        while j<len(A):
            i = A[j]
            if abs(max) < 1:
                startindex = j
                max = i
                if i < 0:
                    if negativestart == -1:
                        negativestart = j
                else:
                    negativestart = -1
            else:
                if max < 0 and (negative - fn == 0):
                    max = i
                    startindex = j
                    if i < 0:
                        if negativestart == -1:
                            negativestart = j
                        else:
                            negativestart = -1
                    else:
                        negativestart = -1
                    j += 1
                    continue
                elif max < 0 and i<0:
                    max *=i
                    if negativestart == -1:
                        negativestart = j
                elif max > 0 and i<0 and negative-fn == 1:
                    if j < len(A)- 1:
                        if negativestart == -1:
                            max = A[j+1]
                            startindex = j + 1
                            if max < 0 and negativestart == -1:
                                negativestart = j + 1
                            else:
                                negativestart = -1
                            j = j + 2
                            continue
                        else:
                            currentmax = max
                            while startindex <= negativestart:
                                max /= A[startindex]
                                startindex += 1
                            found = False
                            max *= A[j]
                            newstart = startindex
                    else:
                        currentmax = max
                        max *= A[j]
                        if negativestart != -1:
                            while startindex<j:
                                max /= A[startindex]

                                if max>currentmax:
                                    currentmax = max
                                startindex+=1

                            max = currentmax
                        break
                else:
                    if i<0:
                        if negativestart == -1:
                            negativestart = j
                    max *= i
            if i<0:
                fn += 1
            if foundmax<max:
                foundmax = max
            if foundmax < i:
                foundmax = i
            j += 1
        if foundmax<max:
            foundmax = max
        if foundmax < maxone:
            foundmax = maxone
        return foundmax

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
    #Linked List Cycle
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
        fast = head.next.next
        slow = head.next
        while True:
            if fast is None or fast.next is None or fast.next.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
    #linked list cycle II ,first found the node which we found while we looking for if it has a cycle,
    #if found, then the linkedlist starts from head and the linkedlist starts from the founded node will meet
    #at the node where the cycle begins and the lengths until this node of two linkedlist must be equal.
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None
        if head.next == head:
            return head
        slow = head
        fast = head
        hasCycle = False
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                hasCycle = True
                break
        if hasCycle:
            slow = head
            while slow != fast:
                fast = fast.next
                slow = slow.next
            return fast
        return None

    #word break
    def wordBreak(self, s, dict):
        dic = set(dict)
        if s is None or len(dic) == 0:
            return False
        if s in dic:
            return True
        dp = {-1:True}
        for i in xrange(0,len(s)):
            for j in xrange(0,i+1):
                if s[i-j:i+1] in dict and dp[i-j-1]:
                    dp[i] = True
                    break
            dp[i] = i in dp or False

        return dp[len(s)-1]

    def wordBreak2(self, s, dict):
        pass

    def dfs(self,length,ran,index,tmplist,result):
        if index == length:
            return tmplist
        for i in tmplist:
            if len(i)<2:
                continue
            j = len(i)-2
            while j>=0 and i[j] >= i[j+1]:
                    i.pop()
                    j -= 1
        if ran[index] is not None:
            for i in ran[index]:
                [item.append(i) for item in tmplist]
                if i == length-1:
                    result.extend(tmplist)
                else:
                    if i+1 in ran:
                        self.dfs(length,ran,i+1,tmplist,result)



    #3Sum
    def threeSum(self, num):
        A = sorted(num)
        result = []
        i = 0
        pre = None
        while i<len(num)-2 and A[i] <= 0:
            if A[i] == pre:
                i += 1
                continue
            m = i+1
            n = len(num) -1
            while m<n:
                if A[m] + A[n] + A[i] == 0:
                    if len(result) >0:
                        tmp = result[len(result)-1]
                        if tmp[0] != A[i] or tmp[1] != A[m] or tmp[2] != A[n]:
                            result.append([A[i],A[m],A[n]])
                    else:
                        result.append([A[i],A[m],A[n]])
                    m += 1
                    n -= 1
                elif A[m] + A[n] > -A[i]:
                    n -= 1
                elif A[m] + A[n] < -A[i]:
                    m += 1
            pre = A[i]
            i += 1
        return result

    def canCompleteCircuit(self, gas, cost):
        if gas is None or cost is None or len(gas)!= len(cost):
            return -1
        length = len(gas)
        for index in range(0,length):
            i = index
            gasleft = gas[i]
            path = 0
            while gasleft >= cost[i] and path<length:
                gasleft = gasleft - cost[i] + gas[self.next(i,length)]
                path += 1
                i = self.next(i,length)
            if path == length:
                return i
            continue
        return -1


    def next(self,i,length):
        if i == length -1:
            return 0
        return i + 1

    #divide two integers
    def divide(self, dividend, divisor):
        if dividend is None or divisor is None:
            return None
        if divisor == 0:
            return None
        if dividend == 0:
            return 0


        pos = True
        if dividend <0 and divisor<0:
            dividend = 0 -  dividend
            divisor = 0 - divisor

        if (dividend>0 and divisor <0) or (dividend<0 and divisor>0):
            pos = False

        if not pos:
            if dividend < 0:
                dividend = 0 - dividend
            elif divisor < 0:
                divisor = 0 - divisor
        if pos:
            if dividend< divisor:
                return 0
        else:
            if dividend<divisor:
                return 0


        partial = []
        cumulative = divisor
        times = 1
        while dividend >= cumulative:
            partial.append((cumulative,times))
            cumulative = cumulative<<1
            time = times<<1

        pair = partial.pop()
        result = pair[1]
        dividend -= pair[0]

        index = len(partial)
        while dividend >= divisor and len(partial)>0:
            pair = partial.pop()
            value = pair[0]
            times = pair[1]
            if dividend >= value:
                result += times
                dividend -= value
        if pos:
            return result
        else:
            if dividend == 0:
                return 0 - result
            else:
                return 0 - result
    #Evaluate Reverse PolishN Notation
    def evalRPN(self, tokens):
        pom = "+-"
        mod = "*/"
        if tokens is None or len(tokens) == 0:
            return 0
        numstack = list()
        operstack = list()
        for i in range(0,len(tokens)):
            item = tokens[i]
            if item not in pom and item not in mod:
                numstack.append(int(item))
            else:
                num1 = numstack.pop()
                num2 = numstack.pop()
                if item == "+":
                    if i == len(tokens) -1:
                        return num1 + num2
                    else:
                        numstack.append(num1 + num2)
                elif item == "-":
                    if i == len(tokens) -1:
                        return num2 - num1
                    else:
                        numstack.append(num2 - num1)
                elif item == "*":
                    if i == len(tokens) -1:
                        return num1 * num2
                    else:
                        numstack.append(num1 * num2)
                elif item == "/":
                    if i == len(tokens) -1:
                        return self.divide(num2,num1)
                    else:
                        numstack.append(self.divide(num2,num1))
    def divide(self, num1 , num2):
        if num1> 0 and num2 <0:
            return num1/-num2 * -1
        elif num1<0 and num2>0:
            return -num1/num2 * -1
        else:
            return num1/num2

    #Binary Tree Level Order Traverse
    def levelOrder(self, root):
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [[root.val]]
        node = root
        result = []
        nextlevel = [node]
        while len(nextlevel) > 0:
            level = nextlevel
            nextlevel = []
            for i in level:
                if i.left is not None:
                    nextlevel.append(i.left)
                if i.right is not None:
                    nextlevel.append(i.right)
            result.append([x.val for x in level])
        return result

    #Bottom Binary Tree Level Order Traverse
    def levelOrderBottom(self, root):
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [[root.val]]
        node = root
        result = []
        nextlevel = [node]
        while len(nextlevel) > 0:
            level = nextlevel
            nextlevel = []
            for i in level:
                if i.left is not None:
                    nextlevel.append(i.left)
                if i.right is not None:
                    nextlevel.append(i.right)
            result.append([x.val for x in level])
        result.reverse()
        return result




n1 = ListNode(1)
n2 = ListNode(1)
n3 = ListNode(2)
n4 = ListNode(3)
n5 = ListNode(3)
n6 = ListNode(3)
n7 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
s = Solution()
n = n1
while n is not None:
    print n.val
    n = n.next
s.deleteDuplicates(n1)
print "after"
n = n1
while n is not None:
    print n.val
    n = n.next

s = Solution()
print s.generate(5)
print "ok"

print s.getRow(5)

s = Solution()
print s.isPalindrome(3456), "3456 is Palindrome"
print s.isPalindrome(343), "343 is Palindrome"
print s.isPalindrome(3443), "3443 is Palindrome"

num = [3, 4, 5, 6, 7, 0, 1, 2, 3]
print "Find minimal in rotated sorted array:", num, " result is:", s.findMin(num)

num = [3, 4, 5, 6, 7, 2]
print "Find minimal in rotated sorted array:", num, " result is:", s.findMin(num)

num = [3, 0, 1, 2]
print "Find minimal in rotated sorted array:", num, " result is:", s.findMin(num)

num = [3, 4, 2]
print "Find minimal in rotated sorted array:", num, " result is:", s.findMin(num)

num = [4, 3]
print "Find minimal in rotated sorted array:", num, " result is:", s.findMin(num)

num = [1, 2, 3]
print "Find minimal in rotated sorted array:", num, " result is:", s.findMin(num)

arr = [1,1,2,2,3,1,3,4,5]
print "Remove Element:",arr," result is ",s.removeElement(arr,1)
arr = [1,2,3]
print "Remove Element:",arr," result is ",s.removeElement(arr,1)
arr = [1]
print "Remove Element:",arr," result is ",s.removeElement(arr,1)
arr = []
print "Remove Element:",arr," result is ",s.removeElement(arr,1)
arr = [2,1,1]
print "Remove Element:",arr," result is ",s.removeElement(arr,1)
arr = [2,3,1,1,2,1]
print "Remove Element:",arr," result is ",s.removeElement(arr,1)

arr = [1,1]
print "Remove Element:",arr," result is ",s.removeElement(arr,1)

print "isNumber(.e1)",s.isNumber(".e1")

A = [1,1,3,3,3,5,6,7,8]
print "removeDuplicates:",A,"reslt is :",s.removeDuplicates(A)

A = [1,1]
print "removeDuplicates:",A,"reslt is :",s.removeDuplicates(A)

A = [1,1,4,4,4]
print "removeDuplicates:",A,"reslt is :",s.removeDuplicates(A)

A = []
print "removeDuplicates:",A,"reslt is :",s.removeDuplicates(A)

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7

s = Solution()
print "removeNthFromEnd:"
node = n1

node = n7
node = s.removeNthFromEnd(node,1)

while node is not None:
    print node.val,"->"
    node = node.next
print "n7========"
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
node = n1
node = s.removeNthFromEnd(node,7)

while node is not None:
    print node.val,"->"
    node = node.next
print "n7========"
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
node = n5
node = s.removeNthFromEnd(node,1)

while node is not None:
    print node.val,"->"
    node = node.next

print "n7========"
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
node = n6
node = s.removeNthFromEnd(node,2)

#string to integer
print "+23",s.atoi("+23")
print "-23",s.atoi("-23")
print "2147483648",s.atoi("2147483648")
print "-2147483649",s.atoi("-2147483649")
print " 123a d " ,s.atoi(" 123a d " )
print "  aa213 ",s.atoi("  aa213")

print "-0012a42",s.atoi("-0012a42")


while node is not None:
    print node.val,"->"
    node = node.next

#max product
A = [1,2,-2,4]
print "max product:",A," result:",s.maxProduct(A)

A = [0.1,0.2,-0.2,.4]
print "max product:",A," result:",s.maxProduct(A)

A = [0.1,2,-2,4,-2,0.1]
print "max product:",A," result:",s.maxProduct(A)

A = [1,0,4,-4,3]
print "max product:",A," result:",s.maxProduct(A)

A = [1,0,4,-4,3,-2]
print "max product:",A," result:",s.maxProduct(A)

A = [0.2,03,05]
print "max product:",A," result:",s.maxProduct(A)

A = [-2,-3,-3]
print "max product:",A," result:",s.maxProduct(A)

A = [-2,-3,-3,-3]
print "max product:",A," result:",s.maxProduct(A)

A = [2,-5,-2,-4,3]
print "max product:",A," result:",s.maxProduct(A)

A = [3,-1,4]
print "max product:",A," result:",s.maxProduct(A)

A = [-2,1,0]
print "max product:",A," result:",s.maxProduct(A)

A = [-1,0,-1,2,-3,1,2,3,-2]
print "max product:",A," result:",s.maxProduct(A)


n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
#n7.next = n1

print "reorder list:",s.reorderList(n1)
node = n1
while node is not None:
    print node.val,"->"
    node = node.next
print "=====>"

n1.next = n2
n2.next = n3
n3.next = n3
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n4
print "hasCycle:",s.hasCycle(n1)
print "detectCycle:",s.detectCycle(n1).val

print "wordBreak:",s.wordBreak("aaaaaaa",["aaaa","aa"])
print "wordBreak2:",s.wordBreak2(	"abcd", ["a","abc","b","cd"])
#print "wordBreak:",s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
print "3Sum:",s.threeSum([0,0,0,0])
print "3Sum:",s.threeSum([7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6])
print "3Sum:",s.threeSum([-1,0,1,2,-1,-4])

print "divideTwoInteger,s.divide(1,1)=",s.divide(1,1)
print "divideTwoInteger,s.divide(40,3)=",s.divide(40,3)
print "divideTwoInteger,s.divide(40,-3)",s.divide(40,-3)
print "divideTwoInteger,s.divide(40,4)",s.divide(40,4)
print "divideTwoInteger,s.divide(40,-4)",s.divide(40,-4)
print "divideTwoInteger,s.divide(40,1)",s.divide(40,1)
print "divideTwoInteger,s.divide(40,41)",s.divide(40,41)
print "divideTwoInteger,s.divide(40,-41)",s.divide(40,-41)
print "divideTwoInteger,s.divide(0,-4)",s.divide(0,-4)
print "divideTwoInteger,s.divide(3,-4)",s.divide(3,-4)
print "divideTwoInteger,s.divide(3,4)",s.divide(3,4)
print "divideTwoInteger,s.divide(-3,4)",s.divide(-3,4)
print "divideTwoInteger,s.divide(1004958205,-2137325331)",s.divide(1004958205,-2137325331)

print """evalRPN(["2", "1", "+", "3", "*"]):""",s.evalRPN(["2", "1", "+", "3", "*"])
print """evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]):""",s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])

n1 = TreeNode(1)

n2 = TreeNode(2)
n1.left = n2
#print "Bottom Level Order Traverse:",s.levelOrderBottom(n1)


n1.next = n3
n3.next = n7
n7.next = n2
n2.next = n4
n4.next = n5
n5.next = n6
n6.next = None
newhead = s.sortList(n1)
print "sortedList():"
node = newhead
while node is not None:
    print node.val,"->"
    node = node.next
print "=====>"

print s.mergeKLists([[],[-2],[-3,-2,1]])
def test1(self):
    n1 = TreeNode(1)

    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n8 = TreeNode(8)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7

    n4.right = n8


s = Solution()
print s.isPalindrome("A man, a plan, a canal: Panama")

