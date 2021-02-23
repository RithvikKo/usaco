with open('diamond.in','r') as fin:
	lines=fin.readlines()

n,k=map(int,lines[0].split())
diamonds=sorted(list(map(int,lines[1:])))

result=0
#iterate through all diamonds
for i in range(n):
	#search for all diamonds that are greater than or equal to the current diamond and less than or equal to k
	for j in range(i+1,n):
		if diamonds[j]-diamonds[i]>k:
			break
		elif j==n-1:
			j+=1
			break
	result=max(result,j-i)

with open('diamond.out','w') as fout:
	fout.write(str(result)+'\n')
