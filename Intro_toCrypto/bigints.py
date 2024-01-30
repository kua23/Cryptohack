from Crypto.Util.number import * # PyCryptoDome library
flag = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
# The long format created by concatenating many hexadecimal values of ASCII togther can be converted into bytes using the long_to_bytes function

print(long_to_bytes(flag).decode()) # converts byte to string

''' Flag
    crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}'''
