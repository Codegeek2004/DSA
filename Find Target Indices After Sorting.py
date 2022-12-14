class Solution(object):
    def targetIndices(self, n, t):
        k=[]
        n.sort()
        for i in range(len(n)):
            if (n[i]==t):
                k.append(i)
        return k