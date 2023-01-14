# Parašykite programą, kuri leistų vartotojui per konsolę:
#
# ieškoti įrašų pagal visus stulpelius. Vartotojas gali pasirinkti kuriuos parametrus paieškoje praleisti.
# Metus ir kainą vartotojas turėtų nurodinėti nuo -iki.

import sqlite3

konektorius = sqlite3.connect("uzduotis_20230112_1.db")
kursorius = konektorius.cursor()

paieska = []

marke_paieska = input("Įveskite automobilio markę: ")
modelis_paieska = input("Įveskite automobilio modelį: ")
spalva_paieska = input("Įveskite automobilio spalvą: ")
metai_nuo_paieska = input("Įveskite automobilio pagaminimo metus 'Nuo': ")
metai_iki_paieska = input("Įveskite automobilio pagaminimo metus 'Iki': ")
kaina_nuo_paieska = input("Įveskite automobilio kainą 'Nuo': ")
kaina_iki_paieska = input("Įveskite automobilio kainą 'Iki': ")

if marke_paieska == '':
    uzklausa1 = ''
elif marke_paieska != '' and modelis_paieska == '' and spalva_paieska == '' and metai_nuo_paieska == ''\
        and metai_iki_paieska == '' and kaina_nuo_paieska == '' and kaina_iki_paieska == '':
    uzklausa1 = " marke = ? COLLATE NOCASE"
    paieska.append(marke_paieska)
else:
    uzklausa1 = " marke = ? COLLATE NOCASE AND"
    paieska.append(marke_paieska)

if modelis_paieska == '':
    uzklausa2 = ''
elif modelis_paieska != '' and spalva_paieska == '' and metai_nuo_paieska == '' and metai_iki_paieska == ''\
        and kaina_nuo_paieska == '' and kaina_iki_paieska == '':
    uzklausa2 = " modelis = ? COLLATE NOCASE"
    paieska.append(modelis_paieska)
else:
    uzklausa2 = " modelis = ? COLLATE NOCASE AND"
    paieska.append(modelis_paieska)

if spalva_paieska == '':
    uzklausa3 = ''
elif spalva_paieska != '' and metai_nuo_paieska == '' and metai_iki_paieska == ''\
        and kaina_nuo_paieska == '' and kaina_iki_paieska == '':
    uzklausa3 = " modelis = ? COLLATE NOCASE"
    paieska.append(spalva_paieska)
else:
    uzklausa3 = " spalva = ? COLLATE NOCASE AND"
    paieska.append(spalva_paieska)

if metai_nuo_paieska == '':
    uzklausa4 = ''
elif metai_nuo_paieska != '' and metai_iki_paieska == '' and kaina_nuo_paieska == '' and kaina_iki_paieska == '':
    uzklausa4 = " pagaminimo_metai >= ?"
    paieska.append(metai_nuo_paieska)
else:
    uzklausa4 = " pagaminimo_metai >= ? AND"
    paieska.append(metai_nuo_paieska)

if metai_iki_paieska == '':
    uzklausa5 = ''
elif metai_iki_paieska != '' and kaina_nuo_paieska == '' and kaina_iki_paieska == '':
    uzklausa5 = " pagaminimo_metai <= ?"
    paieska.append(metai_iki_paieska)
else:
    uzklausa5 = " pagaminimo_metai <= ? AND"
    paieska.append(metai_iki_paieska)

if kaina_nuo_paieska == '':
    uzklausa6 = ''
elif kaina_nuo_paieska != '' and kaina_iki_paieska == '':
    uzklausa6 = " kaina <= ?"
    paieska.append(kaina_nuo_paieska)
else:
    uzklausa6 = " kaina >= ? AND"
    paieska.append(kaina_nuo_paieska)

if kaina_iki_paieska == '':
    uzklausa7 = ''
else:
    uzklausa7 = " kaina <= ?"
    paieska.append(kaina_iki_paieska)

if marke_paieska == '' and modelis_paieska == '' and spalva_paieska == '' and metai_nuo_paieska == ''\
    and metai_iki_paieska == '' and kaina_nuo_paieska == '' and kaina_iki_paieska == '':
    uzklausa = f"SELECT * FROM automobiliai"
else:
    uzklausa = f"SELECT * FROM automobiliai " \
               f"WHERE{uzklausa1}{uzklausa2}{uzklausa3}{uzklausa4}{uzklausa5}{uzklausa6}{uzklausa7}"

with konektorius:
    kursorius.execute(uzklausa, paieska)
    rezultatai = kursorius.fetchall()

if rezultatai:
    for rezultatas in rezultatai:
        print(rezultatas)
else:
    print("Nėra automobilių pagal Jūsų kriterijus!")
