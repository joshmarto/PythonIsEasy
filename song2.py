song = {
    "Title": "Back in the Day & So Good",
    "Album": "Live from the Inside",
    "Artist": "Brian Culbertson",
    "Year": 2009,
    "Genre": "Jazz",
    "Lyrics": True,
    "Platforms": ["Spotify", "iCloud", "Youtube Music", "Deezer", "Play Music"],
    "Author": "Brian Culbertson",
    "Prizes": 4,
    "Track": 10,
}

for key in song.keys():
    if len(key) > 5:
        print(f"{key}: \t{song[key]}")
    else:
        print(f"{key}: \t\t{song[key]}")


print("Extra function")
def letMeGuess(key, value):
    if key in song.keys() and value in song.values():
        if value == song[key]:
            return True
        else:
            return False
# Example of success
print(letMeGuess("Lyrics", True))
# Example of fail
print(letMeGuess("Prizes", 10))
