input = open('index.txt', 'r')
fp = open("index_num.txt", 'w')

all_the_text =input.read( )

li=all_the_text.split()
for x in range(0,len(li),2):
	print x
	print li[x]
	fp.write(li[x]+' ')

fp.close()
input.close()