t = int(input("Number of Inputs: "))
for i in range(t):
    n  = int(input("Input: "))
    x=n
    if n<0:
        n= 0-n
    s=0
    while(n!=0):
        s = (s*10)+(n%10)
        n//=10 
    if x<0:
        print("Output: ", (0-s))
    else:
        print("Output: ", s)
    