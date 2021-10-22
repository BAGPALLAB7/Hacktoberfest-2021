def recursion(n):
    if n<10:
        print(n)
    else:
        s=0
        while (n!=0):
            s+= n%10
            n//=10
        recursion(s)

i= int(input())
recursion(i)