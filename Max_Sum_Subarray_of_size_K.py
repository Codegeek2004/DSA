#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        ans=0
        for i in range(N-K+1):
            s=0
            for j in range(i,i+K):
                s+=Arr[j]
            ans=max(ans,s)
        return ans
    ''' 
    Repetitive part:
        for j in range(i,i+K):
            s+=Arr[j]
            
    Time complexity: O(n*K)
    
    '''