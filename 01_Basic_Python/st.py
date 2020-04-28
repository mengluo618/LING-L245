import sys

vocab = {} # dict to store frequency list

for line in sys.stdin.readlines(): 
    # the form is the line without spacing
    form = line.strip()
    if form not in vocab:
        vocab[form] = 0
    vocab[form] = vocab[form] + 1

"""
After combining this with the sed command and the sort -d to get the alphabetical oder,
I'm trying to combine this the frequency data structure to get results
"""
freq = []

for w in vocab:
    freq.append((vocab[w], w))

freq.sort(reverse=True)

for w in freq:
    print('%d\t%s' % (w[0], w[1]))

fd = open('freq.txt', 'w+')
for w in vocab:
    fd.write('%d\t%s\n' % (vocab[w], w))

fd.close()  
