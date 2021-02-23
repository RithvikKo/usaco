with open('lifeguards.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
lifeguards=sorted([list(map(int,line.split())) for line in lines[1:]])

result=0
#iterate through every lifeguard
for i in range(n):
    first=True
    #find the time covered with one lifeguard fired
    for j in range(n):
        if j!=i:
            if first:
                last=lifeguards[j]
                time_covered=last[1]-last[0]
                first=False
            else:
                if lifeguards[j][0]<=last[1]:
                    time_covered+=lifeguards[j][1]-last[1]
                else:
                    time_covered+=lifeguards[j][1]-lifeguards[j][0]
                last=lifeguards[j]
    result=max(result,time_covered)

with open('lifeguards.out','w') as fout:
    fout.write(str(result)+'\n')
