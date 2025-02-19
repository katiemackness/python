# Katie Mackness
# 24/06/2024 - Updated 19/02/2025

# ---------------------------------------------------------
# Command Line Function - Add Album Information
# ---------------------------------------------------------

def make_album(artist, album_name, number_of_songs=None):
    """Create a dictionary with album information"""
    album_info = {'artist': artist, 'album': album_name}
    if number_of_songs:
        album_info['number_of_songs'] = number_of_songs
    return album_info

# Add a new album to the dictionary
album = make_album("Jimminy Crickets", "The Jiminy Show", 45)
# View new album
print(album)
# Add a new album to the dictionary
album2 = make_album("Friggin' Dylan", "Frig that Frig")
# View new album
print(album2)

# Command line loop to add new alums to the dictionary
while True:
    print("Please enter the album information.")
    print("Press 'q' at any time to quit.")

    artist_name = input("Artist: ")
    if artist_name == 'q':
        break
    album_name = input("Album: ")
    if artist_name == 'q':
        break
    songs = input("# of songs on the album (optional): ")
    if songs == 'q':
        break

    album_info = make_album(artist_name, album_name, songs)

    # View new album
    print("\nNew Album Added:")
    print(album_info)