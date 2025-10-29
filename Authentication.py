# Authentication

#dictionary of users where the key is the username and the value is the role
users={
    "darrick" : "admin",
    "buddy"  : "user",
    "test" : "user",
}

#login function
def login(username):
    if username in users:
        print(f"Login successful. Role: {users[username]}")
    else:
        print("Login failed. Username not found.")

#function for admin use only
def admin_only(role):
    if role == "admin":
        def delete_user(username):
            if username in users:
                del users[username]
                print(f"{username} deleted.")
    else:
        print("Access denied: Admins only.")
            
#function for user only
def user_only(role, current_username, new_username):
    if role == "user":
        if current_username in users and users[current_username] == "user":
            users[new_username] = users.pop(current_username)
            print(f"Username updated to {new_username}.")
        else:
            print("Access denied: You can only update your own username.")
    else:
        print("Access denied: Users only.")
    
# This app shows the confidentiality in the CIA triad. It does this by restricting certain functions to predetermined roles.
# Only the admin will be able to delete users, while only the logged in user will be able to update thier username only.
# If an unauthorized user tries to access these functions, they will be denied access and shown an error message.
# This checks for authentication as well as authorization before allowing access to sensitive functions.
