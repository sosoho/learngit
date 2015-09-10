#!/usr/bin/python
# -*- encoding: gbk -*-

import codecs
import time
import sys

class TrieNode:

    def __init__ (self):
        self.val = 0
        self.trans = {}

class Trie (object):
    def __init__ (self):
        self.root = TrieNode()

    def __walk (self, trienode, ch):
        if ch in trienode.trans:
            trienode = trienode.trans[ch]
            return trienode, trienode.val
        else:
            return None, 0

    def add (self, word, value=1):
        curr_node = self.root
        for ch in word:
            try:
                curr_node = curr_node.trans[ch]
            except:
                curr_node.trans[ch] = TrieNode()
                curr_node = curr_node.trans[ch]

        curr_node.val = value


    def _find_ch(self,curr_node,ch,word,start,limit):
           curr_node, val = self.__walk (curr_node, ch)
           if val:
               return val
           while curr_node is not None and start<(limit-1):
               start= start+1
               ch = word[start]
               curr_node, val = self.__walk (curr_node, ch)
               if val:
                   return val

    def match_all (self, word):
        ret = []
        curr_node = self.root
        index = 0
        size = len(word)
        while index<size:
            val = self._find_ch(curr_node,word[index], word, index, size)
            if val:
                ret.append(val)
            index=index+1
        return ret

class Dict (Trie):
    def __init__(self, fname):
        starttime = time.time()
        super (Dict, self).__init__()
        self.load(fname)
        endtime = time.time()
        print >> sys.stderr,"INIT--LOAD Dict Cost: [%.4f]" % (endtime - starttime)

    def load(self, fname):
        file = codecs.open(fname, 'r', 'gbk')
        for line in file:
            word = line.strip()
            self.add(word, word)
        file.close()

if __name__ == "__main__":
        dic = Dict("dic")

        for x in range(1):
            starttime = time.time()
            test_str = u"�����ú�·�������������С����񣱣��������������������������ȡ��ѣѣ��������������������ռ�ѡС�㡿������С����񣱣��������������������������ѣѣ��������������������ռ�ѡС�㡿������С����񣱣��������������������������ȡ��ѣѣ��������������������ռ俴��Ƭ�����������㳣ס���С��� ������С��������ȡ������������������������������ȡ����Ǹ��²������С���Щ������Ҫ����������С����񣱣�����������������������������Ϊ�������ڼ�į����ҹ�㲻�ڸе��µ��ͼ�į����"
            ret = dic.match_all(test_str)
            endtime = time.time()
            exe_time = (endtime - starttime)*1000
            print  "find forbidden %s  cost:%s" %(" ".join(ret).encode('gbk'),exe_time)
