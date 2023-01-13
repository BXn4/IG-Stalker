#----------------------------------------------------------------------------------------#
#   IIII  GGGGGG       SSSSSS  TTTTTTTT    AAA    LL       KK    KK EEEEEEEE RRRRRRRR    b
#    II  GG    GG     SS    SS    TT      AA AA   LL       KK   KK  EE       RR     RR   e
#    II  GG           SS          TT     AA   AA  LL       KK  KK   EE       RR     RR   n
#    II  GG   GGGG     SSSSSS     TT    AA     AA LL       KKKKK    EEEEEE   RRRRRRRR    c
#    II  GG    GG           SS    TT    AAAAAAAAA LL       KK  KK   EE       RR   RR     e
#    II  GG    GG     SS    SS    TT    AA     AA LL       KK   KK  EE       RR    RR    
#   IIII  GGGGGG       SSSSSS     TT    AA     AA LLLLLLLL KK    KK EEEEEEEE RR     RR   =)
#-----------------------------------------------------------------------------------------#

from datetime import datetime
import shutil

mindenrendben = False
valaszok = []

print("A program ezeket az adatokat a config.txt fájlban fogja tárolni. Ezeket bármikor módosíthatod a config fájlban.")

print("Felhasználóneved: ")
felhasznev = input()
valaszok.append(felhasznev)

print("Jelszód: ")
jelszo = input()
valaszok.append(jelszo)

print("Cél (vesszővel válaszd el, ha többet szeretnél): ")
cel = input()
valaszok.append(cel)

if mindenrendben == False:

    def nulladik():
        print("Hány percenként fusson le? (perc (Minimum 30 perc))) ")
        global intervallum 
        intervallum = int(input())
        # CSAK SAJÁT FELELŐSÉGRE ÁLLÍTHATOD BE 30 PERCNÉL HAMARABB, MIVEL ELŐFORDULHAT, HOGY TÖRLIK A FIÓKOD, MIVEL TÚL GYAKRAN FUT LE A KÉRDEZÉS!
        if intervallum > 29:
            valaszok.append(intervallum)
            elso()
        else:
            nulladik()

    def elso():
        print("A profilt teljesen szeretnéd letölteni? (I = Mindent letölt, N = Kitudod választani, hogy mit szeretnél) [I / N] ")
        valasz = input()
        if valasz == "i" or valasz == "I":
            mindent()
        if valasz == "n" or valasz == "N":
            masodik()


    def masodik():
        print("Szeretnéd-e letölteni a követőket? [I / N] ")
        kovetok = input()
        if kovetok == "i" or kovetok == "I" or kovetok == "n" or kovetok == "N":
            valaszok.append(kovetok)
            harmadik()
        else:
            masodik()

    def harmadik():
        print("Szeretnéd-e letölteni a követéseket? [I / N] ")
        kovetes = input()
        if kovetes == "i" or kovetes == "I" or kovetes == "n" or kovetes == "N":
            valaszok.append(kovetes)
            negyedik()
        else:
            harmadik()

    def negyedik():
        print("Szeretnéd-e letölteni a profilképet? [I / N] ")
        pfp = input()
        if pfp == "i" or pfp == "I" or pfp == "n" or pfp == "N":
            valaszok.append(pfp)
            otodik()
        else:
            negyedik()

    def otodik():
        print("Szeretnéd-e letölteni a biot? [I / N] ")
        bio = input()
        if bio == "i" or bio == "I" or bio == "n" or bio == "N":
            valaszok.append(bio)
            hatodik()
        else:
            otodik()

    def hatodik():
        print("Szeretnéd-e letölteni a bejegyzéseket? (képek / videók) [I / N] ")
        bejegyzesek = input()
        if bejegyzesek == "i" or bejegyzesek == "I" or bejegyzesek == "n" or bejegyzesek == "N":
            valaszok.append(bejegyzesek)
            hetedik()
        else:
            hatodik()

    def hetedik():
        print("Szeretnéd-e letölteni a sztorikat? [I / N] ")
        sztorik = input()
        if sztorik == "i" or sztorik == "I" or sztorik == "n" or sztorik == "N":
            valaszok.append(sztorik)
            nyolcadik()
        else:
            hetedik()
    
    def nyolcadik():
        print("Szeretnéd-e letölteni a kiemelteket? (hightlight) [I / N] ")
        highlight = input()
        if highlight == "i" or highlight == "I" or highlight == "n" or highlight == "N":
            valaszok.append(highlight)
            kilencedik()
        else:
            nyolcadik()

    def kilencedik():
        print("Szeretnéd-e letölteni a jelöléseket? [I / N] ")
        jelolesek = input()
        if jelolesek == "i" or jelolesek == "I" or jelolesek == "n" or jelolesek == "N":
            valaszok.append(jelolesek)
            tizedik()
        else:
            kilencedik()

    def tizedik():
        print("Szeretnéd-e letölteni a bejegyzések hozzászolásait? [I / N] ")
        hozzaszolasokBejegyzes = input()
        if hozzaszolasokBejegyzes == "i" or hozzaszolasokBejegyzes == "I" or hozzaszolasokBejegyzes == "n" or hozzaszolasokBejegyzes == "N":
            valaszok.append(hozzaszolasokBejegyzes)
            tizenegyedik()
        else:
            tizedik()

    def tizenegyedik():
        print("Szeretnéd-e letölteni a megjelölt képek hozzászolásait? [I / N] ")
        hozzaszolasokMegjelolt = input()
        if hozzaszolasokMegjelolt == "i" or hozzaszolasokMegjelolt == "I" or hozzaszolasokMegjelolt == "n" or hozzaszolasokMegjelolt == "N":
            valaszok.append(hozzaszolasokMegjelolt)
            valaszok.append("0")
            sikeres()
        else:
            tizenegyedik()
        
    def sikeres():
        shutil.copy2('config_default.txt', 'config.txt')
        with open("config.txt", "r+") as file:
            sor = file.readlines()
            for i, line in enumerate(sor):
                if '=' in line:
                    sor[i] = line.rstrip() + str(valaszok[i]) + "\n"
                    file.seek(0)
                    file.writelines(sor)
            
        print("Sikeres konfigurálás! Mostmár indíthatod a main.py fájlt!")
    
    def mindent():
        ma = datetime.now()
        valaszokx = [valaszok[0],valaszok[1],valaszok[2],intervallum, "I", "I", "I", "I", "I", "I", "I", "I", "I", "I", "0"]
        shutil.copy2('config_default.txt', 'config.txt')
        with open("config.txt", "r+") as file:
            sor = file.readlines()
            for i, line in enumerate(sor):
                if '=' in line:
                    sor[i] = line.rstrip() + str(valaszokx[i]) + "\n"
                    file.seek(0)
                    file.writelines(sor)
        print("Sikeres konfigurálás! Mostmár indíthatod a main.py fájlt!")

    nulladik()