In order to convert a long string of numbers created by the concatenation of the hexadecimal values of ASCII symbols, the `long_to_bytes()` method can be used to do so. This method can be accessed 
from the PyCryptoDome library and can by imported using `from Crypto.Util.number import *`.

Thus, 
`
from Crypto.Util.number import *
flag = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
print(long_to_bytes(flag))

`

### Flag
`crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}`
