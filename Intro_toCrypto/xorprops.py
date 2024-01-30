key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313" 
key2_1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2_3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_1_3_2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
bkey1 = bytes.fromhex(key1) #Converts the key1 from hexadecimal to its corresponding bytes form
bkey2_1 = bytes.fromhex(key2_1)
bkey2_3 = bytes.fromhex(key2_3) 
bflag_1_3_2 = bytes.fromhex(flag_1_3_2) 
# Bytes is readable by the machine directly while strings have to be encoded in order to be read
key2 = b"" # This is a byte string 
key3 = b""
for i in range(0,26):
    x = bkey1[i] ^ bkey2_1[i] #XORs each byte of the key1 with the XORed key1 and key2
    y = x.to_bytes(1,"big") # As the XOR operation returns an int data type, converts the int back into bytes data type
    key2 += y # appends it back into the key
for i in range(0,26):
    x = bkey2_3[i] ^ key2[i]
    y = x.to_bytes(1,"big")
    key3 += y
flag = b""
for i in range(0,26):
    x = bflag_1_3_2[i] ^ key2[i] ^ bkey1[i] ^ key3[i]
    y = x.to_bytes(1,"big")
    flag += y
print(flag.decode())

''' Flag
crypto{x0r_i5_ass0c1at1v3} '''




