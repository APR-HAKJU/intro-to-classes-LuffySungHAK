"""
Übung 1: Auto-Klasse mit Methoden

Aufgabe:
Erstelle eine Klasse `Auto` mit:
- Konstruktor mit Parametern: marke, modell, kilometerstand
- Methode fahren() ohne Parameter: Erhöht den Kilometerstand um 100
  und gibt aus: "Gefahren! Neuer Stand: X km"
- Methode zeige_info() ohne Parameter: Gibt Marke, Modell und 
  Kilometerstand aus

Erstelle ein Auto und lass es dreimal fahren.

💡 Tipp:
- In fahren() verwendest du self.kilometerstand += 100
- Denke daran, dass Methoden immer self als ersten Parameter haben!

Erwartetes Ergebnis:
VW Golf, Kilometerstand: 50000 km
Gefahren! Neuer Stand: 50100 km
Gefahren! Neuer Stand: 50200 km
Gefahren! Neuer Stand: 50300 km
VW Golf, Kilometerstand: 50300 km
"""

# TODO: Erstelle hier die Klasse Auto
class Auto:
    def __init__(self, Marke, Modell, Kilometerstand):
        self.Marke = Marke
        self.Modell = Modell
        self.Kilometerstand = Kilometerstand
    def Fahren(self):
        self.Kilometerstand += 100
        print(f"Gefahren! Neuer Stand: {self.Kilometerstand} km")
    def zeige_info(self):
        print(f"Marke: {self.Marke}")
        print(f"Modell: {self.Modell}")
        print(f"Kilometerstand: {self.Kilometerstand}")

# TODO: Erstelle ein Auto-Objekt (z.B. VW Golf mit 50000 km)
auto1 = Auto("VW", "Golf", 400)

# TODO: Zeige die Info
auto1.zeige_info()

# TODO: Lass das Auto dreimal fahren
auto1.Fahren()
auto1.Fahren()
auto1.Fahren()

# TODO: Zeige die Info erneut

auto1.zeige_info()