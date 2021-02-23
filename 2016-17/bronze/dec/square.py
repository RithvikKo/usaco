with open('square.in','r') as fin:
    lines=fin.readlines()

lines=[line.strip() for line in lines]
first=list(map(int,lines[0].split()))
second=list(map(int,lines[1].split()))

#calculate each the farthest point on each side
top=max(first[3],second[3])
bottom=min(first[1],second[1])
right=max(first[2],second[2])
left=min(first[0],second[0])

with open('square.out','w') as fout:
    width=right-left
    height=top-bottom
    if width!=height:
        fout.write(str(max(width,height)**2)+'\n')
    else:
        fout.write(str((width)**2)+'\n')
