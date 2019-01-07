fil = open("test_data.txt")
file = open("num_tests.txt")
num_active = int(next(file))
count = 0
x = next(fil)
while(count < num_active):
	f = open("tests/test_"+str(count)+".txt", 'w')
	count+=1
	while(True):
		f.write(x)
		try:
			x = next(fil)
		except:
			break
		if("t" in x):
			break
