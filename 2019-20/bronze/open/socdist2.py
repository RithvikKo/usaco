with open('socdist2.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
cows=sorted([list(map(int,line.split())) for line in lines[1:]])

largest_r=None
last_cow=cows[0]
#iterate through sorted cows and greedily search for the smallest largest r
for cow in cows[1:]:
    if (not cow[1] and last_cow[1]) or (cow[1] and not last_cow[1]):
        if r is None:
            largest_r=cow[0]-last_cow[0]
        else:
            largest_r=min(largest_r,cow[0]-last_cow[0])
    last_cow=cow

#remove healthy cows
cows=[cow for cow in cows if cow[1]]

result=1
last_cow=cows[0]
#count groups of cows that are separated by largest r or more
for cow in cows[1:]:
    if cow[0]-last_cow[0]>=largest_r:
        result+=1
    last_cow=cow

with open('socdist2.out','w') as fout:
    fout.write(str(result)+'\n')
