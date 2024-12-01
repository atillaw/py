import requests
site = input("Log çekmek istediğiniz siteyi girin (exxen.com): ")
api = requests.get(f"https://wizardxcoder.com/log.php?key=3ff04a975b5cc154&site={site}").json()
print(f"Log sayısı: {api['log_count']}")
for log in api["logs"]:
 with open(f"/sdcard/{site}_logs.txt","a") as yazdır:
  yazdır.write(log+"\n")