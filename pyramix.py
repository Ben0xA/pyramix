import random
import operator

# variable declaration

lx = [16,24,30,34,36,36]
rx = [125,226,327,428,529,630]
ri = [20,12,6,2,0,0]
cst = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
lpt = "122033300444400055555000066666600000"
rpt = "606500654000654300006543200000654321"
rst = "102200333000444400005555500000666666"
spc = "XQ"
txt = ""

def getxy(letter, left=True):
	idx = cst.find(letter)
	rtn = "000"
	
	lindex = int(lpt[cst.find(letter)]) -1
	if lindex > -1 and left:
		rtn = str(lx[lindex] + cst.find(letter)).zfill(3)
	else:
		lindex = int(rpt[cst.find(letter)]) -1
		if lindex > -1:
			rtn = str(int(rx[lindex]) - int(ri[int(rst[cst.find(letter)])-1]) + cst.find(letter)).zfill(3)
		else:
			lindex = int(lpt[cst.find(letter)]) -1
			if lindex > -1:
				rtn = str(lx[lindex] + cst.find(letter)).zfill(3)
	return rtn

def encipher(txt, add=0):
	global spc
	ct = ""
	txt = txt.replace(" ", spc).upper()
	lr = False
	for idx in range(len(txt)):
		nr = random.randint(0,10)
		lr = bool(operator.mod(nr,2)) 
		ct += getxy(txt[idx],lr)

	if add > 3:
		add = 3

	if 0 < add <= 3:
		newct = ""
		for adt in range(len(ct)):
			newct += str(int(ct[adt]) + add)
			#newct += str(int(ct[adt]))
		ct = newct

	rx = ""
	yy = ""
	lx = ""
	for tnp in range(0, len(ct), 3):
		rx += ct[tnp]
		yy += ct[tnp + 1]
		lx += ct[tnp + 2]

	ct = rx + yy + lx
	return ct

def mnuencipher():
	global txt
	enctext = raw_input("Enter the text to encipher: ")
	enctext = enctext.upper()
	for spl in enctext:
		if spl != " ":
			if spl in cst:
				txt += spl
		else:
			txt += spl
	
	print "\nEnciphered text: " + encipher(txt, random.randint(1,3)) + "\n"
	raw_input("Press enter to continue.")

def getletter(idx):
	lid = int(str(idx)[0]) - 1
	sid = 0
	rtn = ""

	if idx > 66:
		sid = int(str(idx)[1]) - 1
		rtn = cst[idx - (int(rx[lid]) - int(ri[sid]))]
	else:
		rtn = cst[idx - int(lx[lid])]

	return rtn

def decipher(ct):
	global spc
	rtn = ""
	if ct.find("0") == -1:
		lowest = 9
		for li in range(len(ct)):
			if int(ct[li]) < lowest:
				lowest = int(ct[li])

		newct = ""
		for ls in range(len(ct)):
			newct += str(int(ct[ls]) - lowest)

		ct = newct
	
	ctlen = len(ct) / 3
	ctidx = 0
	lx = ""
	yy = ""
	rx = ""
	lx = ct[ctidx:ctlen]
	ctidx += ctlen
	yy = ct[ctidx:ctlen * 2]
	ctidx += ctlen
	rx = ct[ctidx:ctlen * 3]

	cttran = ""
	for cti in range(len(lx)):
		cttran += lx[cti]
		cttran += yy[cti]
		cttran += rx[cti]
	ct = cttran

	clen = 0
	for idx in range(0, len(ct), 3):
		clen += 3
		rtn += getletter(int(ct[idx:clen]))

	if spc != "":
		rtn = rtn.replace(spc, " ")

	return rtn

def mnudecipher():
	dectext = raw_input("Enter the text to decipher: ")
	dectext = dectext.upper()
	if dectext.isdigit():
		print "\nDeciphered text: \n" + decipher(dectext) + "\n"
	else:
		print "Invalid cipher text. Please verify and try again."
	raw_input("Press enter to continue.")

def mnushowsett():
	print "Character Set: " + cst
	print "Space String: " + spc
	print "\n" + "Pryamix".center(17) + "\n"

	print str("1|" + cst[0] + "|1").center(17)
	print str("2|" + cst[1:4] + "|2").center(17)
	print str("3|" + cst[4:9] + "|3").center(17)
	print str("4|" + cst[9:16] + "|4").center(17)
	print str("5|" + cst[16:25] + "|5").center(17)
	print str("6|" + cst[25:36] + "|6").center(17)
	print "-----------".center(17)
	print "12345654321".center(17) + "\n"
	raw_input("Press enter to continue.")

def mnuchgchars():
	global cst
	print "Current Character Set: " + cst
	tstr = raw_input("Enter the new character set (36 chars, no space): ")
	if len(tstr) == 36:
		cst = tstr
		print "New character set: " + cst
	else:
		print "Invalid character set."
	raw_input("Press enter to continue.")

def mnuchgspace():
	global spc
	print "Current Space String: " + spc
	tspc = raw_input("Enter the new space string (2 to 3 chars, no space): ")
	if len(tspc) <= 3:
		spc = tspc
		print "New space string: " + spc
	else:
		print "Invalid space string."
	raw_input("Press enter to continue.")

def mnunull():
	print "That is not an option."
	raw_input("Press enter to continue.")


def main():
	global txt
	menu = {
		0:mnunull,
		1:mnuencipher,
		2:mnudecipher,
		3:mnushowsett,
		4:mnuchgchars,
		5:mnuchgspace,		
	}
	rsp = 0
	print "Praymix Cipher"
	print "Cipher & Program written by Ben0xA"
	while rsp != 99:
		txt = ""
		print "\nMenu:"
		print "1. Encipher"
		print "2. Decipher"
		print "3. Show Cipher Settings"
		print "4. Change Character Set"
		print "5. Change Space String"
		print "99. Exit\n"
		print ""
		irsp = raw_input("Choose an option: ")
		if irsp.isdigit():
			rsp = int(irsp)
			if rsp!= 99:
				menu.get(rsp, mnunull)()


if __name__ == "__main__":
    main()
