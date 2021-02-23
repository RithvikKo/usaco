with open('photo.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
b=list(map(int,lines[1].split()))

#iterate through all possible first elements of a
for i in range(1,b[0]):
	result=[i]
	found=True
    #iterate through b, subtracting each element in b by each element in a to get the next element in a
	for cow in b:
		current=cow-result[-1]
        #a is wrong if current element is already in a or below or equal to zero
		if current in result or current<1:
			found=False
			break
		result.append(current)
	if found:
		break

with open('photo.out','w') as fout:
	fout.write(' '.join(map(str,result))+'\n')
