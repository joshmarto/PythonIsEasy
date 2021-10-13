"""Set up of variables"""
title = "Back in the Day & So Good"
album = "Live from the Inside"
artist = "Brian Culbertson"
year = 2009
genre = "Jazz"
lyrics = True
platforms = ["Spotify", "iCloud", "Youtube Music", "Deezer", "Play Music"]
author = "Brian Culbertson"
prizes = 4
track = 10

"""Definition of functions"""
def Title():
    print("Title: " + title)
def Album():
    print("Album: " + album)
def Artist():
    print("Artist: " + artist)
def Year():
    print("Year: " + str(year))
def Genre():
    print("Genre: " + genre)
def Lyrics():
    print("Lyrics: " + str(lyrics))
def Platforms():
    print("Platforms: " + str(platforms))
def Author():
    print("Author: " + author)
def Prizes():
    print("Prizes: " + str(prizes))
def Track():
    print("Track: " + str(track))

"""Call of functions"""
Title()
Album()
Artist()
Year()
Genre()
Lyrics()
Platforms()
Author()
Prizes()
Track()