__author__ = 'fafu'
import time


class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.queue = []

    # @return an integer
    def get(self, key):
        if key in self.cache:
            val = self.cache[key]
            self.cache[key] = (val, time.time())
            self.queue.append(key, time.self.cache[key][1])
            if len(self.queue) >= self.capacity * 2:
                i = 0
                while i < (self.capacity):
                    if self.queue[i][1] != self.cache[self.queue[i][1]]:
                        self.queue.pop(i)
                    else:
                        i += 1
            return val[0]
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        self.get(key)
        self.cache[key] = (value, time.time())
        self.queue.append((key, time.self.cache[key][1]))
        if len(self.cache) > self.capacity:
            while True:
                obj = self.queue.pop(0)
                if self.cache[obj[0]][1] == obj[1]:
                    del self.cache[obj[0]]
                    break





