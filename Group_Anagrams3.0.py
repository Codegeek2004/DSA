import collections
class Solution(object):
    def groupAnagrams(self, li):
        d={}
        for i in li:
            f=[0]*26
            for j in i:
                f[ord(j)-97]+=1
            f=tuple(f)
            if f in d:
                d[f].append(i)
            else:
                d[f]=[i]
        res=[]
        for k in d:
            res.append(d[k])
        return res
        
            