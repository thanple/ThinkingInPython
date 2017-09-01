a=5

def get_int(msg):
	try:
		i=int(input(msg))
		return i
	except ValueError as err:
		print ("Exception:",err)
		return;