import sys

vocab = [] #vocab is a list of valid word forms

f = open('freq.txt', 'r')
#get the valid word
for line in f.readlines(): 
	line = line.strip('\n ')
	(x,y) = line.split('\t')
	vocab.append(y)

#get the input
for line in sys.stdin.readlines(): 
	w = line.split(' ') 
	#get each token
	for key in w :
		if key.isalpha(): 
			if key not in vocab :
				sys.stdout.write('*'+key+' ')
			else :
				sys.stdout.write(key+' ')
		else:
			sys.stdout.write(key+' ')
