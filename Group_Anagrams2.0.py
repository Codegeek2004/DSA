import collections
class Solution(object):
    def groupAnagrams(self, li):
        l=[]
        l=[]
        for i in li:
            l.append(i)
        for i in range(len(l)):
            l[i]=''.join(sorted(l[i]))
        o=list(collections.Counter(l).keys())
        d={}
        for i in range(len(o)):
            d[i]=[]
        d=dict(zip(o,list(d.values())))
        for i in range(len(li)):
            r=''.join(sorted(li[i]))
            if r in d:
                d[r].append(li[i])
        k=[]
        for i in d:
            k.append(d[i])
        return k
            