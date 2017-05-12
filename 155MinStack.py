class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.store = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.store) == 0:
            self.store.append((x,x))
            return
        self.store.append((x,min(x,self.store[-1][1])))

    def pop(self):
        """
        :rtype: void
        """
        self.store.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        if len(self.store)==0:
            return None
        return self.store[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.store) == 0:
            raise IndexError
        return self.store[-1][1]



        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()

if __name__=="__main__":
    minStack = MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    print minStack.getMin();   #--> Returns -3.
    minStack.pop();
    print minStack.top();     # --> Returns 0.
    print minStack.getMin();   #--> Returns -2.