# Ram
# Marke
# Modell
# Bildschirmgröße

notebook_1_ram = 64
notebook_2_ram = 23

notebook_1_marke = "Lenovo"
notebook_2_marke = "Apple"

notebook_1_modell = "Windows Edition"
notebook_2_modell = "Apple"

notebook_1_resolution = 16.1
notebook_2_resolution = 14

class Notebook:
    def __init__(self, ram, marke, modell, resolution):
        self.ram = ram
        self.marke = marke
        self.modell = modell
        self.resolution = resolution
        print(f"Neues Notebook mit Marke: " + marke + "wurde erstellt.")

nb_1 = Notebook(8, "Apple", "Macbook Pro", 14.2)