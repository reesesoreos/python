# Reuses exercise [9-03]

class User:
    def __init__(
            self, first_name, last_name, language_preference, display_name
            ):
        self.first_name = first_name
        self.last_name = last_name
        self.language_preference = language_preference
        self.display_name = display_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"This user's first name is {self.first_name.title()}.")
        print(f"This user's last name is {self.last_name.title()}.")
        print(f"This user's language preference is {self.language_preference.title()}.")
        print(f"This user's display name is {self.display_name}.")
    
    def greet_user(self):
        print(f"Hello {self.first_name.title()}, welcome to the platform.")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User('alex', 'smith', 'english', 'AlexS')
user2 = User('maria', 'garcia', 'spanish', 'MGarcia')
user3 = User('kenji', 'sato', 'japanese', 'KenjiS')

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)