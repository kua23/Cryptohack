# 3 * d ≡ 1 mod 13
# We need to find out what d is 
# We can either do it using extended Euler's algorithm, which says:
# 13 = 3(4) + 1
# Thus, 1 = 13(1) - 3(4), which makes the inverse = 13-4 = 9
# Or we can use Fermat's little theorem, stating that a ^ (p-1) % p = 1
# Which means 3 * 3 ^ 11 mod 13 = 1
print(pow(3,11)%13)
