current_users = ['VoltFox99', 'CosmicKite', 'NeonRider', 'StarDrop', 'PixelPulsar']
new_users = ['NeonRider', 'StarDrop', 'RetroViper', 'ShadowCombo', 'PhantomPixel']

current_users_lower = []
for username in current_users:
     current_users_lower.append(username.lower())

if new_users:
    for username in new_users:
        if username.lower() in current_users_lower:
                print(f"{username}, you will need to enter a new username.")
        else:
             print(f"{username}, this username is available.")
            