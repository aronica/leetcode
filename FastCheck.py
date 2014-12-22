#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import codecs

from Check import Check


__author__ = 'fafu'


class FastCheck(Check):
    def __init__(self):
        self.fast_check = [0 for i in range(65536)]
        self.fast_length = [0 for i in range(65536)]
        self.char_check = [False for i in range(65536)]
        self.end_check = [False for i in range(65536)]
        self.min_word_length = 10000
        self.max_word_length = 0
        self.hash = set()
        return super(Check, self).__init__()

    def add_word(self, text):
        self.max_word_length = max(self.max_word_length, len(text))
        self.min_word_length = min(self.min_word_length, len(text))
        for i in range(min(7, len(text))):
            self.fast_check[ord(text[i])] |= (1 << i)
        for i in range(7, len(text)):
            self.fast_check[ord(text[i])] |= 0x80
        if len(text) == 1:
            self.char_check[ord(text[0])] = True
        else:
            self.fast_length[ord(text[0])] |= 1 << min(7, len(text) - 2)
            self.end_check[ord(text[len(text) - 1])] = True
            self.hash.add(text)

    def get_bad_word(self, text, offset=0):
        if len(text) is None:
            raise Exception("text should not be None.")
        index = offset
        text = unicode(text[offset:], 'utf-8')
        while index < len(text):
            count = 1
            if index > 0 and self.fast_check[ord(text[index])] & 1 == 0:
                while index < len(text) - 1 and self.fast_check[ord(text[index]) & 1] == 0:
                    index += 1
            ch = text[index]
            if self.min_word_length == 1 and self.char_check[ord(ch)]:
                return index, ch
            for j in range(1, min(self.max_word_length, len(text) - index - 1) + 1):
                current = text[index + j]
                if self.fast_check[ord(current) & 1] == 0:
                    count += 1
                if self.fast_check[ord(current)] & (1 << min(j, 7)) == 0:
                    break;
                if j + 1 >= self.min_word_length:
                    if self.fast_length[ord(ch)] & (1 << min(j - 1, 7)) > 0 and self.end_check[
                        ord(current)] and text[index:index + j + 1] in self.hash:
                        return index, text[index:index + j + 1]
            index += count

    def replace_bad_word(self, text, offset=0, mark='*'):
        if len(text) is None:
            raise Exception("text should not be None.")
        if offset < 0 or offset > len(text):
            raise Exception("Invalid offset value.")
        index = offset
        text = unicode(text[offset:], 'utf-8')
        newValue = list(text)
        while index < len(text):
            count = 1
            if index > 0 and self.fast_check[ord(text[index])] & 1 == 0:
                while index < len(text) - 1 and self.fast_check[ord(text[index + 1]) & 1] == 0:
                    index += 1
            ch = text[index]
            if self.min_word_length == 1 and self.char_check[ord(ch)]:
                newValue[index] = mark
                index += 1
                continue
            for j in range(1, min(self.max_word_length, len(text) - index - 1) + 1):
                current = text[index + j]
                if self.fast_check[ord(current)] & 1 == 0:
                    count += 1
                if self.fast_check[ord(current)] & (1 << min(j, 7)) == 0:
                    break
                if j + 1 >= self.min_word_length:
                    if self.fast_length[ord(ch)] & (1 << min(j - 1, 7)) > 0 and self.end_check[ord(current)]:
                        if text[index:index + j + 1] in self.hash:
                            newValue[index:index + j + 1] = [mark for m in range(index, index + j + 1)]
                            break
            index += count
        return "".join(newValue)


def load(path, checker):
    with codecs.open(path, 'r', encoding='utf-8-sig') as f:
        for line in f.readlines():
            # print line.strip()
            line = line.strip()
            if line.startswith(u'#'):
                continue
            checker.add_word(line)


def main(argv):
    if len(argv) < 2:
        raise Exception("provide at least one parameter")
    check = FastCheck()
    load(argv[1], check)
    print check.get_bad_word('我喜欢毛泽东哈遺囑哈，邓小平')
    print check.replace_bad_word('我喜欢毛泽东哈遺囑哈，邓小平')
    print "Finish"


if __name__ == "__main__":
    main(sys.argv)