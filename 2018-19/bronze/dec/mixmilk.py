with open('mixmilk.in','r') as fin:
    lines=fin.readlines()

buckets=[list(map(int,line.split())) for line in lines]

#iterate through all pours
for i in range(100):
    first=i%3
    second=(i+1)%3
    if buckets[first][1]+buckets[second][1]>buckets[second][0]:
        buckets[first][1]-=buckets[second][0]-buckets[second][1]
        buckets[second][1]=buckets[second][0]
    else:
        buckets[second][1]+=buckets[first][1]
        buckets[first][1]=0

with open('mixmilk.out','w') as fout:
    for bucket in buckets:
        fout.write(str(bucket[1])+'\n')
