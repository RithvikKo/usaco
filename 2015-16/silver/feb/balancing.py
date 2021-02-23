class Cow:
	def __init__(self,x,y):
		self.x=x
		self.y=y

with open('balancing.in','r') as fin:
	lines=fin.readlines()

n=int(lines[0])
cows=[Cow(*map(int,line.split())) for line in lines[1:]]
#sort cows by x and y
sorted_x=sorted(cows,key=lambda c:c.x)
sorted_y=sorted(cows,key=lambda c:c.y,reverse=True)

#find all valid vertical fence positions
x=list({cow.x+1 for cow in sorted_x})
result=1000
for a in x:
	quadrants=[0]*4
	#calculate how many cows are in each quadrant
	for cow in cows:
		if cow.x>a:
			quadrants[3]+=1
		else:
			quadrants[2]+=1
	#update the quadrants for each cow
	for cow in sorted_y:
		if cow.x>a:
			quadrants[0]+=1
			quadrants[3]-=1
		else:
			quadrants[1]+=1
			quadrants[2]-=1
		result=min(result,max(quadrants))

with open('balancing.out','w') as fout:
	fout.write(str(result)+'\n')
