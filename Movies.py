movie_1 = ["Horror", "it", 2017, 120]
movie_2 = ["Fantasy", "Harry Potter", 1997, 97]

print(f"Titel des Filmes: {movie_1[1]}")


class Movie:
    def __init__(self, Genre, Titel, Date, Min):
        self.Titel = Titel
        self.Genre = Genre
        self.Date = Date
        self.Min = Min

        print(f"Neue Movie mit Titel: {Titel} wurde erstellt.")


movie_6 = Movie(Titel = input(f"Titel des Filmes: "), Genre=input(f"Genre des Filmes: "), Date=int(input(f"Release Date des Filmes: ")), Min=int(input(f"Wie lang: ")))

print(f"Titel des Filmes: {movie_6.Titel}")