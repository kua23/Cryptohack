Base64 is used to represent ASCII characters in 64 different ways. This can also be done using Python and Linux.

In Python, we can use
`import base64 ` <br>
`flag = str(input("Enter the flag"))  ` <br> 
`hexflag = bytes.fromhex(flag) ` <br> 
`b64flag = base64.b64encode(hexflag)` <br>  
`print(b64flag) ` <br>
First, decoding it from hex and then encoding it in base64, where base64 is a library.

In Linux, we just use the command base64
`echo 72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf | xxd -r -p | base64`
which then returns the answer

### Flag
`crypto/Base+64+Encoding+is+Web+Safe/`

