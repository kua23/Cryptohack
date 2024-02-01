#This is based on Fermat's little theorem. 
#It states that if p is a prime number, a^p % p = a
# Also states that, if a^(p-1) % p = 1

a = 273246787654
b = 65536
p = 65537   
mod = 0
if b == p:
    mod = a
elif b == p-1:
    mod = 1
else:
    print("oops")
print(mod)