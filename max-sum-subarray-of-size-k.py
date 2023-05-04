#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        wend=0
        wstart=0
        s=0
        ans=0
        while(wend<len(Arr)):
            s+=Arr[wend]
            if((wend-wstart+1)==K):
                ans=max(ans,s)
                s-=Arr[wstart]
                wstart+=1
            wend+=1
        return ans
'''Time Complexity: O(n)'''