with open('shuffle.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
shuffle=list(map(int,lines[1].split()))
ids=list(map(int,lines[2].split()))

#shuffle three times
for _ in range(3):
    new_ids=[None]*n
    #reverse the shuffle
    for i in range(n):
        new_ids[i]=ids[shuffle[i]-1]
    ids=new_ids

with open('shuffle.out','w') as fout:
    for id in ids:
        fout.write(str(id)+'\n')
