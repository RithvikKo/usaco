with open('teleport.in','r') as fin:
    lines=fin.readlines()

a,b,x,y=map(int,lines[0].split())

#find distance if teleporter is used
if abs(a-x)<abs(a-y):
    result=abs(a-x)+abs(b-y)
else:
    result=abs(a-y)+abs(b-x)

with open('teleport.out','w') as fout:
    fout.write(str(min(result,abs(a-b)))+'\n')
