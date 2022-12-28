def DHA(p, g, a, b):
  x_a = (g**a) % p
  x_b = (g**b) % p
  a_k = (x_b**a) % p
  b_k = (x_a**b) % p
  return(a_k == b_k)

p = 23
g = 5
a = 4
b = 3
print(DHA(p, g, a, b))