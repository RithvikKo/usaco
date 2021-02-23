import copy

with open('mowing.in','r') as fin:
    lines=fin.readlines()

lines=[line.strip() for line in lines]
n=int(lines[0])
pattern=[[line.split()[0],int(line.split()[1])] for line in lines[1:]]

result=-1
cell=[0,0]
mowed=[copy.deepcopy(cell)]
time=1
#iterate through each step of the pattern
for line in pattern:
    if line[0]=='N':
        x,y=0,1
    elif line[0]=='E':
        x,y=1,0
    elif line[0]=='W':
        x,y=-1,0
    else:
        x,y=0,-1
    #iterate through every cell in the step
    for _ in range(1,line[1]+1):
        cell[0]+=x
        cell[1]+=y
        #check if cell was already mowed
        if cell in mowed:
            if result==-1:
                result=time-(time-1-mowed[::-1].index(cell))
            else:
                result=min(result,time-(time-1-mowed[::-1].index(cell)))
        mowed.append(copy.deepcopy(cell))
        time+=1

with open('mowing.out','w') as fout:
    fout.write(str(result)+'\n')
