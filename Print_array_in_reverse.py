def Reverse_Array(arr,i):
    if i==len(arr):
        return
    Reverse_Array(arr,i+1)
    print(arr[i])
arr=[2,3,6,7,8,1]
i=0
print(Reverse_Array(arr,i))