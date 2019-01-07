import os
from multiprocessing import Process, Array

def getPos(i, j):
	return i*num_features + j

def active(start, end, lines_active, num_features, array, id):
	for j in xrange(start, end):
		for x in xrange(3):
			array[getPos(j, x)] = 0
		strg = tests[j]
		s1 = len(strg)
		for i in xrange(3, lines_active):
			temp = open("temp_a"+str(id)+".txt", 'w')
			data = active_graph[i]
			temp.write(strg+data)
			temp.close()
			s2 = len(data)
			os.popen("./gSpan-64 -f temp_a"+str(id)+".txt -s 1 -o")
			file = open("temp_a"+str(id)+".txt.fp")
			if(len(file.read()) > min(s1,s2)):
				array[getPos(j, i)] = 1
			else:
				array[getPos(j, i)] = 0

def inactive(start, end, lines_active, num_features, array, id):
	for j in xrange(start, end):
		strg = tests[j]
		s1 = len(strg)
		for x in xrange(lines_active, lines_active+8):
			array[getPos(j, x)] = 0
		for i in xrange(lines_active+3, num_features):
			temp = open("temp_i"+str(id)+".txt", 'w')
			data = inactive_graph[i-lines_active]
			temp.write(strg+data)
			temp.close()
			s2 = len(data)
			os.popen("./gSpan-64 -f temp_i"+str(id)+".txt -s 1 -o")
			file = open("temp_i"+str(id)+".txt.fp")
			if(len(file.read()) > min(s1,s2)):
				array[getPos(j, i)] = 1
			else:
				array[getPos(j, i)] = 0

if __name__ == "__main__":
	num_tests = open("num_tests.txt")
	num_test = int(next(num_tests))
	num_lines_active = open("num_lines_active.txt")
	lines_active = int(next(num_lines_active))
	num_lines_inactive = open("num_lines_inactive.txt")
	lines_inactive = int(next(num_lines_inactive))
	num_features = lines_active + lines_inactive
	array = [[0 for x in xrange(num_features)] for x in xrange(num_test)]

	active_graph = []
	inactive_graph = []
	tests = []

	for i in xrange(lines_active):
		g = open("temporary_active/input_"+str(i)+".txt")
		data = os.read(g.fileno(), 65536)
		active_graph.append(data)

	for i in xrange(lines_active, num_features):
		g = open("temporary_inactive/input_"+str(i-lines_active)+".txt")
		data = os.read(g.fileno(), 65536)
		inactive_graph.append(data)

	fil = open("test_data.txt")
	file = open("num_tests.txt")
	num_active = int(next(file))
	count = 0
	x = next(fil)
	while(count < num_active):
		over = ""
		count+=1
		while(True):
			over+=x
			try:
				x = next(fil)
			except:
				break
			if("t" in x):
				break
		tests.append(over)

	array = Array('i', range(num_features*num_test))
	p1 = Process(target=active, args=(0, num_test/4, lines_active, num_features, array, 1))		
	p2 = Process(target=active, args=(num_test/4, num_test/2, lines_active, num_features, array, 2))
	p3 = Process(target=active, args=(num_test/2, 3*num_test/4, lines_active, num_features, array, 3))		
	p4 = Process(target=active, args=(3*num_test/4, num_test, lines_active, num_features, array, 4))	
	q1 = Process(target=inactive, args=(0, num_test/4, lines_active, num_features, array, 1))
	q2 = Process(target=inactive, args=(num_test/4, num_test/2, lines_active, num_features, array, 2))
	q3 = Process(target=inactive, args=(num_test/2, 3*num_test/4, lines_active, num_features, array, 3))
	q4 = Process(target=inactive, args=(3*num_test/4, num_test, lines_active, num_features, array, 4))
	p1.start()
	p2.start()
	q1.start()
	q2.start()
	p3.start()
	p4.start()
	q3.start()
	q4.start()

	p1.join()
	p2.join()
	q1.join()
	q2.join()
	p3.join()
	p4.join()
	q3.join()
	q4.join()
	for i in xrange(num_test):
		for j in xrange(num_features):
			print str(j)+":"+str(array[getPos(i, j)]),
		print ""
