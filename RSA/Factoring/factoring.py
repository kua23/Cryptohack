from factordb.factordb import FactorDB
n = 510143758735509025530880200653196460532653147
k = FactorDB(n)
k.connect()
l = k.get_factor_list()
if l[0] < l[1]:
    print(l[0])
else:
    print(l[1])