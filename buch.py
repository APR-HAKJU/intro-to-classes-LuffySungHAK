# TODO: 
# Aufgabe 1:
"""Erstelle eine Klasse Buch mit folgenden Attributen:

- titel
- autor
- seiten
- gelesen (Boolean )

Erstelle zwei Bücher: Eines, das du gelesen hast (setze gelesen=True), 
und eines, das du noch nicht gelesen hast.
"""
class Book:
    def __init__(self, titel, autor, seiten, gelesen):
        self.titel = str(titel)
        self.autor = str(autor)
        self.seiten = int(seiten)
        self.gelesen = bool(gelesen)

book1 = Book("Kinder von Bahnhof Zoo", "Caroline", 200, True)
book2 = Book("Bibel", "Gott", 1200, False)

# TODO: Aufgabe 2:
# Gib für jedes Buch eine Nachricht aus, die angibt, ob du das Buch gelesen hast oder nicht.

print(f"Book: {book1.titel} gelesen: {book1.gelesen}")
print(f"Book: {book2.titel} gelesen: {book2.gelesen}")

