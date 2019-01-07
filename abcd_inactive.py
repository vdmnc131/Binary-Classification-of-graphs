import os
fil = open("input_inactive.txt.fp")
file = open("num_lines_inactive.txt")
num_active = int(next(file))
count = 0
while(count < num_active):
	f = open("temporary_inactive/input_"+str(count)+".txt", 'w')
	count+=1
	try:
		x = next(fil)
	except:
		break
	while("x" not in x):
		f.write(x)
		x = next(fil)
	x = next(fil)
