username_list = ['VoltFox99', 'CosmicKite', 'NeonRider', 'StarDrop', 'admin']
for username in username_list:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")
