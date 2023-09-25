# This Script is used to check how many time a password has been sceen in data breaches.
# To use run the script in a shell with a path to a text file that stores your passwords.
# Example -- python3 script.py pass.txt

import hashlib, requests , sys

def makeAPIrequest(head): 
	response = requests.get('https://api.pwnedpasswords.com/range/'+ head)
	responseList = response.text.splitlines()
	return(responseList)

def getConvertsplit(passwords):
	for password in passwords:
		hashedPaswd = hashlib.sha1(password.strip().encode('utf-8')).hexdigest()
		prefix = hashedPaswd[:5]
		suffix = hashedPaswd[5:]
		responseArray = makeAPIrequest(prefix)
		mainEngine(responseArray, suffix)


def mainEngine(hashlist, suffix):
	for hashes in hashlist:
		head, tail = hashes.split(':')
		if head == suffix.upper():
			count = int(tail)
			break
		else:
			count = 0
	return(finish(count))


def useText():
	filename = sys.argv[1]
	passfile = open(filename, 'r')
	passfilelist = passfile.readlines()
	return(getConvertsplit(passfilelist))



def finish(count):
	if count > 0:
		print (f'Not Good!!! Your password appered {count} times. Please for the love of God use a better one :)')
	else:
		print(f'Good Job! Your password hasn\'t been hacked yet ')


useText()
