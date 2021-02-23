with open('planting.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
pathways=[list(map(int,line.split())) for line in lines[1:]]

adjacent={field:0 for field in range(1,n+1)}
#count how many fields are adjacent to each field
for pathway in pathways:
    adjacent[pathway[0]]+=1
    adjacent[pathway[1]]+=1

with open('planting.out','w') as fout:
    fout.write(str(max(adjacent.values())+1)+'\n')
