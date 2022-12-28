def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def nearestPrime(num):
    x = num
    y = num

    while not isPrime(x):
        x -= 1
        continue
    diff1 = num-x
    while not isPrime(y):
        y += 1
        continue
    diff2 = y-num

    if(diff1 <= diff2):
        return x
    return y

def gcd(a, b):
    if b == 0:
        return a
    return (gcd(b, a%b))

def relativePrime(phi, p, q):
    for e in range(2, phi):
        if(e != p and e != q):
            if(gcd(phi, e) == 1):
                return e

def extEuclidean(phi, e):
    a = [1, 0]
    b = [0, 1]
    d = [phi, e]
    k = [None, phi // e]

    while(d[-1] != 1):
        a.append(a[-2] - a[-1] * k[-1])
        b.append(b[-2] - b[-1] * k[-1])
        d.append(d[-2] - d[-1] * k[-1])
        k.append(d[-2] // d[-1])

    if(d[-1] == 1):
        if(b[-1] < 0):
            return (b[-1] + phi)
        return b[-1]

def encryption(pt, e, n):
  ct = (pt)**e % n
  return ct

def decryption(ct, d, n):
  pt = (ct)**d % n
  return pt


def RSA(str1, str2, pt):
    # Step1
    p = nearestPrime(len(str1))
    q = nearestPrime(len(str2))
    # Step2
    n = p * q
    # Step3
    phi = (p-1) * (q-1)
    # Step4
    e = relativePrime(phi, p, q)
    print(e)
    # Step5
    d = extEuclidean(phi, e)
    print(d)
    # Step6
    ct = encryption(pt, e, n)
    print(ct)
    # Step7
    pt = decryption(ct, d, n)
    print(pt)

str1 = "abcdefg"
str2 = "abcdefghijk"
pt = 24
RSA(str1, str2, pt)