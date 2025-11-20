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
print(key) 