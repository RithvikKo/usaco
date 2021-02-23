import copy

with open('milkorder.in','r') as fin:
    lines=fin.readlines()

n,m,k=map(int,lines[0].split())
hierarchy=list(map(int,lines[1].split()))
positions={int(line.split()[0]):int(line.split()[1]) for line in lines[2:]}

initial=[None]*n
#fix cows with preferred order
for cow,position in positions.items():
    initial[position-1]=cow

#iterate through all positions and place first cow in every position
if 1 in hierarchy:
	possible=[i for i in range(hierarchy.index(1),n) if initial[i]==None]
else:
	possible=[i for i in range(n) if initial[i]==None]
for i in possible:
    order=copy.deepcopy(initial)
    order[i]=1
    valid=True
    #iterate through all cows in the hierarchy
    for j in [i for i in range(m) if hierarchy[i] not in order]:
        valid=False
        #find the index of previous cow and next cow
        if j:
            previous=order.index(hierarchy[j-1])+1
        else:
            previous=0
        if j==m-1 or hierarchy[j+1] not in order:
            next=n
        else:
            next=order.index(hierarchy[j+1])
        #add cow to the first empty position between previous and next cow
        for k in range(previous,next):
            if order[k]==None:
                order[k]=hierarchy[j]
                valid=True
                break
        #if cow was not added then break
        if not valid:
            break
    #break if valid order is found or if first cow is in last position
    if valid:
        result=i+1
        break

with open('milkorder.out','w') as fout:
    fout.write(str(result)+'\n')
