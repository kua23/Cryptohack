Here, we need to XOR the word `label` with the integer `13`. So, we need to first convert each letter of the word to its ordinal, XOR it with the integer and then convert it back to ASCII.

`word = "label"
flag = ""
for x in word:
    flag += chr((ord(x)^13))
print(flag)`
 This is what the code also does.
`^` operator is used to perform XOR operation.

### Flag
`crypto{aloha}`
