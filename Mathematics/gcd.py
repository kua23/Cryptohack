#This is based on Euclidean's algorithm which states that in order to find the GCD between the two numbers, subtract the larger number
#from the smaller number and keep doing so until botht the numbers are equal which gives the GCD
#example: 252, 105 ==> 252 - 105 = 147 ==> 147 - 105 = 42 ==> 105 - 42 = 63 ==> 63 - 42 = 21 ==> 42 - 21 = 21 which gives the answer as 21

num1 = 66528
num2 = 52920
temp = 0
if num2 > num1:
    num1, num2 = num2, num1
while num1 != num2:
    temp = num1 - num2
    num1 = temp
    if (num2>num1):
        num2, num1 = num1, num2
print(num1)