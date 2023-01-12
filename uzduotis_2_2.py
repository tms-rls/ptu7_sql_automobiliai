# Parašykite programą, kuri leistų vartotojui per konsolę:
#
# ieškoti įrašų pagal visus stulpelius. Vartotojas gali pasirinkti kuriuos parametrus paieškoje praleisti.
# Metus ir kainą vartotojas turėtų nurodinėti nuo -iki.

import sqlite3

konektorius = sqlite3.connect("uzduotis_20230112_1.db")
kursorius = konektorius.cursor()

marke_paieska = input("Įveskite automobilio markę: ")
modelis_paieska = input("Įveskite automobilio modelį: ")
spalva_paieska = input("Įveskite automobilio spalvą: ")
metai_nuo = input("Įveskite automobilio pagaminimo metus nuo: ")
metai_iki = input("Įveskite automobilio pagaminimo metus iki: ")
kaina_nuo = input("Įveskite automobilio kainą nuo: ")
kaina_iki = input("Įveskite automobilio kainą iki: ")

paieska = (marke_paieska, modelis_paieska, spalva_paieska, metai_nuo, metai_iki, kaina_nuo, kaina_iki)


with konektorius:
    kursorius.execute("SELECT * FROM automobiliai WHERE marke = ? OR modelis = ? OR spalva= ?"
                      "OR pagaminimo_metai BETWEEN ? AND ? OR kaina BETWEEN ? AND ?", paieska)
    rezultatai = kursorius.fetchall()

if rezultatai:
    for rezultatas in rezultatai:
        print(rezultatas)
else:
    print("Nėra automobilių pagal Jūsų kriterijus!")
