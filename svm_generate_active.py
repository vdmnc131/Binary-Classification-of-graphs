fil = open("input_active.txt.fp")
count = 0
for f in fil:
	if ("t" in f):
		count += 1
print count