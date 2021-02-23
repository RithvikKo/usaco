with open('crossroad.in','r') as fin:
    lines=fin.readlines()

lines=[line.strip() for line in lines]
n=int(lines[0])
observations=[list(map(int,line.split())) for line in lines[1:]]

result=0
crossings={}
#iterate through all observations and keep track of when they cross the road
for observation in observations:
    if observation[0] not in crossings:
        crossings[observation[0]]=observation[1]
    elif observation[1]!=crossings[observation[0]]:
        result+=1
        crossings[observation[0]]=observation[1]

with open('crossroad.out','w') as fout:
    fout.write(str(result)+'\n')
