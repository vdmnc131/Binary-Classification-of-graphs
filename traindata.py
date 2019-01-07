num_lines_active = open("num_lines_active.txt")
lines_active = int(next(num_lines_active))
num_lines_inactive = open("num_lines_inactive.txt")
lines_inactive = int(next(num_lines_inactive))
num_features = lines_active + lines_inactive

num_actives = open("parsed_active.txt")
num_active = int(next(num_actives))
num_inactives = open("parsed_inactive.txt")
num_inactive = int(next(num_inactives))

array = [[0 for x in xrange(num_features)] for x in xrange(num_active+num_inactive)]

# for j in xrange(num_lines_active):
fil = open("input_active.txt.fp")
count = 0
flag = False
while(True):
	x = ""
	while("x" not in x):
		try:
			x = next(fil)
		except:
			flag = True
			break
	if(flag):
		break
	# print lin
	lin = [int(k) for k in x[1:].split()]
	for l in lin:
		array[l][count] = 1
	count += 1
	try:
		x = next(fil)
	except:
		break


# for j in xrange(num_lines_active, num_features):
fil = open("input_inactive.txt.fp")
count = 0
flag = False
while(True):
	x = ""
	while("x" not in x):
		try:
			x = next(fil)
		except:
			flag = True
			break
	if(flag):
		break
	lin = [int(k) for k in x[1:].split()]
	# print lin
	for l in lin:
		array[l+num_active][count+lines_active] = 1
	count += 1
	try:
		x = next(fil)
	except:
		break

for i in xrange(num_active):
	print 0,
	for j in xrange(num_features):
		print str(j)+":"+str(array[i][j]),
	print ""

for i in xrange(num_active, num_inactive+num_active):
	print 1,
	for j in xrange(num_features):
		print str(j)+":"+str(array[i][j]),
	print ""