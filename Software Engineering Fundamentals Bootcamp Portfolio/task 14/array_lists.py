"""
This program shows methods of sorting and searching lists in python
using albums as an example. It uses the built-in method sort() and a binary
search function to achieve this.
"""


# Create a class with attributes for album name, artist and number of songs
class Album:

    def __init__(self, album_name, artist, num_of_songs):
        self.album_name = str(album_name)
        self.artist = str(artist)
        self.num_of_songs = int(num_of_songs)

    def __str__(self):
        return f"{self.album_name} - {self.artist} - {self.num_of_songs}"


# Create first list of albums
albums1 = [Album("Miracle Milk", "Mili", 17),
           Album("Millennium Mother", "Mili", 19),
           Album("Rise of the Monarch", "AmaLee", 8),
           Album("If you don't like the story, write your own", "Witt Lowry", 16),
           Album("Criminal Idol", "Static-P", 13)]

print("Albums 1 list as created")
# Iterate through the list and print each element
for obj in albums1:
    print(obj)

# Sort the first album list by the number of songs on the albums
albums1.sort(key=lambda album: album.num_of_songs)

print("\nAlbums 1 list sorted by number of songs: \n")
for obj in albums1:
    print(obj)

# Swap album in index 0 with album in index 1
albums1[0], albums1[1] = albums1[1], albums1[0]


print("\nAlbums 1 list with first 2 entries swapped: \n")
for obj in albums1:
    print(obj)

# Create second list of albums
albums2 = [Album("Hybrid Theory", "Linkin Park", 12),
           Album("Melodies for the Outsiders", "Burn the Ballroom", 6),
           Album("Don't judge a band by its covers", "Area 11", 5),
           Album("End Credits", "EDEN", 7),
           Album("Twilight Theatre", "Poets of the Fall", 10)]

print("\nAlbums 2 list as created: \n")
for obj in albums2:
    print(obj)

# Merge first album list into second album list
albums2 = albums1 + albums2

print("\nAlbums 2 list merged with Albums 1 list: \n")
for obj in albums2:
    print(obj)

# Add 2 new albums to the second album list
albums2.append(Album("Dark Side of the Moon", "Pink Floyd", 9))
albums2.append(Album("Oops!.. I Did it Again", "Britney Spears", 16))

# Sort the second album list after merging and adding addition albums
albums2.sort(key=lambda album: album.album_name)


print("\nAlbums 2 list sorted by alphabetical album name: \n")
for obj in albums2:
    print(obj)


# Binary Search function, with a complexity of O(log n)
def binary_search(arr, search):
    # Set the index search range with low and high
    low = 0
    high = len(albums2) - 1
    while low <= high:
        mid = (low + high) // 2  # Floor Division divides by 2 and rounds down to nearest whole number
        current = arr[mid].album_name  # The current value is the central index, and reads the album name
        if current == search:
            return mid
        elif current > search:
            # Because the list is sorted, if the first found letter is greater than the search parameter,
            # we know we have to search lower into the list
            high = mid - 1
        else:
            # If the first letter found is lower than the search parameter,
            # we know we have to search higher in the list
            low = mid + 1
    return -1


search_album = binary_search(albums2, "Dark Side of the Moon")
if search_album:
    print(f"\nDark Side of the Moon can be found at index {search_album}")
else:
    print("\nAlbum not found")
