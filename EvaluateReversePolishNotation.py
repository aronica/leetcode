__author__ = 'fafu'
class Solution:
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
