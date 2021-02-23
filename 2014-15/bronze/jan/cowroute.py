with open('cowroute.in','r') as fin:
    lines=fin.readlines()

a,b,n=map(int,lines[0].split())
cost=[]
cities=[]
for i in range(1,2*n,2):
	cost.append(int(lines[i].split()[0]))
	cities.append(list(map(int,lines[i+1].split())))

#iterate through all routes and greedily search for the best route
result=-1
for i in range(n):
	if a in cities[i] and b in cities[i] and cities[i].index(b)>cities[i].index(a):
		if result==-1:
			result=cost[i]
		else:
			result=min(result,cost[i])

with open('cowroute.out','w') as fout:
    fout.write(str(result)+'\n')
