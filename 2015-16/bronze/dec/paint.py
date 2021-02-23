with open('paint.in','r') as fin:
    lines=[line for line in fin.readlines()]

a,b=map(int,lines[0].split())
c,d=map(int,lines[1].split())

#calcuate overlap between painted segments
overlap=max(0,min(b,d)-max(a,c))

with open('paint.out','w') as fout:
    fout.write(str(b-a+d-c-overlap)+'\n')
