# Reuses and slightly modifies exercise [5-08]

username_list = []
if username_list:
    for username in username_list:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
        print("We need some more users!")
