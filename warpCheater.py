import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
os.system("title warpCheater")
os.system('cls' if os.name == 'nt' else 'clear')
print('                                              ______   __                              __                         '
'                                             /      \ /  |                            /  |                        \n'
' __   __   __   ______    ______    ______  /$$$$$$  |$$ |____    ______    ______   _$$ |_     ______    ______  \n'
'/  | /  | /  | /      \  /      \  /      \ $$ |  $$/ $$      \  /      \  /      \ / $$   |   /      \  /      \ \n'
'$$ | $$ | $$ | $$$$$$  |/$$$$$$  |/$$$$$$  |$$ |      $$$$$$$  |/$$$$$$  | $$$$$$  |$$$$$$/   /$$$$$$  |/$$$$$$  |\n'
'$$ | $$ | $$ | /    $$ |$$ |  $$/ $$ |  $$ |$$ |   __ $$ |  $$ |$$    $$ | /    $$ |  $$ | __ $$    $$ |$$ |  $$/ \n'
'$$ \_$$ \_$$ |/$$$$$$$ |$$ |      $$ |__$$ |$$ \__/  |$$ |  $$ |$$$$$$$$/ /$$$$$$$ |  $$ |/  |$$$$$$$$/ $$ |      \n'
'$$   $$   $$/ $$    $$ |$$ |      $$    $$/ $$    $$/ $$ |  $$ |$$       |$$    $$ |  $$  $$/ $$       |$$ |      \n'
 '$$$$$/$$$$/   $$$$$$$/ $$/       $$$$$$$/   $$$$$$/  $$/   $$/  $$$$$$$/  $$$$$$$/    $$$$/   $$$$$$$/ $$/       \n'
 '								   $$ |\n'                                                                            
 '								   $$ |\n'                                                                            
 '								   $$/\n'                                                                             )
print ("[+] Thanks for use our script.")
print ("[+] discord.gg/TRvwJhJDjD")
print ("--------")
referrer = input("[#] Enter the ID:")
def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)		    
def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))    
	except Exception as error:
		print(error)	
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run():
	try:
		install_id = genString(22)
		body = {"key": "{}=".format(genString(43)),
				"install_id": install_id,
				"fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
				"referrer": referrer,
				"warp_enabled": False,
				"tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
				"type": "Android",
				"locale": "es_ES"}
		data = json.dumps(body).encode('utf8')
		headers = {'Content-Type': 'application/json; charset=UTF-8',
					'Host': 'api.cloudflareclient.com',
					'Connection': 'Keep-Alive',
					'Accept-Encoding': 'gzip',
					'User-Agent': 'okhttp/3.12.1'
					}
		req         = urllib.request.Request(url, data, headers)
		response    = urllib.request.urlopen(req)
		status_code = response.getcode()	
		return status_code
	except Exception as error:
		print(error)	

g = 0
b = 0
while True:
	result = run()
	if result == 200:
		g = g + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		print("")
		print("                              warpCheater")
		print("")
		animation = ["[■□□□□□□□□□] 10%","[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"] 
		for i in range(len(animation)):
			time.sleep(1)
			sys.stdout.write("\r[+] Preparing... " + animation[i % len(animation)])
			sys.stdout.flush()
		print(f"\n[-] WORKING ON ID: {referrer}")    
		print(f"[:)] {g} GB has been successfully added to your account.")
		print(f"[#] Total: {g} Good {b} Bad")
		print("[*] After 9 seconds, a new request will be sent.")
		time.sleep(9)
	else:
		b = b + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		print("")
		print("                              warpCheater")
		print("")
		print("[:(] Error when connecting to server. Waiting 10 seconds...")
		print(f"[#] Total: {g} Good {b} Bad")
		time.sleep(10)	

  