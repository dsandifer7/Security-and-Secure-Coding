import hashlib

def sha_hashing(string):
    encoded_string = string.encode("utf-8")
    hashed_string = hashlib.sha256()
    hashed_string.update(encoded_string)
    return(hashed_string.hexdigest())
string = "Hello, World!"
print(sha_hashing(string))