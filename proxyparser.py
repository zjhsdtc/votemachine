file = open('proxylist', 'r')
for line in file.readlines():
	if 'HTTP' in line:
		print str(line.split('HTTP')[0].strip())
file.close()
