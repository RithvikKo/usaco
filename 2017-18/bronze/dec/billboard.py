with open('billboard.in','r') as fin:
    lines=fin.readlines()

billboards=[list(map(int,line.split())) for line in lines[:2]]
truck=list(map(int,lines[2].split()))

result=0
#calculate area that remains visible for each billboard
for billboard in billboards:
    result+=(billboard[2]-billboard[0])*(billboard[3]-billboard[1])-max(0,min(billboard[2],truck[2])-max(billboard[0],truck[0]))*max(0,min(billboard[3],truck[3])-max(billboard[1],truck[1]))

with open('billboard.out','w') as fout:
    fout.write(str(result)+'\n')
