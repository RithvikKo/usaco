with open('sleepy.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
starting=list(map(int,lines[1].split()))

result=n-1
#go through the cows and find how long the sorted suffix is
for i in range(n-2,-1,-1):
	if starting[i]<starting[i+1]:
		result=i
	else:
		break

with open('sleepy.out','w') as fout:
    fout.write(str(result)+'\n')
