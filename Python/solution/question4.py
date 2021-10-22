print("Perfect Square Question 4")
i= int(input())
x=0
div=1
flag=0
while(div*div<=i):
    if div*div == i:
        print("True")
        flag = 1
        break
    div+=1
if flag == 0:
    print("False")   
