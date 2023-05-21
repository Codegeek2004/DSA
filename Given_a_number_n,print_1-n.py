def Recursion_print(n):
    if(n==0):
        return
    else:
        Recursion_print(n-1)
        print(n)
n=6
print(Recursion_print(n))