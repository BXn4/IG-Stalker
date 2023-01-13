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
insta = instaloader.Instaloader()

with open("config.txt", "r") as file:
    valaszok = [line.split('=')[-1].strip() for line in file.readlines() if '=' in line]
    felhasznalonev = valaszok[0]
    jelszo = valaszok[1]
    datum = datetime.now()
    ido = datum.strftime("%H:%M")
    print("\n[{}] >> Belépés\n".format(ido))
    try:
        insta.login(felhasznalonev, jelszo)
    except TwoFactorAuthRequiredException:
        kod = input("Kétlépcsős azonosítás szükséges, add meg a kódot: ")
        insta.two_factor_login(kod)
