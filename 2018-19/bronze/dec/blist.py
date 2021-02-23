with open('blist.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
cows=sorted([list(map(int,line.split())) for line in lines[1:]])
start=min([cow[0] for cow in cows])
end=max([cow[1] for cow in cows])

buckets=0
result=0
#greedily search for the maxiumum number of buckets by iterating through start and end times
for i in range(start,end+1):
    #find if cows start or end and add or remove buckets accordingly
    for cow in cows:
        if cow[0]==i:
            buckets+=cow[2]
        elif cow[1]==i:
            buckets-=cow[2]
    result=max(result,buckets)

with open('blist.out','w') as fout:
    fout.write(str(result)+'\n')
