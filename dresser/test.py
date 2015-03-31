

def main():
	print int(dieGameHelp(55)*10000)


def dieGameHelp(rolls):
	if rolls == 1:
		return 3.5
	if rolls > 1:
		temp1 = dieGameHelp(rolls-1)
		temp = 6 - int(temp1)
		return ((6 + (7-temp)) * temp/2 + (6-temp) * temp1)/6



	
if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print "\n"
		exit()
	