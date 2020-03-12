import sys

ML, MR, TL, TR = input().split()
if TL == "S" and TR == "S":
	if ML == "R" or MR == "R":
		print("MS")
		sys.exit()
	if ML == "P" and MR == "P":
		print("TK")
		sys.exit()
elif TL == "R" and TR == "R":
	if ML == "P" or MR == "P":
		print("MS")
		sys.exit()
	if ML == "S" and MR == "S":
		print("TK")
		sys.exit()
elif TL == "P" and TR == "P":	
	if ML == "S" or MR == "S":
		print("MS")
		sys.exit()
	if ML == "R" and MR == "R":
		print("TK")
		sys.exit()
elif ML == "S" and MR == "S":
	if TL == "R" or TR == "R":
		print("TK")
		sys.exit()
	if TL == "P" and TR == "P":
		print("MS")
		sys.exit()
elif ML == "R" and MR == "R":
	if TL == "P" or TR == "P":
		print("TK")
		sys.exit()
	if TL == "S" and TR == "S":
		print("MS")
		sys.exit()
elif ML == "P" and MR == "P":	
	if TL == "S" or TR == "S":
		print("TK")
		sys.exit()
	if TL == "R" and TR == "R":
		print("MS")
		sys.exit()
print("?")