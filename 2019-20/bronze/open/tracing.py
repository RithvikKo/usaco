class Cow():
	def __init__(self,k):
		self.k=k
		self.infected=0

with open('tracing.in','r') as fin:
	lines=fin.readlines()

n,t=map(int,lines[0].split())
result=[int(i) for i in lines[1].strip()]
interactions=sorted([list(map(int,i.split())) for i in lines[2:]])
interactions=[[interaction[1]-1,interaction[2]-1] for interaction in interactions]

patient_zeros=lowest_k=highest_k=0
#iterate through infected cows
for i in [i for i in range(n) if result[i]]:
	found=False
	#iterate through possible values of k
	for k in range(1,t+1):
		cows=[Cow(k) for i in range(n)]
		cows[i].infected=1
		#simulate interactions
		for x,y in interactions:
			x_infected=cows[x].infected
			y_infected=cows[y].infected
			if x_infected:
				if cows[x].k>0:
					if not y_infected:
						cows[y].infected=1
					cows[x].k-=1
			if y_infected:
				if cows[y].k>0:
					if not x_infected:
						cows[x].infected=1
					cows[y].k-=1
		#check if cows equals the result and update lowest and highest k
		if [cow.infected for cow in cows]==result:
			if not found:
				patient_zeros+=1
				found=True
			if not lowest_k or k<lowest_k:
				lowest_k=k
			if highest_k!='Infinity':
				if k==t:
					highest_k='Infinity'
				else:
					highest_k=max(highest_k,k)

with open('tracing.out','w') as fout:
	fout.write(str(max(patient_zeros,1))+' '+str(lowest_k)+' '+str(highest_k)+'\n')
