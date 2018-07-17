__author__ = 'fafu'


class Solution:
    # max profit of selling stocks
    def maxProfit(self, prices):
        if prices is None or len(prices) == 0:
            return 0
        if len(prices) == 2:
            return max(0, prices[1] - prices[0])
        stack = [prices[len(prices) - 1]]
        for i in xrange(len(prices) - 2, 0, -1):
            stack.append(max(prices[i], stack[len(stack) - 1]))
        profit = 0
        for i in xrange(len(prices) - 1):
            profit = max(profit, stack.pop() - prices[i])
        return profit
