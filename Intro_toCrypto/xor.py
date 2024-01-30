
''' from pwn import *
from Crypto.Util.number import *
word = "label"
integer = 13
flag = xor(word, integer)
print(flag) '''

word = "label"
flag = ""
for x in word:
    flag += chr((ord(x)^13)) #Here, XORing is done by first converting the string to its ASCII, and then XORing the ASCII with the number 13. This is then converted back to a string at the end
print(flag)

''' Flag
    crypto{Aloha} '''


