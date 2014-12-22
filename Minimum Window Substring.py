__author__ = 'fafu'
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
