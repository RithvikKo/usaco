import copy

#calculates border cows and their indexes
def _borders(cows):
    borders=[1,40000,1,40000]
    indexes=[None]*4
    for i,cow in enumerate(cows):
        if cow[1]>borders[0]:
            borders[0]=cow[1]
            indexes[0]=i
        if cow[1]<borders[1]:
            borders[1]=cow[1]
            indexes[1]=i
        if cow[0]>borders[2]:
            borders[2]=cow[0]
            indexes[2]=i
        if cow[0]<borders[3]:
            borders[3]=cow[0]
            indexes[3]=i
    return borders,indexes

#calculates the area of the rectangle formed by the border cows
def area(borders):
    return (borders[0]-borders[1])*(borders[2]-borders[3])

with open('reduce.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
cows=[list(map(int,line.split())) for line in lines[1:]]

borders,indexes=_borders(cows)
result=1599920002
#iterate through border cows
for i in indexes:
    temp=copy.deepcopy(cows)
    del temp[i]
    temp_borders,temp_indexes=_borders(temp)
    result=min(result,area(temp_borders))

with open('reduce.out','w') as fout:
    fout.write(str(result)+'\n')
