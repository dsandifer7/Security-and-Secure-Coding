import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256


message = "Hello"
# must have a password to begin AES encryption
password = "password"

# generate a salt as a random number or string in bytes third import line


# derive a key from the password and salt using PBKDF2 
# PBDKF2 takes these parameters:
    # password (encoded)
    # salt (in bytes)
    # length dkLen ( how long you want the key to be, 16 bytes for AES-128 and 32 bytes for AES-256)
    # count ( number of times you want to hash it)
    # hmac_hash_module (hashing algorithm to use)

password_bytes = password.encode('utf-8')
salt = get_random_bytes(16)
dkLen = 32 # AES-256
count = 100000
hmac_hash_module = SHA256

key = PBKDF2(password_bytes, salt, dkLen=32, count=100000, hmac_hash_module=SHA256)
# print(key) 

# to encrypt we need to use a specific AES MODE 
# create a new AES cipher in GCM mode

cipher = AES.new(key, AES.MODE_GCM)
encrypted_message, tag = cipher.encrypt_and_digest(message.encode('utf-8'))
nonce = cipher.nonce # get the nonce from the cipher object number used once nonce
#print(encrypted_message)

# to decrypt the message we need the key, tag, nonce, encrypted message, and salt
decrypt = AES.new(key, AES.MODE_GCM, nonce=nonce)
decrypted_message = decrypt.decrypt_and_verify(encrypted_message, tag)
print(decrypted_message.decode('utf-8'))