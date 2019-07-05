import requests,sys,time,json
from bs4 import BeautifulSoup
import argparse

banner = """\033[0;35m  
==================================================
\033[1;32m__        __                 _____         _      
\033[1;32m\ \      / /__  _ __ _ __ __|_   _|____  _(_) ___ 
\033[1;32m \ \ /\ / / _ \| '__| '_ ` _ \| |/ _ \ \/ / |/ __|
\033[1;32m  \ V  V / (_) | |  | | | | | | | (_) >  <| | (__ 
\033[1;32m   \_/\_/ \___/|_|  |_| |_| |_|_|\___/_/\_\_|\___|
   
     BTC AUTO MINING SCRIPT FOR COWDOLLARS  V 5.0
\033[0;34m==================================================
\033[1;32mPowered\033[1;31m    :\033[1;0m WormToxic
\033[1;32mGit Hub\033[1;31m    : \033[1;0mhttps://github.com/wormtoxic
\033[1;32mCopyright © 2019 «Все права сохранены»\033[1;31m
==================================================
"""
print (banner)

parser = argparse.ArgumentParser(description='Script Auto BTC Mining for Website CowDollar')
parser.add_argument(
    '-u','--email',
    help='<Enter Your Email>',required=True
)
parser.add_argument(
    '-p','--password',
    help='<Enter Your Password>',required=True
)
parser.add_argument(
    '-s','--sleep',
    default=30,
    help='Sleep (default: 30)'
)
my_namespace = parser.parse_args()


def tunggu(x):
    sys.stdout.write("\r")
    sys.stdout.write("                                                               ")
    for remaining in range(x, 0, -1):
       sys.stdout.write("\r")
       sys.stdout.write("\033[1;30m#\033[1;0m{:2d} \033[1;32mseconds remaining".format(remaining))
       sys.stdout.flush()
       time.sleep(1)
    sys.stdout.write("                                             ")

ua = {
   "upgrade-insecure-requests": "1",
   "user-agent": "Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.121 Mobile Safari/537.36",
   "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
   "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
}

c = requests.session()
r = c.get("https://gymx.site/en/login",headers=ua)
soup = BeautifulSoup(r.text,"html.parser")
a = 0
for auth in soup.findAll("input"):
    a +=1
    autho = auth.get("value")
    if a == 2:
      break

r = c.post("https://gymx.site/en/login",headers=ua,data={"utf8": "&#x2713;","authenticity_token": autho,"user[email]": my_namespace.email,"user[password]": my_namespace.password,"commit": "Login"})
soup = BeautifulSoup(r.text,"html.parser")
print ("\033[1;37m"+soup.title.text,"\n")
a =0
if soup.title.text == "Cowdollars":
   print ("\033[1;31mFiled To Login\nPlease Chrck Your Email Or Your Password")
   sys.exit()
else:
  for ball in soup.findAll("span", class_="counter"):
    a+=1
    if a == 1:
       print ("\033[1;32mToday Balance    \033[1;31m :\033[1;0m",ball.text,"BTC")
    if a == 2:
       print ("\033[1;32mYesterday Balance \033[1;31m:\033[1;0m",ball.text,"BTC")
    if a == 3:
       print ("\033[1;32mTotal Balance\033[1;31m     :\033[1;0m",ball.text,"BTC")
    if a == 5:
       print ("\033[1;32mConvert To USD\033[1;31m    :\033[1;0m",ball.text,"USD")

a=0
for csr in soup.findAll("meta"):
    a+=1
    token = csr.get("content")
    if a == 5:
       break


print ("\033[1;37m\n\nСкрипт запущен Пожалуйста подождите..")
while True:
 try:
  r = c.get("https://gymx.site/en/mining/mine",headers=ua,cookies=r.cookies,timeout=15)
  r1 = c.post("https://gymx.site/mining/toggle_miner_state/",headers={"accept": "application/json, text/javascript, */*; q=0.01","x-csrf-token": token,"x-requested-with": "XMLHttpRequest","user-agent": "Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.121 Mobile Safari/537.36","content-type": "application/x-www-form-urlencoded; charset=UTF-8","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"} ,data={"state[mining_state]": "actived"},cookies=r.cookies,timeout=15)
  j = json.loads(r1.text)
  sys.stdout.write("\r\033[1;30m# \033[1;32m"+j["message"]["title"])
  tunggu(int(my_namespace.sleep))
  r2 = c.post("https://gymx.site/earnings",headers={"accept": "application/json, text/javascript, */*; q=0.01","x-csrf-token": token,"x-requested-with": "XMLHttpRequest","user-agent": "Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.121 Mobile Safari/537.36","content-type": "application/x-www-form-urlencoded; charset=UTF-8","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data={"earning[bitcoin]": "0.0000005"},cookies=r.cookies,timeout=15)
  js = json.loads(r2.text)
  sys.stdout.write("\r\033[1;30m#\033[0;32m "+js["message"]["title"]+" "+js["message"]["msg"])
  r3 = c.post("https://gymx.site/mining/toggle_miner_state/",headers={"accept": "application/json, text/javascript, */*; q=0.01","x-csrf-token": token,"x-requested-with": "XMLHttpRequest","user-agent": "Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.121 Mobile Safari/537.36","content-type": "application/x-www-form-urlencoded; charset=UTF-8","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data={"state[mining_state]": "passived"},cookies=r.cookies,timeout=15)
  r4 = c.get("https://gymx.site/en/mining/dashboard",headers=ua,cookies=r.cookies,timeout=15)
  soup = BeautifulSoup(r4.text,"html.parser")
  sys.stdout.write("\r\033[1;30m# \033[1;32mБаланс  BTC обновлён и он составляет\033[1;31m :\033[1;30m "+soup.find("span", class_="counter").text+"\n")
 except:
    time.sleep(3)
    pass
