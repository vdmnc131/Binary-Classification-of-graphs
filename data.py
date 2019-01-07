fil = open("data.txt")
elements = set()
graphids = set()
files = 0
for f in fil:
	if(len(f.split()) == 1):
		if("#" in f):
			graphids.add(f)
		else:
			if(ord(f[0]) - ord('0') > 9):
				elements.add(f[:len(f)-1])

count = 0
element = dict()
print len(elements)
for key in elements:
	print key, count
	count += 1

fil.close()

tgt = open("number_ids.txt", 'w')
tgt.write(str(len(graphids))+"\n")
tgt.close()