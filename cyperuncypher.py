import math
#pick 2 prime numbers p and q

p=3
q=7
m = 10 #message to be encrypted
n=p*q
totient = (p-1) * (q-1)

for i in range (2, totient):
    if math.gcd(i,totient) ==1:
        e = i
        break
    
#encrypting the message before displaying public keys

c = m**e % n

print(f"Public Keys:({e}, {n})")
print(f"Cypher Text: {c}")

#finding d which is any number that when you multiply by e and mod totient gives 1

for j in range(1,100):
    if (j * e) % totient ==1:
        d = j
        break
print(f"D is: {d}")

plaintext = c**d % n
print(f"Plain Text: {plaintext}")