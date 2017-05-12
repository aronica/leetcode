__author__ = 'fafu'
class Solution:
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
