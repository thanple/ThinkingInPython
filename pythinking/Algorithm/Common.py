def exchange(data,i,j):
	if(i!=j):
		temp = data[i]
		data[i] = data[j]
		data[j] = temp