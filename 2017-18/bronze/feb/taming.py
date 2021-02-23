with open('taming.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
entries=list(map(int,lines[1].split()))

consistent=False
#check if first day is consistent
if entries[0]<1:
	entries[0]=0
	consistent=True
	#iterate through all days backwards
	for i in range(n-2,0,-1):
		if entries[i]==-1:
			#fill in entry if we know the previous entry
			if entries[i+1]>0:
				entries[i]=entries[i+1]-1
		else:
			#check if entry is consistent
			if entries[i+1]>0 and entries[i+1]!=entries[i]+1:
				consistent=False
				break
	if consistent:
		result=entries.count(0)

with open('taming.out','w') as fout:
	if consistent:
		fout.write(str(result)+' '+str(result+entries.count(-1))+'\n')
	else:
	    fout.write('-1\n')
