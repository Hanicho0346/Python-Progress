import hashlib
import json
import os


class User:
    def __init__(self, username, password_hash, is_logged_in=False, login_attempts=0):
        self.username = username
        self._password_hash = password_hash
        self.is_logged_in = is_logged_in
        self.login_attempts = login_attempts

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password):
        return self._password_hash == self.hash_password(password)

    def reset_login_attempts(self):
        self.login_attempts = 0

    def to_dict(self):
        return {
            "username": self.username,
            "password_hash": self._password_hash,
            "is_logged_in": self.is_logged_in,
            "login_attempts": self.login_attempts
        }


class AuthSystem:
    MAX_LOGIN_ATTEMPTS = 3
    FILE_NAME = "users.json"

    def __init__(self):
        self.users = {}
        self.load_users()


    def save_users(self):
        try:
            with open(self.FILE_NAME, "w") as file:
                json.dump(
                    {username: user.to_dict() for username, user in self.users.items()},
                    file,
                    indent=4
                )
        except Exception as e:
            print("Error saving users:", e)

    def load_users(self):
        if not os.path.exists(self.FILE_NAME):
            return

        try:
            with open(self.FILE_NAME, "r") as file:
                data = json.load(file)
                for username, user_data in data.items():
                    self.users[username] = User(
                        username=user_data["username"],
                        password_hash=user_data["password_hash"],
                        is_logged_in=user_data["is_logged_in"],
                        login_attempts=user_data["login_attempts"]
                    )
        except Exception as e:
            print("Error loading users:", e)


    def register(self, username, password):
        try:
            if username in self.users:
                return "Username already exists"

            if len(password) < 6:
                return "Password must be at least 6 characters long"

            password_hash = User.hash_password(password)
            self.users[username] = User(username, password_hash)
            self.save_users()
            return "User registered successfully"

        except Exception as e:
            return f"Registration error: {e}"

    def login(self, username, password):
        try:
            user = self.users.get(username)
            if not user:
                return "User not found"

            if user.login_attempts >= self.MAX_LOGIN_ATTEMPTS:
                return "Account locked due to too many failed login attempts"

            if user.verify_password(password):
                user.is_logged_in = True
                user.reset_login_attempts()
                self.save_users()
                return "Login successful"
            else:
                user.login_attempts += 1
                self.save_users()
                remaining = self.MAX_LOGIN_ATTEMPTS - user.login_attempts
                return (
                    f"Invalid password. {remaining} attempts remaining"
                    if remaining > 0
                    else "Account locked due to too many failed login attempts"
                )

        except Exception as e:
            return f"Login error: {e}"

    def logout(self, username):
        try:
            user = self.users.get(username)
            if user and user.is_logged_in:
                user.is_logged_in = False
                self.save_users()
                return "Logout successful"
            return "User not logged in"
        except Exception as e:
            return f"Logout error: {e}"

    def total_users(self):
        return len(self.users)

auth_system = AuthSystem()

def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Logout")
        print("4. Total Users")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(auth_system.register(username, password))

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(auth_system.login(username, password))

        elif choice == "3":
            username = input("Enter username: ")
            print(auth_system.logout(username))

        elif choice == "4":
            print(f"Total users: {auth_system.total_users()}")

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
