code = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104") #Convert the hexadecimal to bytes
i = 0
len_code = len(code)
strflag = b""
flagformat = b"myXORkey"
lenflag = len(flagformat) 
for i in range (0, len_code): 
    flag = flagformat[i%lenflag] ^ code[i] # We use i % lenflag as the code is repeatedyl XORed with the key/flag, thuse once the entire length finishes it iterates back to the original length 
    strflag += flag.to_bytes(1, "big")
print(strflag)

#We first use the key as crypto{ to get an idea of what the key might be. It return myXORkey, which is the reeason why we then use myXORkey as the key

#Flag
    #crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}
