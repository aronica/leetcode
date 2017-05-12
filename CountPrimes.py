__author__ = 'fafu'
import math
from time import clock
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        if n < 4:
            return 1
        if n < 6:
            return 2
        if n < 8:
            return 3
        if n < 12:
            return 4
        prime = [3, 5, 7, 11]
        s = {
            3 : set([2])
        }
        idx = 0
        large = prime[idx+1]*prime[idx+1]
        for i in xrange(13, n, 2):
            is_prime = True
            is_prime2 = True
            for m in s:
                if prime[idx] - ((i - prime[-1]) % m) in s[m]:# not prime
                    is_prime = False
                    break
            if is_prime:
                for m in s:
                    s[m].add(i % m)
            if i >= large:
                idx += 1
                large = prime[idx]*prime[idx]
                if i == large:
                    is_prime = False
                    #s[prime[idx]] = set([prime[k]%prime[idx] for k in xrange(idx+1,len(prime))])
                    break
                else:
                    for m in s:
                        left = i % m
                        if left == 0:
                            is_prime2 = False
                            break
            else:
                if is_prime and is_prime2:
                    prime.append(i)
            for m in xrange(idx+1):
                s[prime[m]] = set([prime[n]%prime[m] for n in xrange(idx+1,len(prime))])




        return prime

if __name__ == "__main__":
    s = Solution()
    clock()
    print s.countPrimes(30)
    print clock()
