import math
i= int(input())
# print(round(math.log(i)/math.log(2)))
if (round(math.log(i)/math.log(2))%2==0):
    print("True")
else:
    print("False")