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