#return smallest gap when adding two cows in largest gap
def same(largest,first,last):
	return max([(largest-2)//3,(first-2)//2,(last-2)//2])

#return smallest gap when adding one cow in each of the two largest gaps
def different(largest,second_largest,first,last):
	return min(sorted([(largest-1)//2,(second_largest-1)//2,first-1,last-1])[-2:])

with open('socdist1.in','r') as fin:
	lines=fin.readlines()

n=int(lines[0])
stalls=[int(i) for i in lines[1].strip()]

occupied=stalls.count(1)
smallest=int(1e5)
if occupied:
	if occupied==1:
		first=last=stalls.index(1)
		second_largest,largest=sorted([first,n-1-last])
	else:
		#calculate first and last stalls with cows
		first=stalls.index(1)
		last=n-1-stalls[::-1].index(1)

		largest=second_largest=current=0
		#iterate through first and last stalls with cows and greedily search for the two largest gaps and the smallest gap
		for i in range(first+1,last+1):
			if stalls[i]:
				smallest=min(smallest,current)
				if current>largest:
					second_largest=largest
					largest=current
				elif current>second_largest:
					second_largest=current
				current=0
			else:
				current+=1

	result=min(smallest,different(largest,second_largest,first,n-1-last))
	if largest>1:
		result=max(result,min(smallest,same(largest,first,n-1-last)))
else:
	result=n-2

with open('socdist1.out','w') as fout:
	fout.write(str(result+1)+'\n')
