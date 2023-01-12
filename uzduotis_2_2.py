# Parašykite programą, kuri leistų vartotojui per konsolę:
#
# ieškoti įrašų pagal visus stulpelius. Vartotojas gali pasirinkti kuriuos parametrus paieškoje praleisti.
# Metus ir kainą vartotojas turėtų nurodinėti nuo -iki.

import sqlite3

konektorius = sqlite3.connect("uzduotis_20230112_1.db")
kursorius = konektorius.cursor()

marke_paieska = str(input("Įveskite automobilio markę: "))
modelis_paieska = str(input("Įveskite automobilio modelį: "))
spalva_paieska = str(input("Įveskite automobilio spalvą: "))
metai_nuo = str(input("Įveskite automobilio pagaminimo metus nuo: "))
metai_iki = str(input("Įveskite automobilio pagaminimo metus iki: "))
kaina_nuo = float(input("Įveskite automobilio kainą nuo: "))
kaina_iki = float(input("Įveskite automobilio kainą iki: "))

paieska = (marke_paieska, modelis_paieska, spalva_paieska, metai_nuo, metai_iki, kaina_nuo, kaina_iki)

with konektorius:
    kursorius.execute("SELECT * FROM automobiliai WHERE marke = ? AND modelis = ? AND spalva= ?"
                      "AND pagaminimo_metai BETWEEN ? AND ? AND kaina BETWEEN ? AND ?", paieska)
    print(kursorius.fetchall())

# while True:
#     paieska = int(input("""Įveskite paieškos kriterijus:
# 1 - Įveskite automobilio markę
#
# """))


