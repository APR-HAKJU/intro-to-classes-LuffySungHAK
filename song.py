# Gegeben ist eine Liste, die Informationen über verschiedene Songs enthält.
# Verändere den Code so, dass eine Klasse "Song" definiert wird.
# Die Eigenschaften Titel, Künstler und Anzahl der Streams sollen als Attribute im Konstruktor definiert werden

song_1 = ["Blinding Lights", "The Weeknd", 4_200_000_000]
song_2 = ["Shape of You", "Ed Sheeran", 5_300_000_000]
song_3 = ["Dance Monkey", "Tones and I", 3_400_000_000]

#TODO: Aufgabe 1: 
#   Definiere die Klasse "Song" mit einem Konstruktor (__init__),
#  der die Attribute titel, künstler und streams initialisiert.
songs = []
class Song:
    def __init__(self, titel, autor, streams):
        self.titel = str(titel)
        self.autor = str(autor)
        self.streams = str(streams)
        songs.append(Song)
    def print_info(self):
        print(f"Der Song {self.titel} von {self.autor} hat {self.streams} Streams.")
        

# TODO: Aufgabe 2:
#   Erstelle drei Objekte der Klasse "Song" mit den Informationen aus der Liste oben

song1 = Song("Blinding Lights", "The Weeknd", 4_200_000_000)
song2 = Song("Shape of You", "Ed Sheeran",5_300_000_000)
song3 = Song("Dance Monkey", "Tones and I", 3_400_000_000)

songs.append(song1)
songs.append(song2)
songs.append(song3)
# TODO: Aufgabe 3:
#   Gib für jeden Song den Titel und die Anzahl der Streams in folgendem Format aus:
#   "Der Song '<Titel>' von <Künstler> hat <Anzahl der Streams> Streams."



for x in songs:
    x.print_info()