import sqlite3



conn = sqlite3.connect("users.db")

cur = conn.cursor()



cur.execute("""

CREATE TABLE IF NOT EXISTS users (

        id INTEGER PRIMARY KEY,

        username TEXT,

        password TEXT

    )

    """)



cur.execute("INSERT INTO users (username, password) VALUES ('admin', 'password123')")

conn.commit()




print("Database ready.")



# writing the login feature function

username = input("Enter Username: ")

password = input("Enter password: ")



query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

cur.execute(query)

result = cur.fetchone()

if result:

    print("User exists")

else:

    print("User does not exist")

    

conn.close()