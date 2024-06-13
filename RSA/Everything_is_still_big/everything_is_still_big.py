from Crypto.Util.number import *
from factordb.factordb import FactorDB
from sympy import *
from math import isqrt
N = "b12746657c720a434861e9a4828b3c89a6b8d4a1bd921054e48d47124dbcc9cfcdcc39261c5e93817c167db818081613f57729e0039875c72a5ae1f0bc5ef7c933880c2ad528adbc9b1430003a491e460917b34c4590977df47772fab1ee0ab251f94065ab3004893fe1b2958008848b0124f22c4e75f60ed3889fb62e5ef4dcc247a3d6e23072641e62566cd96ee8114b227b8f498f9a578fc6f687d07acdbb523b6029c5bbeecd5efaf4c4d35304e5e6b5b95db0e89299529eb953f52ca3247d4cd03a15939e7d638b168fd00a1cb5b0cc5c2cc98175c1ad0b959c2ab2f17f917c0ccee8c3fe589b4cb441e817f75e575fc96a4fe7bfea897f57692b050d2b"
E = "9d0637faa46281b533e83cc37e1cf5626bd33f712cc1948622f10ec26f766fb37b9cd6c7a6e4b2c03bce0dd70d5a3a28b6b0c941d8792bc6a870568790ebcd30f40277af59e0fd3141e272c48f8e33592965997c7d93006c27bf3a2b8fb71831dfa939c0ba2c7569dd1b660efc6c8966e674fbe6e051811d92a802c789d895f356ceec9722d5a7b617d21b8aa42dd6a45de721953939a5a81b8dffc9490acd4f60b0c0475883ff7e2ab50b39b2deeedaefefffc52ae2e03f72756d9b4f7b6bd85b1a6764b31312bc375a2298b78b0263d492205d2a5aa7a227abaf41ab4ea8ce0e75728a5177fe90ace36fdc5dba53317bbf90e60a6f2311bb333bf55ba3245f"
C = "a3bce6e2e677d7855a1a7819eb1879779d1e1eefa21a1a6e205c8b46fdc020a2487fdd07dbae99274204fadda2ba69af73627bdddcb2c403118f507bca03cb0bad7a8cd03f70defc31fa904d71230aab98a10e155bf207da1b1cac1503f48cab3758024cc6e62afe99767e9e4c151b75f60d8f7989c152fdf4ff4b95ceed9a7065f38c68dee4dd0da503650d3246d463f504b36e1d6fafabb35d2390ecf0419b2bb67c4c647fb38511b34eb494d9289c872203fa70f4084d2fa2367a63a8881b74cc38730ad7584328de6a7d92e4ca18098a15119baee91237cea24975bdfc19bdbce7c1559899a88125935584cd37c8dd31f3f2b4517eefae84e7e588344fa5"
n = int(N,16)
e = int(E,16)
c = int(C,16)
def continued_fraction_terms(n, d):
    terms = []
    while d:
        terms.append(n // d)
        n, d = d, n % d
    return terms

# Function to compute convergents from continued fraction terms
def convergents_from_cf(cf):
    n0, n1 = cf[0], cf[0] * cf[1] + 1
    d0, d1 = 1, cf[1]
    yield n0, d0
    yield n1, d1
    for i in range(2, len(cf)):
        n2 = cf[i] * n1 + n0
        d2 = cf[i] * d1 + d0
        yield n2, d2
        n0, n1 = n1, n2
        d0, d1 = d1, d2

# Function to perform Wiener's attack
def wiener_attack(e, n):
    cf = continued_fraction_terms(e, n)
    for k, d in convergents_from_cf(cf):
        if k == 0:
            continue
        # Check if d is the correct private key
        phi = (e * d - 1) // k
        s = n - phi + 1
        discr = s * s - 4 * n
        if discr >= 0:
            t = isqrt(discr)
            if t * t == discr:
                p = (s + t) // 2
                q = (s - t) // 2
                if p * q == n:
                    return d
    return None

# Perform Wiener's attack
d = wiener_attack(e, n)
if d is None:
    print("Failed to find the private key using Wiener's attack.")
else:
    print(f"Found private key d: {d}")
    # Decrypt the message
    m = pow(c, d, n)
    message = long_to_bytes(m)
    try:
        print(f"Decrypted message: {message.decode()}")
    except UnicodeDecodeError:
        print(f"Decrypted message (bytes): {message}")