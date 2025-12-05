"""
Übung 2: Kaffeemaschine mit Parametern

Aufgabe:
Erstelle eine Klasse `Kaffeemaschine` mit:
- Konstruktor mit Parameter: wasserstand (in ml, z.B. 1000)
- Methode kaffee_machen(menge) mit Parameter:
  - Prüft, ob genug Wasser da ist
  - Wenn ja: Reduziert Wasserstand und gibt aus "☕ Kaffee gemacht! X ml"
  - Wenn nein: Gibt aus "❌ Nicht genug Wasser! Bitte nachfüllen."
- Methode wasser_nachfuellen(menge) mit Parameter: Erhöht den Wasserstand
- Methode zeige_status() ohne Parameter: Zeigt aktuellen Wasserstand

Erstelle eine Kaffeemaschine mit 500ml Wasser, mache 2x Kaffee (je 200ml),
versuche es nochmal (es sollte dieses Mal fehlschlagen), fülle Wasser nach und mache nochmal Kaffee.

💡 Tipps:
- Verwende if self.wasserstand >= menge: um zu prüfen
- self.wasserstand -= menge verringert den Wasserstand
- self.wasserstand += menge erhöht den Wasserstand

Erwartetes Ergebnis:
Wasserstand: 500 ml
☕ Kaffee gemacht! 200 ml
☕ Kaffee gemacht! 200 ml
❌ Nicht genug Wasser! Bitte nachfüllen.
💧 500 ml Wasser nachgefüllt
☕ Kaffee gemacht! 200 ml
Wasserstand: 400 ml
"""

# TODO: Erstelle hier die Klasse Kaffeemaschine
class Kaffeemaschine:
    def __init__(self, Wasserstand):
        self.Wasserstand = Wasserstand
    def kaffee_machen(self, Menge):
        self.Menge = Menge
        if self.Wasserstand >= Menge:
            self.Wasserstand -= Menge
            print(f"☕ Kaffe gemacht! {Menge} ml")
        else:
            print(f"❌ Nicht genug Wasser! Bitte nachfüllen.")
    def zeige_status(self):
        print(f"Wasserstand: {self.Wasserstand} ml")
    def wasser_nach_fullen(self, menge):
        self.Wasserstand += menge
        print(f"💧 {menge} ml Wasser nachgefüllt")




# TODO: Erstelle eine Kaffeemaschine mit 500ml Wasser
Kaffeemaschine_1 = Kaffeemaschine(500)

# TODO: Zeige den Status
Kaffeemaschine_1.zeige_status()

# TODO: Mache 2x Kaffee mit je 200ml
Kaffeemaschine_1.kaffee_machen(200)
Kaffeemaschine_1.kaffee_machen(200)

# TODO: Versuche nochmal Kaffee zu machen (sollte fehlschlagen)
Kaffeemaschine_1.kaffee_machen(200)

# TODO: Fülle 500ml Wasser nach
Kaffeemaschine_1.wasser_nach_fullen(400)

# TODO: Mache nochmal Kaffee mit 200ml
Kaffeemaschine_1.kaffee_machen(200)

# TODO: Zeige den Status erneut
Kaffeemaschine_1.zeige_status()