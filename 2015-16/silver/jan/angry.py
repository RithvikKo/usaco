#calculate if r is enough to explode all of the hay bales
def enough(r):
	global bales
	global n
	global k
	start=bales[0]
	used=1
	for i in range(1,n):
		if bales[i]>start+2*r:
			used+=1
			if used>k:
				return False
			else:
				start=bales[i]
	return True

#binary search for the smallest r
def bs():
	l=0
	r=5e8;
	while l<r:
		m=(l+r)//2
		if enough(m):
			r=m
		else:
			l=m+1
	return l

with open('angry.in','r') as fin:
    lines=fin.readlines()

n,k=map(int,lines[0].split())
bales=sorted([int(line) for line in lines[1:]])

with open('angry.out','w') as fout:
    fout.write(str(bs())+'\n')
