# Reuses exercise [8-07]

def make_album(artist_name, album_title, song_number=None):
    album = {
        'artist': artist_name.title(),
        'title': album_title.title()
    }
    if song_number:
        album['song_number'] = song_number
    return album

print(make_album('michael jackson', 'thriller'))
print(make_album('ac/dc', 'back in black'))
print(make_album('eagles', 'hotel california', 9))

while True:
    artist_name = input("" 
    "Please enter a music artist. Type q to quit at any time.")
    if artist_name == 'q':
        break
    
    album_title = input("Please enter an album made by that artist.")
    if album_title == 'q':
        break
    else:
        print(make_album(artist_name, album_title))

