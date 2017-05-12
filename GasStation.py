__author__ = 'fafu'
class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if len(gas)==1:
            if gas[0]>=cost[0]:
                return 1
            return -1
        gasleft = 0

        i = 0
        startindex = 0
        found = False
        while i<len(gas):
            gasleft += gas[i]-cost[i]
            if gasleft>=0:
                if not found:
                    startindex = i
                    found = True
                gasleft = gasleft - cost[i] + gas[i]
            if gasleft<0 and gas[i]-cost[i]<0:
                found = False
            i += 1
        if gasleft>=0:
            return startindex
        return -1



if __name__=="__main__":
    s = Solution()
    s.canCompleteCircuit([4],[5])

