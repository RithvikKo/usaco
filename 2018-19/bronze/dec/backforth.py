import copy

with open('backforth.in','r') as fin:
    lines=fin.readlines()

first_barn=list(map(int,lines[0].split()))
second_barn=list(map(int,lines[1].split()))

measures=[[1000,1000,first_barn,second_barn]]
#go through every day
for i in range(4):
    new_measures=[]
    if i%2:
        barn,a,b=3,1,0
    else:
        barn,a,b=2,0,1
    #iterate through all buckets that could be picked
    for measure in measures:
        for bucket in set(measure[barn]):
            new_measure=copy.deepcopy(measure)
            new_measure[a]-=bucket
            new_measure[b]+=bucket
            new_measure[2+a].remove(bucket)
            new_measure[2+b].append(bucket)
            new_measures.append(new_measure)
    measures=new_measures

with open('backforth.out','w') as fout:
    fout.write(str(len(set([measure[0] for measure in measures])))+'\n')
