import sys
  
dic = {}
vocabulary1 = []
vocabulary2 = []
file1 = open(sys.argv[1])

#get the highest probability of the word combination.
for line in file1.readlines():
	prob = line.strip('\n').split(' ')[0]
	word1 =line.strip('\n').split(' ')[1]
	word2 =line.strip('\n').split(' ')[2]
	word1 = word1.strip()
	word2 = word2.strip()
	if word1 not in dic:
		dic[word1] = (prob,word2)
	if word1 in dic and prob > dic[word1][0]:
		dic[word1] = (prob,word2)

#get the input content
content = sys.stdin.read()

#transfer the word
word = content.strip().split()
for x in word:
	if x.lower() in dic:
		print(dic[x.lower()][1],end =' ')
	else:
		print("*"+x+' ' , end = ' ')
