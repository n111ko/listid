from pickle import MARK
import string

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
            
            elif taht in markid:
                m += 1

            elif taht == " ":
                t += 1

    print("Vokaali :", v)
    print("Konsonanti :", k)
    print("Markid :", m)
    print("Tühikud :", t)