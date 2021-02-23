import itertools

with open('triangles.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
posts=[list(map(int,line.split())) for line in lines[1:]]

result=0
#check all post combinations
for combo in itertools.combinations(posts,3):
    x=None
    y=None
    #check if one side is parallel to x-axis and if one side is parallel to y-axis
    if combo[0][1]==combo[1][1]:
        x=abs(combo[0][0]-combo[1][0])
    elif combo[1][1]==combo[2][1]:
        x=abs(combo[1][0]-combo[2][0])
    elif combo[2][1]==combo[0][1]:
        x=abs(combo[2][0]-combo[0][0])
    if combo[0][0]==combo[1][0]:
        y=abs(combo[0][1]-combo[1][1])
    elif combo[1][0]==combo[2][0]:
        y=abs(combo[1][1]-combo[2][1])
    elif combo[2][0]==combo[0][0]:
        y=abs(combo[2][1]-combo[0][1])
    if x!=None and y!=None:
        result=max(result,x*y)

with open('triangles.out','w') as fout:
    fout.write(str(result)+'\n')
