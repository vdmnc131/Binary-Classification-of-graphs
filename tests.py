fil = open("testset.txt")
count = 0
for f in fil:
	if("#" in f):
		count += 1
print count
