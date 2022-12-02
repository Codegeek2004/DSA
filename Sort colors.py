class Solution(object):
    def sortColors(self, n):
        for i in range(1, len(n)):
            k=n[i]
            j = i-1
            while j >= 0 and k< n[j] :
                n[j + 1] = n[j]
                j -= 1
            n[j + 1] = k
        return n