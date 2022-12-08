class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  
        l = defaultdict(list)
        
        for i in strs:
            key = ''.join(sorted(i))
            print(key)
            l[key].append(i)
            print(l[key])
        p = []
        
        for k in l:
            p.append(l[k])
        return p