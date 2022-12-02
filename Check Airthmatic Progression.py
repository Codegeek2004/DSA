class Solution:
    
    def checkIsAP(self, arr, n):
        arr.sort()
        k=0
        d=arr[1]-arr[0]
        for i in range(0,len(arr)-1):
            if((arr[i+1]-arr[i])==d):
                k+=1

        if(k==(n-1)):
            return True
        else:
            return False
    
        # code here
        
    
