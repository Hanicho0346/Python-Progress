# Question 1: Write a function that takes a username, email, and password as input and validates them based on the following criteria:
def validate_user(username, email, password):
    if len(username) < 4:
        return " Username too short."
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if "@" not in email:
        return "Email must contain '@' symbol."
    return "Valid"

print(validate_user("hana", "hana@example.com", "mypassword"))