"""
Pagrindinių Python duomenų tipų naudojimo pavyzdžiai
"""

# Skaičiai

# sveiki skaičiai (int)

sveiki_skaičiai = 1

print(f"Sveikų skaičių tipas: {type(sveiki_skaičiai)}")
print(f"2 + 5 = {2+5}")
print(f"Dalybos sveika liekana 16 % 5 = {16%5}")
print(f"Sveikas dalybos rezultatas 16 // 5 = {16 // 5}")

# float skaičiai (float)

skaičiai_su_liekana = 4.15

print(f"Skaičių su liekana tipas: {type(skaičiai_su_liekana)}")
print(f"2 + 5.15 = {2+5.15}")
print(f"Dalybos sveika liekana 16.45 % 5 = {16.45%5}")
print(f"Sveikas dalybos rezultatas 16.45 // 5 = {16.45 // 5}")

# String tipas (str)

sakinys = "String pavyzdys"

print(f"Teksto tipas: {type(sakinys)}")
print(sakinys)
print("Įterpimas su format {}".format(sakinys))
print("Įterpimas su format naudojant vardus {pirmas} ir {antras}".format(pirmas="1 kintamasis", antras="2 kintamasis"))
print("Pirmas {} antras {} trečias {}".format(*[1, 2, 3]))

# Sąrašai (list)

sąrašas = [25, None, "Something"]
print(f"Sąrašo ilgis: {len(sąrašas)}")
print(f"Sąrašo pirmas elementas {sąrašas[0]}")
print(f"Sąrašo paskutinis elementas {sąrašas[-1]}")
print(f"Sąrašo iškarpa (slice) - sąrašas[:2] : {sąrašas[:2]}")
print(f"Sąrašo iškarpa (slice) - sąrašas[:-1] : {sąrašas[:-1]}")
print(f"Sąrašo iškarpa (slice) - sąrašas[:20] : {sąrašas[:20]}")
print(f"Sąrašo iškarpa (slice) - sąrašas[5:] : {sąrašas[5:]}")

# Dictionary (dict)

# galima kaip raktą nurodyti bet ką
žodynas = {"raktinis žodis": "vertė", 1: "vienas", "labas": "hello"}
# galima nurodyti tik žodžius, negali sakyti 1="vienas"
žodynas_2 = dict(raktinis_žodis="vertė",one="vienas",labas="hello")


# Funkcijos
def kvadratu(skaičius):
    return skaičius**2


# Klasės

class Skaičius:
    kvadratas = None
    kubas = None
    def __init__(self, skaičius):
        self.kvadratu(skaičius)
        self.kubu(skaičius)
    def kvadratu(self, skaičius):
        self.kvadratas = skaičius ** 2
    def kubu(self, skaičius):
        self.kubas = skaičius **3

naujas = Skaičius(3)
print(naujas.kvadratas)
print(naujas.kubas)