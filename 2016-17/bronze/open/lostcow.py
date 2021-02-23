with open('lostcow.in','r') as fin:
    lines=fin.readlines()

x,y=map(int,lines[0].split())

#determine if Bessie is ahead or behind farmer John
ahead=True
if x>y:
    ahead=False

result=0
step=1
current=x
#simulate all of Farmer John's steps
while True:
    if ahead:
        if x+step>=y:
            result+=y-temp
            break
    else:
        if x+step<=y:
            result+=temp-y
            break
    result+=abs(temp-x)+abs(step)
    temp=x+step
    step*=-2

with open('lostcow.out','w') as fout:
    fout.write(str(result)+'\n')
