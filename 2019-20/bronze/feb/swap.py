import copy

#cows after one routine
def routine(cows):
	global a
	global b
	cows[a[0]-1:a[1]]=cows[a[1]-1:a[0]-2:-1]
	cows[b[0]-1:b[1]]=cows[b[1]-1:b[0]-2:-1]
	return cows

with open('swap.in','r') as fin:
    lines=fin.readlines()

n,k=map(int,lines[0].split())
a=list(map(int,lines[1].split()))
b=list(map(int,lines[2].split()))

initial=list(range(1,n+1))
cows=routine(copy.deepcopy(initial))
reset=1
#find amount of routines until cows return to initial order
while cows!=initial:
    cows=routine(cows)
    reset+=1

#do routine k mod amount of rountines until cows return to initial order times
for _ in range(k%reset):
    cows=routine(cows)

with open('swap.out','w') as fout:
    fout.write('\n'.join(map(str,cows))+'\n')
