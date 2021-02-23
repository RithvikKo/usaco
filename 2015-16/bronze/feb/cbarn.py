with open('cbarn.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
rooms=list(map(int,lines[1:]))

result=None
#iterate through every starting room
for i in range(n):
    total=0
    path=rooms[i:]+rooms[:i]
    #determine the total distance that all cows need to walk
    for j in range(n):
        total+=j*path[j]
    if result==None:
        result=total
    else:
        result=min(result,total)

with open('cbarn.out','w') as fout:
    fout.write(str(result)+'\n')
