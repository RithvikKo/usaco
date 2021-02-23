#standard input
n=int(input())
_,_=map(int,input().split())
_=list(map(int,input().split()))
_=[int(input()) for _ in range(n)]
_=[list(map(int,input().split())) for _ in range(n)]

result=_

print(result)

#file input
with open('_.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
_,_=map(int,lines[0].split())
_=list(map(int,lines[0].split()))
_=[int(line) for line in lines[1:]]
_=[list(map(int,line.split())) for line in lines[1:]]

result=_

with open('_.out','w') as fout:
    fout.write(str(result)+'\n')
