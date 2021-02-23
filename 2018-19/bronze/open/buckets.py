with open('buckets.in','r') as fin:
    lines=fin.readlines()

farm=[[square for square in line] for line in lines]

#locate barn, lake, and rock
for i in range(10):
    for j in range(10):
        if farm[i][j]=='B':
            barn=[i,j]
        elif farm[i][j]=='L':
            lake=[i,j]
        elif farm[i][j]=='R':
            rock=[i,j]

#shortest path between the barn and the lake is the sum of the differences between their x and y
result=abs(barn[0]-lake[0])+abs(barn[1]-lake[1])-1
#have to go around the rock if it is between the barn and the lake
if (barn[0]==lake[0]==rock[0] and (barn[1]<rock[1]<lake[1] or lake[1]<rock[1]<barn[1])) or (barn[1]==lake[1]==rock[1] and (barn[0]<rock[0]<lake[0] or lake[0]<rock[0]<barn[0])):
    result+=2

with open('buckets.out','w') as fout:
    fout.write(str(result)+'\n')
