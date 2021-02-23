with open('traffic.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
segments=[[line.split()[0]]+list(map(int,line.split()[1:])) for line in lines[1:]]

#find first and last highway segments without a ramp
for first in range(n):
    if segments[first][0]=='none':
        break
for last in range(n-1,-1,-1):
    if segments[last][0]=='none':
        break

#search from first highway segment without ramp to end
after_range=[segments[first][1],segments[first][2]]
for segment in segments[first+1:]:
    #update range of flow rates depending on highway segment
    if segment[0]=='none':
        after_range[0]=max(after_range[0],segment[1])
        after_range[1]=min(after_range[1],segment[2])
    elif segment[0]=='on':
        after_range[0]+=segment[1]
        after_range[1]+=segment[2]
    else:
        after_range[0]=max(0,after_range[0]-segment[2])
        after_range[1]=max(0,after_range[1]-segment[1])

#search from last highway segment without ramp to start
before_range=[segments[last][1],segments[last][2]]
for segment in segments[last-1::-1]:
    #update range of flow rates depending on highway segment
    if segment[0]=='none':
        before_range[0]=max(before_range[0],segment[1])
        before_range[1]=min(before_range[1],segment[2])
    elif segment[0]=='on':
        before_range[0]=max(0,before_range[0]-segment[2])
        before_range[1]=max(0,before_range[1]-segment[1])
    else:
        before_range[0]+=segment[1]
        before_range[1]+=segment[2]

with open('traffic.out','w') as fout:
    fout.write(' '.join(map(str,before_range))+'\n')
    fout.write(' '.join(map(str,after_range))+'\n')
