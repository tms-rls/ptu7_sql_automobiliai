# Parašykite programą, kuri leistų vartotojui per konsolę:
#
# ieškoti įrašų pagal visus stulpelius. Vartotojas gali pasirinkti kuriuos parametrus paieškoje praleisti.
# Metus ir kainą vartotojas turėtų nurodinėti nuo -iki.

import sqlite3

konektorius = sqlite3.connect("uzduotis_20230112_1.db")
kursorius = konektorius.cursor()


# def rezultatai():
#     paieskos_rezultatai = kursorius.fetchall()
#     if paieskos_rezultatai:
#         for rezultatas in paieskos_rezultatai:
#             print(rezultatas)
#     else:
#         print("Nėra automobilių pagal Jūsų kriterijus!")
#
#
# while True:
#     paieska = int(input("""Pasirinkite paieškos kriterijus:
# 1 - Ieškoti pagal automobilio markę
# 2 - Ieškoti pagal automobilio modelį
# 3 - Ieškoti pagal automobilio spalvą
# 4 - Ieškoti pagal automobilio pagaminimo metus
# 5 - Ieškoti pagal automobilio kainą
# 6 - Išeiti iš programos
# """))
#     if paieska == 1:
#         marke_paieska = input("Įveskite automobilio markę: ")
#         with konektorius:
#             kursorius.execute("SELECT * FROM automobiliai WHERE marke = ? COLLATE NOCASE", (marke_paieska,))
#             rezultatai()
#     if paieska == 2:
#         modelis_paieska = input("Įveskite automobilio modelį: ")
#         with konektorius:
#             kursorius.execute("SELECT * FROM automobiliai WHERE modelis = ? COLLATE NOCASE", (modelis_paieska,))
#             rezultatai()

paieska = []

marke_paieska = str(input("Įveskite automobilio markę: "))
modelis_paieska = str(input("Įveskite automobilio modelį: "))
spalva_paieska = str(input("Įveskite automobilio spalvą: "))

if marke_paieska == '':
    s1 = ''
elif marke_paieska != '' and modelis_paieska == '' and spalva_paieska == '':
    s1 = "marke = ? COLLATE NOCASE"
    paieska.append(marke_paieska)
else:
    s1 = "marke = ? COLLATE NOCASE AND"
    paieska.append(marke_paieska)


if modelis_paieska == '':
    s2 = ''
elif modelis_paieska != '' and spalva_paieska == '':
    s2 = "modelis = ? COLLATE NOCASE"
    paieska.append(modelis_paieska)
else:
    s2 = "modelis = ? COLLATE NOCASE AND"
    paieska.append(modelis_paieska)


if spalva_paieska == '':
    s3 = ''
else:
    s3 = "spalva = ? COLLATE NOCASE"
    paieska.append(spalva_paieska)


# metai_nuo = input("Įveskite automobilio pagaminimo metus nuo: ")
# metai_iki = input("Įveskite automobilio pagaminimo metus iki: ")
# kaina_nuo = input("Įveskite automobilio kainą nuo: ")
# kaina_iki = input("Įveskite automobilio kainą iki: ")


uzklausa = f"SELECT * FROM automobiliai WHERE {s1} {s2} {s3}"

print(uzklausa)
print(paieska)

with konektorius:
    kursorius.execute(uzklausa, paieska)
    rezultatai = kursorius.fetchall()



#
# with konektorius:
#     kursorius.execute("SELECT * FROM automobiliai WHERE marke = ? OR modelis = ? OR spalva = ?"
#                       "OR pagaminimo_metai BETWEEN ? AND ? OR kaina BETWEEN ? AND ? COLLATE NOCASE", paieska)
#     rezultatai = kursorius.fetchall()

if rezultatai:
    for rezultatas in rezultatai:
        print(rezultatas)
else:
    print("Nėra automobilių pagal Jūsų kriterijus!")
