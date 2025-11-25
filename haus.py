# TODO: Aufgabe 1:
# Ändere den Code unten, so dass die Eigenschaften des Hauses als Attribute im Konstruktor definiert sind.
# Aktuell werden die Eigenschaften als separate Variablen definiert.
# Definiere einen Konstruktor (__init__), um die Attribute zu initialisieren.
class Haus:
    def __init__(self, quadratmeter, schlafzimmer, badezimmer):
        self.quadratmeter = quadratmeter
        self.schlafzimmer = schlafzimmer
        self.badezimmer = badezimmer
    



haus1 = Haus(quadratmeter=120, schlafzimmer=3, badezimmer=2)
haus1.quadratmeter = 120
haus1.schlafzimmer = 3
haus1.badezimmer = 2

print(f"Haus: {haus1.quadratmeter}m², {haus1.schlafzimmer} Schlafzimmer")

# TODO: Aufgabe 2: Erstelle drei weitere Objekte der Klasse Haus mit unterschiedlichen Eigenschaften.
haus2 = Haus(115, 2, 2)
haus3 = Haus(130, 4, 3)
haus4 = Haus(125, 3, 2)

# TODO: Aufgabe 3: Gib die Anzahl der Schlafzimmer und Badezimmer für jedes Haus aus.

print(f"Haus: {haus2.quadratmeter}m², {haus2.schlafzimmer} Schlafzimmer")
print(f"Haus: {haus3.quadratmeter}m², {haus3.schlafzimmer} Schlafzimmer")
print(f"Haus: {haus4.quadratmeter}m², {haus4.schlafzimmer} Schlafzimmer")