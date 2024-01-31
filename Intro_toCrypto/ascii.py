code = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
flag = ""
for x in code:
    flag = flag + chr(x) #chr is a function used to convert decimal values into their corresponding ASCII 
print(flag)