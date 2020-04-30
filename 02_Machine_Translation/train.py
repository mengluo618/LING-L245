import sys

#initialize dicitonary and list 
dic = {} 
vocabulary1 = [] 
vocabulary2 = []

#get the 2 input file
file1 = open(sys.argv[1]) 
file2 = open(sys.argv[2])

#read 2 file and put each word into two lists
while 1<2:
	s1 = file1.readline() 
	s2 = file2.readline()
	if s1 == '' or s2 == '':
		break
	vocabulary1 += s1.strip('\n').split(' ')
	vocabulary2 += s2.strip('\n').split(' ')

#read 2 lists, if the word not in dictionary, 
#add it in dictionary. If it is already in dictionary
#then check if the transfer word is in that dictionary
#if not, define it to 0. It looks like this word1:{word2 = 0}

for x in vocabulary1:
	if x.lower() not in dic:
		dic[x.lower()] = {}
	for y in vocabulary2:
		if y.lower() not in dic[x.lower()]:
			dic[x.lower()][y.lower()] = 0

#when we find transfered word, we add the combination by 1.	
z = 0
while z < len(vocabulary1):
	dic[vocabulary1[z].lower()][vocabulary2[z].lower()] += 1
	print(vocabulary1[z],"||",vocabulary2[z])
	z+=1

#In the end, we get the probability
for key1 in dic:
	for key2 in dic[key1]:
		prob = dic[key1][key2]/len(dic[key1])
		print("{:5f} {:s} {:s}".format(prob,key1,key2))
		
