 #1.
import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha1(password.encode("utf-8")).hexdigest()

def verify_password(password: str, stored_hash: str) -> bool:
    return hash_password(password) == stored_hash

# Example usage:
# stored = hash_password("secret123")
# verify_password("secret123", stored)

# Tasks for students:

# List at least three reasons this password storage approach is insecure.
# 1. SHA-1 is outdated and no longer considered secure. 2. There is no salt being used. 3. The cost of computing is to low to slow down brute-force attacks. 
# Explain what an attacker can do if they obtain the password hash database from this system.
#use a gpu to brute force thousands of hashes per second 
# Replace this design with a more secure scheme using a modern password hashing library (for example, bcrypt or argon2) and briefly describe:
import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt(rounds=12)
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(password, stored_hash):
    return bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8'))


# How salts are handled
#bcrypt automatically generates a unique salt for each password hash and stores it as part of the hash output.
# How “work factor” / cost makes attacks more expensive

#how work factor cost makes attacks more expensive
# The work factor (or cost) in bcrypt determines how many iterations of the hashing algorithm are performed. A higher cost increases the time required to compute the hash, making brute-force and dictionary attacks significantly more expensive and time-consuming for attackers.
# Link this to the relevant OWASP category and name one OWASP cheat sheet that would help improve this code.
# A02:2021 Cryptographic Failures
# Password Storage Cheat Sheet

#2.
import sqlite3
from getpass import getpass

def login():
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()

    username = input("Username: ")
    password = getpass("Password: ")

    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("DEBUG SQL:", query)  # left in by a developer

    cur.execute(query)
    row = cur.fetchone()

    if row:
        print("Login successful!")
    else:
        print("Invalid username or password.")

    conn.close()

if __name__ == "__main__":
    login()

#Tasks for students:

#Identify the vulnerability in how the SQL query is built.
# The vulnerability is SQL injection, the username and password are put into the query without sanitization or parameterization

#Rewrite the login code using parameterized queries to prevent this vulnerability.

import sqlite3
from getpass import getpass

def login():
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()

    username = input("Username: ")
    password = getpass("Password: ")

    # Use parameterized query with ? placeholders
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    
    cur.execute(query, (username, password))
    row = cur.fetchone()

    if row:
        print("Login successful!")
    else:
        print("Invalid username or password.")

    conn.close()

if __name__ == "__main__":
    login()

#Name the relevant OWASP Top 10 category and explain why this code is risky in a real application.
#A03:2021 Injection
#this code is risky because any SQL code can be injected into the username or password fields.

#3.
import requests

API_KEY = "sk_live_1234567890SECRET"
BASE_URL = "https://api.payment-provider.example/v1"

def charge_customer(customer_id, amount_cents):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {"customer": customer_id, "amount": amount_cents}
    response = requests.post(f"{BASE_URL}/charge", headers=headers, json=data)
    print("Status:", response.status_code)
    print("Response:", response.text)

if __name__ == "__main__":
    cid = input("Customer ID: ")
    amt = int(input("Amount (cents): "))
    charge_customer(cid, amt)

 

#Tasks for students:

#Explain why hardcoding API_KEY in the source code is a security problem.
# The API key is hardcoded meaning anyone with access to the source code can use it to call the API
 
#Describe what could happen if this repository is accidentally made public or sent to a contractor.
# Some could use the API key to make unauthorized transactions or access to sensitive data.

#Propose a more secure way to handle this API key in Python (hint: environment variables, config files, secret managers, etc.).
import requests
import os

# Load API key from environment variable
API_KEY = os.getenv("PAYMENT_API_KEY")
BASE_URL = "https://api.payment-provider.example/v1"

def charge_customer(customer_id, amount_cents):
    if not API_KEY:
        raise ValueError("API key not found. Set PAYMENT_API_KEY environment variable.")
    
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {"customer": customer_id, "amount": amount_cents}
    response = requests.post(f"{BASE_URL}/charge", headers=headers, json=data)
    print("Status:", response.status_code)
    print("Response:", response.text)

if __name__ == "__main__":
    cid = input("Customer ID: ")
    amt = int(input("Amount (cents): "))
    charge_customer(cid, amt)
#Name at least one OWASP category this falls under (e.g., Cryptographic Failures, Security Misconfiguration, Software and Data Integrity Failures) and explain briefly.
# A02:2021 Cryptographic Failures
# Hardcoding sensitive credentials like API keys in source code exposes them in plaintext. This violates the principle of protecting data at rest.