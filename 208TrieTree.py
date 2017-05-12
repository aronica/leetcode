class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = [None for i in xrange(26)]
        self.end = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        def __insert__(root,word):
            if len(word) == 0:
                root.end = True
                return
            node = root
            head = ord(word[0]) - ord('a')
            if node.dic[head] is not None:
                __insert__(node.dic[head],word[1:])
            else:
                newnode = TrieNode()
                node.dic[head] = newnode
                __insert__(newnode,word[1:])
        if word is None or len(word) == 0:
            return
        __insert__(self.root,word)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if word is None or len(word)==0:
            return False
        node = self.root
        for i in word:
            i = ord(i)-ord('a')
            if node.dic[i] is not None:
                node = node.dic[i]
            else:
                return False
        return node.end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if prefix is None or len(prefix)==0:
            return False
        node = self.root
        for i in prefix:
            i = ord(i)-ord('a')
            if node.dic[i] is not None:
                node = node.dic[i]
            else:
                return False
        return True
