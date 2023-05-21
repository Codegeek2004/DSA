def Array(arr,i):
    if (i==len(arr)):
        return 
    print(arr[i])
    Array(arr,i+1)
arr=[5,9,4,1,3,7]
i=0
print(Array(arr,i))