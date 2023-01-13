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
from instaloader import *
from instaloader.exceptions import TwoFactorAuthRequiredException

global felhasznalonev
global jelszo

global cel
cel = []
global intervallumERTEK
global kovetokERTEK
global kovetesERTEK
global pfpERTEK
global bioERTEK
global bejegyzesekERTEK
global sztorikERTEK
global kiemeltekERTEK
global jelolesekERTEK
global bejegyzesekHozzaszolasokERTEK
global jelolesekHozzaszolasokERTEK
global elozoERTEK

insta = instaloader.Instaloader()

with open("config.txt", "r") as file:
    valaszok = [line.split('=')[-1].strip() for line in file.readlines() if '=' in line]
    felhasznalonev = valaszok[0]
    jelszo = valaszok[1]
    cel.append(valaszok[2])
    intervallumertek = valaszok[3]
    kovetokERTEK = valaszok[4]
    kovetesERTEK = valaszok[5]
    pfpERTEK = valaszok[6]
    bioERTEK =valaszok[7]
    bejegyzesekERTEK = valaszok[8]
    sztorikERTEK = valaszok[9]
    kiemeltekERTEK = valaszok[10]
    jelolesekERTEK = valaszok[11]
    bejegyzesekHozzaszolasokERTEK = valaszok[12]
    jelolesekHozzaszolasokERTEK = valaszok[13]
    elozoERTEK = valaszok[14]
    datum = datetime.now()
    ido = datum.strftime("%H:%M")
    print("\n[{}] >> Belépés\n".format(ido))
    print(valaszok)

   # while True:
    #    if elozoERTEK == "0":
     #       for i in range(len(cel)):
      #          print(cel[i])
       #     break


    try:
        insta.load_session_from_file(felhasznalonev)
    except FileNotFoundError:
        try:
            insta.login(felhasznalonev, jelszo)
        except TwoFactorAuthRequiredException:
            kod = input("Kétlépcsős azonosítás szükséges, add meg a kódot: ")
            insta.two_factor_login(kod)