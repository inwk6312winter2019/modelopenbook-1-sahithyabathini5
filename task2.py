import math
def list_ifname_ip():
	myfile = open('running-config.cfg')
	nameifdict=dict()
	for line in myfile:
		if "nameif" in line:
			mytemplist = line.split()
			next(myfile)
			templine = next(myfile)
			mylist= templine.split()
		if mytemplist[0]=='nameif':
		if mylist[0] == 'ip':
                    mylist=mylist[2:]
		for item in mylist:
		     firstoctect = item[0]+item[1]+item[2]
		if (firstoctect == 172) or (firstoctect == 192):
		return nameifdict



ipconfigs = list_ifname_ip()
print(ipconfigs)

