with open('revegetate.in','r') as fin:
    lines=fin.readlines()

n,m=map(int,lines[0].split())
favorites=[list(map(int,line.split())) for line in lines[1:]]

pastures=[0]*n
#iterate through every pasture
for i in range(n):
    adjacent=set()
    #find adjacent pastures that cannot have the same grass type
    for favorite in favorites:
        for j in range(2):
            if favorite[j]==i+1:
                adjacent.add(pastures[favorite[1-j]-1])
    #plant unused first grass type
    for j in range(1,5):
        if j not in adjacent:
            pastures[i]=j
            break

with open('revegetate.out','w') as fout:
    for pasture in pastures:
        fout.write(str(pasture))
    fout.write('\n')
