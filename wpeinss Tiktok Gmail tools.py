import webbrowser
webbrowser.open('https://t.me/wpeinhackk')
import requests
import random
import threading
E = '\x1b[1;31m'
Z = '\x1b[1;31m'
R = '\x1b[1;31m'
X = '\x1b[1;33m'
F = '\x1b[2;32m'
C = '\x1b[1;97m'
B = '\x1b[2;36m'
Y = '\x1b[1;34m'
E = '\x1b[1;31m'
B = '\x1b[2;36m'
G = '\x1b[1;32m'
S = '\x1b[1;33m'
C1 = '\x1b[2;35m'
G = '\x1b[1;35m'
Z = '\x1b[1;31m'
X = '\x1b[1;33m'
Z1 = '\x1b[2;31m'
F = '\x1b[2;32m'
A = '\x1b[2;34m'
C = '\x1b[2;35m'
B = '\x1b[2;36m'
Y = '\x1b[1;34m'
M = '\x1b[1;37m'
S = '\x1b[1;33m'
U = '\x1b[1;37m'
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
BBlue = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'
import requests
import sys
import os
import time
token = input(f'''{Z} [{B}⌯{Z}] {R}𝘌𝘯𝘵𝘦𝘳 𝘛𝘰𝘬𝘦𝘯 ➪  ''' + B)
ID = input(f'''{Z} [{M}⌯{Z}] {R}𝘌𝘯𝘵𝘦𝘳 𝘐𝘋 ➪ ''' + B)
import requests

def sui():
  try:
    user = '1234567890.asdfghjklqwertyuiopzxcvbnm'
    num = ('Michael', 'Christopher', 'Jessica', 'Matthew', 'Ashley', 'Jennifer', 'Joshua', 'Amanda', 'David', 'Daniel', 'James', 'Robert', 'John', 'Joseph', 'Andrew', 'Ryan', 'Brandon', 'Jason', 'Justin', 'Sarah', 'William', 'Jonathan', 'Stephanie', 'Brian', 'Nicole', 'Nicholas', 'Anthony', 'Heather', 'Elizabeth', 'Megan', 'Adam', 'Eric', 'Melissa', 'Kevin', 'Steven', 'Eizon'); 
    rang = ''.join(random.choice(num) for i in range(1))
    name = ''.join(random.choice(user) for i in range(6))
    username = name
    email = name + '@gmail.com'
    res = requests.get(f'''https://GmailandTiktokandzaid.zaidbot.repl.co/2/email={email}''').text
    if '"By":"@Eiz0n","Email":"Hit"' in res:
        print(f'''{F}Hit Email : {email}''')
    api = requests.get(f'''https://api.dlyar-dev.tk/info-tiktok.json?user={username}''').json()
    if api['status'] == True:
        name = api['name']
        followers = api['followers']
        following = api['following']
        like = api['likes']
        id = api['id']
        code = api['code-country']
        country = api['country']
        tlg = f'''\n n𝙽𝙰𝙼𝙴  : {name}\n𝚄𝚂𝙴𝚁 𝙽𝙰𝙼𝙴  : {username}\n𝙶𝙼𝙰𝙸𝙻  : {email}\n𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂  : {followers}\n𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶  : {following}\n𝙻𝙸𝙺𝙴  : {like}\n𝙸𝙳  : {id}\n𝚄𝚁𝙻  : https://www.tiktok.com/@{username}\n By @wpeinss @wpeinhackk '''
        tlg = f'''\n\n𝙽𝙰𝙼𝙴  : {name}\n𝚄𝚂𝙴𝚁 𝙽𝙰𝙼𝙴  : {username}\n𝙶𝙼𝙰𝙸𝙻  : {email}\n𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂  : {followers}\n𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶  : {following}\n𝙻𝙸𝙺𝙴  : {like}\n𝙸𝙳  : {id}\n𝚄𝚁𝙻 : https://www.tiktok.com/@{username}\n By @wpeinss ~ @wpeinhackk'''
        requests.get('https://t.me/mlopaq/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(tlg))
        print(tlg)
    else:
      print(f''' Bad Gmail : {email}''')
  except:
    print(f''' Bad Gmail : {email}''')
while True:
    sui()
    
    
    
    # @wpeinss
