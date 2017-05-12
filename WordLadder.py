__author__ = 'fafu'
class Solution:
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
