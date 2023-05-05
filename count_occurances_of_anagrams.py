#User function Template for python3
class Solution:

    
    def search(self,pat, txt):
        freq = [0] * 26
        freqOfPat = [0] * 26
        for i in range(len(pat)):
            freqOfPat[ord(pat[i]) - 97] += 1
        start, end, occurrence = 0, 0, 0
        temp = []
        while end < len(txt):
            temp.append(txt[end])
            freq[ord(txt[end]) - 97] += 1
            if end - start + 1 == len(pat):
                if freq == freqOfPat:
                    occurrence += 1
                freq[ord(temp[0]) - 97] -= 1
                temp.pop(0)
                start += 1
            end += 1
        return occurrence

        
        
'''  Time Complexity: O(n)'''