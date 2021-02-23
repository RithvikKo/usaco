with open('pails.in','r') as fin:
    lines=fin.readlines()

lines=[line.strip() for line in lines]
x,y,m=map(int,lines[0].split())

result=0
i=0
total=0
#search for every combination of both buckets
while total<=m:
    result=max(result,total+y*((m-total)//y))
    i+=1
    total=i*x

with open('pails.out','w') as fout:
    fout.write(str(result)+'\n')
