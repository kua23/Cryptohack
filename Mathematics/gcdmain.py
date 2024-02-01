#This is applying the actual Euclidean algorithm, which states that in the expression a = bq + r, GCD(a,b) = GCD(b,r)
#In the first step, a = bq + r, in the second step, a becomes b and b becomes r.
#This continues till r = 0, which means b = 0 

num1 = 57
num2 = 81
if num2 > num1:
    num1, num2 = num2, num1
while num1 != num2 & num2 !=0:
    r = num1 % num2
    num1 = num2
    num2 = r
    if(num2 == 0):
        break
print(num1)