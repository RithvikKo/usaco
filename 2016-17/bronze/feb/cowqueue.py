with open('cowqueue.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
cows=sorted([list(map(int,line.split())) for line in lines[1:]])

time=0
#iterate through all cows and simulate the queue
for cow in cows:
    if time>cow[0]:
        time+=cow[1]
    else:
        time=sum(cow)

with open('cowqueue.out','w') as fout:
    fout.write(str(time)+'\n')
