import os
# test = open("tests.txt")
fil = open("input_active.txt.fp")
file = open("num_lines_active.txt")
num_active = int(next(file))
# for t in test:
count = 0
while(count < num_active):
	f = open("temporary_active/input_"+str(count)+".txt", 'w')
	count+=1
	x = next(fil)
	while("x" not in x):
		f.write(x)
		x = next(fil)
	x = next(fil)
