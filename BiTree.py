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


class Solution:

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




    #







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

