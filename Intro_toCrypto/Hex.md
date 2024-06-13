The flag is encoded as a hex string.
`63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d`

In order to decode this, we can either use Python or the Linux terminal.

### For Python

`choice = str(input("Enter hex or bytes to get the output in that form: "))` <br>
`flag = str(input("Enter the string: "))` <br>
`if choice == "bytes": `<br>
    `print(bytes.fromhex(flag)) `<br>
`elif choice == "hex": `<br>
   ` print(flag.hex()) `<br>
`else: `<br>
   ` print("Invalid user input")` <br>
    
The `bytes.fromhex()` function converts hex to bytes, while `.hex()` method converts bytes to hex

### For Linux
In order to convert hex to ASCII, we can use `-xxd` in order to do so.
Using
`echo 63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d | xxd -r -p`
Here `-r` is used to convert it from ASCII to text and the `-p` is used to print the output

### Flag
`crypto{You_will_be_working_with_hex_strings_a_lot} `
