import requests
import os

r = requests.session()

def cls_(): # thx stackoverflow or no because idek if this work or not
    os.system('cls' if os.name=='nt' else 'clear')

def getIpu():
	ipu = r.get("http://apims.doe.gov.my/data/public_v2/CAQM/last24hours.json") # get ipu data
	info = ipu.json()['24hour_api_apims'] # set info to requested ipu data (json)

	for x in range(len(info)): # loop to write all of the State and location
		if x > 0:
			print(str(x), "| State:", info[x][0], "->",info[x][1])
			pass

	print('_______________________')
	print('Enter your States Code')
	code = input('> ') # ask for input
	return code,info # return the code and the requested ipu data so you dont need to request it again

def printInfo(stateData,stateNumber): # print state info by user input (code)
	try:	
		cls_()
		print("____________________")

		data = stateData
		code = int(stateNumber)

		for x in range(len(data[code])):
			print(data[0][x], ":", data[code][x])
			pass

		print("____________________")
		exitP = input("Press Enter to Exit")

	# Error Handling start here
	except IndexError:
		print("Make sure the number isn't bigger than state code")
		exitP = input("Press Enter to Exit")
	except ValueError:
		print('Enter a number you dumbass')
		exitP = input("Press Enter to Exit")




ipuCode,ipuData = getIpu()
printInfo(ipuData,ipuCode)
