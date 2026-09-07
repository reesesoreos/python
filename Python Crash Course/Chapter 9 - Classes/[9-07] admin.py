# Reuses exercise [9-03]

class User:
    def __init__(
            self, first_name, last_name, language_preference, display_name
            ):
        self.first_name = first_name
        self.last_name = last_name
        self.language_preference = language_preference
        self.display_name = display_name

    def describe_user(self):
        print(f"This user's first name is {self.first_name.title()}.")
        print(f"This user's last name is {self.last_name.title()}.")
        print(f"This user's language preference is {self.language_preference.title()}.")
        print(f"This user's display name is {self.display_name}.")
    
    def greet_user(self):
        print(f"Hello {self.first_name.title()}, welcome to the platform.")

class Admin(User):
    def __init__(self, first_name, last_name, language_preference, display_name):
        super().__init__(first_name, last_name, language_preference, display_name)
        self.privileges = ['delete users', 'ban users', 'delete posts']

    
    def show_privileges(self):
        for privilege in self.privileges:
            print(f"The admin can {privilege}.")


admin = Admin('alex', 'smith', 'english', 'AlexS',)
admin.show_privileges()