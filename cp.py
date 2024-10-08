import os
try:
	import names
except:
	os.system('pip install names')
	import names
import requests,os,time,string,random,names
try:
	import requests
except:
	os.system('pip install requests')
try:
	from cfonts import render  
except:
	os.system('pip install python-cfonts')
proxies = None
import re
import requests
try:
  from faker import Faker
except:
  os.system("pip install faker")
  from faker import Faker
from time import sleep
import random
try:
  from user_agent import generate_user_agent as gg
except:
  os.system("pip install user_agent")
  from user_agent import generate_user_agent as gg
  
output = render('Insta', colors=['white', 'magenta'], align='center')
print(output)   
E = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'
M = '\x1b[1;37m'
B = '\x1b[38;5;208m'
token = input(f' {F}({M}1{F}) {M} 𝐄𝐧𝐭𝐞𝐫 𝐓𝐨𝐤𝐞𝐧{F}  ' + E)
print(X + ' ═════════════════════════════════  ')
ID = input(f' {F}({M}2{F}) {M} 𝐄𝐧𝐭𝐞𝐫 𝐈𝐃{F}  ' + E)
faker = Faker()
faker1 = Faker('ru_RU')
faker2 = Faker('fa')
faker3 = Faker('en')
faker4 = Faker('zh')
faker5 = Faker('ar')
faker6 = Faker('ko_KR')

def GetNewEmail():
    nn = faker.name()
    yy = faker1.name()
    mm = faker2.name()
    pp = faker3.name()
    ko = faker4.name()
    aa = faker5.name()
    bv = faker6.name()
    nam = random.choice([nn, yy, mm, pp, ko, aa, bv])
    url = 'https://api.internal.temp-mail.io/api/v3/email/new'
    data = {'name': nam, 'domain': 'greencafe24.com'}
    headers = {'User-Agent': gg()}

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        req = response.json()
        Email = req['email']
        print(f"Your Email is {Email}")
        return Email
    else:
        print(f"Failed to create account. Status code: {response.status_code}")
        return None
        
def GetMessage(Email):
    while True:
        sleep(2)
        url = f'https://api.internal.temp-mail.io/api/v3/email/{Email}/messages'
        response = requests.get(url)
        if response.status_code == 200:
            messages = response.json()
            if messages:
                for msg in messages:
                    body_text = msg.get('body_text', '')
                    subject = msg.get('subject', '')
                    print(f"الموضوع: {subject}")           
                    match = re.search(r'\b\d{6}\b', body_text)
                    if match:
                        code = match.group(0)
                        print(f"رمز التأكيد الخاص بك هو: {code}")
                        return code
                break
            else:
                print("لا توجد رسائل")
        else:
            print(f"Failed to get messages. Status code: {response.status_code}")
       

def get_headers(Country,Language):
    while True:
        try:
            an_agent=f'Mozilla/5.0 (Linux; Android {random.randint(9,13)}; {"".join(random.choices(string.ascii_uppercase, k=3))}{random.randint(111,999)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'

            res = requests.get("https://www.facebook.com/",headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'},proxies=proxies, timeout=30)
            
            js_datr = res.text.split('["_js_datr","')[1].split('",')[0]
            
            r=requests.get('https://www.instagram.com/api/v1/web/accounts/login/ajax/',headers={
                'user-agent': an_agent,
            },proxies=proxies,timeout=30).cookies

            headers1 = {
                'authority': 'www.instagram.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': f'{Language}-{Country},en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                'cookie': f'dpr=3; csrftoken={r["csrftoken"]}; mid={r["mid"]}; ig_nrcb=1; ig_did={r["ig_did"]}; datr={js_datr}',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': an_agent,
                'viewport-width': '980',
            }
            
            response1 = requests.get('https://www.instagram.com/', headers=headers1,proxies=proxies,timeout=30)
            
            appid=response1.text.split('APP_ID":"')[1].split('"')[0]
            
            rollout=response1.text.split('rollout_hash":"')[1].split('"')[0]
            
            headers = {
                'authority': 'www.instagram.com',
                'accept': '*/*',
                'accept-language': f'{Language}-{Country},en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': f'dpr=3; csrftoken={r["csrftoken"]}; mid={r["mid"]}; ig_nrcb=1; ig_did={r["ig_did"]}; datr={js_datr}',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/signup/email/',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': an_agent,
                'viewport-width': '360',
                'x-asbd-id': '198387',
                'x-csrftoken': r["csrftoken"],
                'x-ig-app-id': str(appid),
                'x-ig-www-claim': '0',
                'x-instagram-ajax': str(rollout),
                'x-requested-with': 'XMLHttpRequest',
                'x-web-device-id': r["ig_did"],
            }
            
            return headers
        except Exception as E:
            print(E)

def Get_UserName(Headers,Name,Email):
    try:
        updict = {"referer": 'https://www.instagram.com/accounts/signup/birthday/'}
        Headers = {key: updict.get(key, Headers[key]) for key in Headers}
        while True:

            data = {
                'email': Email,
                'name': Name+str(random.randint(1,99)),
            }

            response = requests.post(
                'https://www.instagram.com/api/v1/web/accounts/username_suggestions/',
                headers=Headers,
                data=data,
                proxies=proxies,
                timeout=30
            )
            
            if 'status":"fail' in response.text:
                print("Turn VPN")
            elif 'status":"ok' in response.text :
                print("Good Creating")
                return random.choice(response.json()['suggestions'])
            else:print("Turn VPN ")

    except Exception as E:
        print(E)

def Send_SMS(Headers,Email):
    try:
        data = {
            'device_id': Headers['cookie'].split('mid=')[1].split(';')[0],
            'email': Email,
}

        response = requests.post(
            'https://www.instagram.com/api/v1/accounts/send_verify_email/',
            headers=Headers,
            data=data,
            proxies=proxies,
            timeout=30
        )
        
        return response.text
    except Exception as E:
        print(E)

def Validate_Code(Headers,Email,Code):

    try:
        updict = {"referer": 'https://www.instagram.com/accounts/signup/emailConfirmation/'}
        Headers = {key: updict.get(key, Headers[key]) for key in Headers}

        data = {
            'code': Code,
            'device_id': Headers['cookie'].split('mid=')[1].split(';')[0],
            'email': Email,
        }

        response = requests.post(
            'https://www.instagram.com/api/v1/accounts/check_confirmation_code/',
            headers=Headers,
            data=data,
            proxies=proxies,
            timeout=30
        )
        return response

    except Exception as E:
        print(E)

def Create_Acc(Headers, Email, SignUpCode):
    try:
        firstname = names.get_first_name()
        UserName = Get_UserName(Headers, firstname, Email)
        Password = firstname.strip() + '@' + str(random.randint(111, 999))

        updict = {"referer": 'https://www.instagram.com/accounts/signup/username/'}
        Headers = {key: updict.get(key, Headers[key]) for key in Headers}
        
        data = {
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{round(time.time())}:{Password}',
            'email': Email,
            'username': UserName,
            'first_name': firstname,
            'month': random.randint(1, 12),
            'day': random.randint(1, 28),
            'year': random.randint(1990, 2001),
            'client_id': Headers['cookie'].split('mid=')[1].split(';')[0],
            'seamless_login_enabled': '1',
            'tos_version': 'row',
            'force_sign_up_code': SignUpCode,
        }      

        response = requests.post(
            'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/',
            headers=Headers,
            data=data,
            proxies=proxies,
            timeout=30
        )        
        if '"account_created":true' in response.text:
            tlg = f'''
Good Creat..!      
Email ==> {Email}
Password ==> {Password}
Username ==> {UserName}
'''
            requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}')
            print(F+tlg) 
            with open("Insta-Acc_good.txt", "a") as f:
                f.write(tlg + '\n')                          
            
        else:
            tlg = f"""
CP Creat            
Email ==> {Email}
Password ==> {Password}
Username ==> {UserName}
"""
            requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}')
            with open("Insta-Acc_bad.txt", "a") as f:
                f.write(tlg + '\n')       
            print(X+tlg)
            
    except Exception as E:
        print(E)
        
if __name__ == "__main__":
    while True:
        headers = get_headers(Country='US', Language='en')
        Email = GetNewEmail()
        print("\x1b[38;5;5m—" * 60)
        ss = Send_SMS(headers, Email)
        print(ss)
        
        if 'email_sent":true' in ss:
            code = GetMessage(Email)
            print("\x1b[38;5;5m—" * 60)
            a = Validate_Code(headers, Email, code)
            print(a.text)
            
            if 'status":"ok' in a.text:
                SignUpCode = a.json()['signup_code']
                Create_Acc(headers, Email, SignUpCode)
            else:
                print(a.text)
        else:
            pass
