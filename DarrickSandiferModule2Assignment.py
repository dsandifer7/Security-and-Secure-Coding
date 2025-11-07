#RSA asymmetric encryption and decryption
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


#Caesar Cipher encryption and decryption

alphabets = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:\'",.<>?/`~ '
message= 'surprise!'
shift = 14
encryptedmessage = ''

#checks each letter in the message to see if it is in the alphabet
for i in message:
    if i in alphabets:
        plaintext = alphabets.index(i)  #finds the position of the letter in the alphabet
        encrypt = (plaintext + shift) % 73  #shifts the letter by the specified amount the modulo 73 makes sure that the position wraps around the alphabet  if the position is would be greater than 72
        encryptedmessage += alphabets[encrypt]
    else:
        encryptedmessage += i  #if the character is not in the alphabet (like a space or punctuation) it is added unchanged

#decryption 
decryptedmessage = ''
for i in encryptedmessage:
    if i in alphabets:
        encrypted = alphabets.index(i)
        decrypt = (encrypted - shift) % 73  #the same as encryption but subtracting the shift instead of adding it
        decryptedmessage += alphabets[decrypt]
    else:
        decryptedmessage += i

print(f'Original message: {message}')
print(f'Encrypted message: {encryptedmessage}')
print(f'Decrypted message: {decryptedmessage}')