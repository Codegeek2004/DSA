def Recursion_print(n):
    if(n==0):
        return
    else:
        print(n)
        Recursion_print(n-1)
n=5
print(Recursion_print(n))