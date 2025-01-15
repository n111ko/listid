from pickle import MARK
import string

##### Ülesanne 1 #####

vokaali = ["a","e","u","o","i","ü","õ","ö","ä"]
konsonanti = "qwrtpsdfghjklzxcvbnm"
markid = string.punctuation # %&/()=><{}[]
v = k = m = t = 0

while True:
    tekst = input("Sisesta mingi tekst: ").lower()
    
    if tekst.isdigit():
        break
    else:
        tekst_list = list(tekst)
        print(tekst_list)

        for taht in tekst_list:
            if taht in vokaali:
                v += 1
            
            elif taht in konsonanti:
                k += 1
            
            elif taht in markid or taht == "ˇ":
                m += 1

            elif taht == " ":
                t += 1

    print("Vokaali :", v)
    print("Konsonanti :", k)
    print("Markid :", m)
    print("Tühikud :", t)

######################



##### Ülesanne 2 #####

nimed = []

for i in range(5):
    nimi = input(f"{i + 1}. Nimi: ")
    nimed.append(nimi)
print(nimed)
nimed.sort()
print("Sorteerimise pärast: ")
print(nimed)
print(f"Viimasena lisatud nimi on: {nimi}") # {nimed[4]}, {nimed[-1]}

v = input("Kas muudame nimeid? ").lower()

if v == "jah":
    v = input("Nimi või positsioon: N/P ").upper()

    if v == "P":
        print("Sisesta nime asukoht")
        v = int(input())


    else:
        print("Sisesta nimi")






######################
