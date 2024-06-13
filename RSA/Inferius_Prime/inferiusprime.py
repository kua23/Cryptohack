from factordb.factordb import FactorDB
from Crypto.Util.number import *
n = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373
f = FactorDB(n)
f.connect()
factors = f.get_factor_list()
print(factors)
p = factors[0]
q = factors[1]
phi_n = (p-1) * (q-1)
d = inverse(e,phi_n)
m = pow(ct,d,n)
print(m)
print(long_to_bytes(m))

