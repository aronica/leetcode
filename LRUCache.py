__author__ = 'fafu'
from collections import deque
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.indexcache = dict()
        self.last_get_index = 0
        self.last_invalid_index = 0



    # @return an integer
    def get(self, key):
        if key in self.cache:
            val = self.cache[key]
            self.last_get_index += 1
            self.cache[key] = (val[0],self.last_get_index)
            return val[0]
        return -1


    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        self.last_get_index += 1
        if len(self.cache)<self.capacity:
            self.cache[key] = (value,self.last_get_index)
        else:

            self.cache[key] = (value,self.last_get_index)



