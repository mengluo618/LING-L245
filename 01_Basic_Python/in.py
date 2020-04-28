fd = open('freq.txt', 'w+')
for w in vocab:
    fd.write('%d\t%s' % (vocab[w], w))
fd.close()
