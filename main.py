
#----------------------------------------------------------------------------------------#
#   IIII  GGGGGG       SSSSSS  TTTTTTTT    AAA    LL       KK    KK EEEEEEEE RRRRRRRR    b
#    II  GG    GG     SS    SS    TT      AA AA   LL       KK   KK  EE       RR     RR   e
#    II  GG           SS          TT     AA   AA  LL       KK  KK   EE       RR     RR   n
#    II  GG   GGGG     SSSSSS     TT    AA     AA LL       KKKKK    EEEEEE   RRRRRRRR    c
#    II  GG    GG           SS    TT    AAAAAAAAA LL       KK  KK   EE       RR   RR     e
#    II  GG    GG     SS    SS    TT    AA     AA LL       KK   KK  EE       RR    RR    
#   IIII  GGGGGG       SSSSSS     TT    AA     AA LLLLLLLL KK    KK EEEEEEEE RR     RR   =)
#-----------------------------------------------------------------------------------------#

from datetime import datetime as dt
from instaloader import *
from instaloader.exceptions import TwoFactorAuthRequiredException
from instascrape import *
import requests

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
global jelenlegiSTK

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
    datum = dt.now()
    ido = datum.strftime("%H:%M")
    print("\n[{}] >> Belépés\n".format(ido))
    print(valaszok)

    for k in cel:
        fiokok = k.split(',')
        for fiok in fiokok:
            fiokscrape = fiok
            url = f"https://www.instagram.com/{fiokscrape}/"
            SESSIONID = "NEM"
            headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57",
           "cookie": f"sessionid={SESSIONID};"}
            profile = Profile("https://www.instagram.com/valami")
            profile.scrape()
            posts = profile.get_posts()