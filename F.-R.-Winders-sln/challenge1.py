## As written in SageMathCell
## RSA Encryption Algorithm
n = Integer(197223219037565632376695983094276850131)
e = Integer(65537)
ciphertext = Integer(30481081274197412964612081780126987047)

factors = factor(n)
p = Integer(factors[0][0])
q = Integer(factors[1][0])
print(p)
print(q)

totient = (p - Integer(1)) * (q - Integer(1))

d = power_mod(e, -1, totient)
print(d)

plaintext = power_mod(ciphertext, d, n)
print(plaintext) 
