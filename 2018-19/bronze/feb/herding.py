with open('herding.in','r') as fin:
    lines=fin.readlines()

cows=list(map(int,lines[0].split()))
distances=[cows[1]-cows[0],cows[2]-cows[1]]

if distances[0]==1 and distances[1]==1:
    min_moves=0
    max_moves=0
else:
    if distances[0]==2 or distances[1]==2:
        min_moves=1
    else:
        min_moves=2
    if distances[0]>distances[1]:
        max_moves=distances[0]-1
    else:
        max_moves=distances[1]-1

with open('herding.out','w') as fout:
    fout.write(str(min_moves)+'\n')
    fout.write(str(max_moves)+'\n')
