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