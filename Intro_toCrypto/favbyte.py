code = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d") #Convert the hexadecimal to bytes
print(code)
i = 0

while i <= 255: # As there are 256 different byte possibilities
    flag = ""
    for x in code: #Here, each value of x is an integer, as when you iterate through a bytestring, it returns the integer value of each byte
        flag += chr(x ^ i) #Here, the code is XORed with each of the 256 possible values of the byte.
    i += 1
    if "crypto" in flag: 
        print(flag)


    
